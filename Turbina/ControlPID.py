class PID:
    """
    PID industrial (discreto) con:
    - anti-windup por back-calculation
    - derivada sobre medición (más robusta)
    - bumpless transfer (MAN/AUTO sin salto)
    - límites de salida
    - dt configurable
    """

    def __init__(self, kP=2.0, kI=0.2, kD=0.02, out_min=0.0, out_max=100.0, tau_d=0.05, aw_gain=0.5):
        self.kP = float(kP)
        self.kI = float(kI)   # 1/s
        self.kD = float(kD)   # s

        self.out_min = float(out_min)
        self.out_max = float(out_max)

        # Filtro para derivada (0..inf). Más alto = más filtrado.
        self.tau_d = float(tau_d)

        # Ganancia anti-windup (back calculation). 0..1 típico.
        self.aw_gain = float(aw_gain)

        self.reset()

    def reset(self):
        self._I = 0.0
        self._prev_meas = None
        self._D = 0.0
        self.output = 0.0

        # para bumpless transfer
        self._manual_output = 0.0
        self._last_mode_auto = False

    def set_tunings(self, kP=None, kI=None, kD=None):
        if kP is not None: self.kP = float(kP)
        if kI is not None: self.kI = float(kI)
        if kD is not None: self.kD = float(kD)

    def set_limits(self, out_min=None, out_max=None):
        if out_min is not None: self.out_min = float(out_min)
        if out_max is not None: self.out_max = float(out_max)

    @staticmethod
    def _clamp(x, lo, hi):
        if x < lo: return lo
        if x > hi: return hi
        return x

    def update(self, meas, setpoint, dt, mode_auto=True, manual_output=0.0):
        """
        meas: medición (PV)
        setpoint: consigna (SP)
        dt: tiempo de muestreo (s)
        mode_auto: True=Auto, False=Manual
        manual_output: salida en manual (%)
        """
        dt = float(dt)
        if dt <= 0:
            return self.output

        meas = float(meas)
        setpoint = float(setpoint)

        # --------------------
        # MODO MANUAL
        # --------------------
        if not mode_auto:
            self.output = self._clamp(float(manual_output), self.out_min, self.out_max)
            self._manual_output = self.output
            self._last_mode_auto = False

            # Mantener prev_meas para derivada suave al volver a Auto
            if self._prev_meas is None:
                self._prev_meas = meas
            return self.output

        # --------------------
        # BUMPLESS TRANSFER (al pasar de MAN->AUTO)
        # Ajusta integral para que el output no salte.
        # --------------------
        if not self._last_mode_auto:
            # P y D se calculan normal; acomodamos I para que:
            # output ≈ manual_output
            error = setpoint - meas
            P = self.kP * error

            # Derivada sobre medición (si no hay prev, cero)
            if self._prev_meas is None:
                dmeas = 0.0
            else:
                dmeas = (meas - self._prev_meas) / dt

            # filtro 1er orden para derivada
            alpha = dt / (self.tau_d + dt) if self.tau_d > 0 else 1.0
            self._D = (1 - alpha) * self._D + alpha * (-self.kD * dmeas)

            # Set integral para “pegar” la salida manual
            target = self._clamp(self._manual_output, self.out_min, self.out_max)
            self._I = target - (P + self._D)

        self._last_mode_auto = True

        # --------------------
        # PID AUTO
        # --------------------
        error = setpoint - meas
        P = self.kP * error

        # Derivada sobre medición: D = -kD * d(meas)/dt (con filtro)
        if self._prev_meas is None:
            dmeas = 0.0
        else:
            dmeas = (meas - self._prev_meas) / dt

        alpha = dt / (self.tau_d + dt) if self.tau_d > 0 else 1.0
        D_new = -self.kD * dmeas
        self._D = (1 - alpha) * self._D + alpha * D_new

        # Integral
        self._I += (self.kI * error) * dt

        # Salida sin saturar
        u_unsat = P + self._I + self._D

        # Saturación
        u = self._clamp(u_unsat, self.out_min, self.out_max)

        # Anti-windup (back calculation): corrige I si saturó
        # I += aw_gain * (u - u_unsat)
        self._I += self.aw_gain * (u - u_unsat)

        # Guardar estados
        self.output = u
        self._prev_meas = meas
        return self.output
