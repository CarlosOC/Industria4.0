import time
import ControlPID


class Turbina:
    """
    TURBINA A GAS – SIMULACIÓN INDUSTRIA 4.0
    A+B+C+D+E:
    - Máquina de estados
    - Modelo físico realista
    - PID industrial (rampa SP, anti-windup, bumpless)
    - Alarmas + Parada de Emergencia automática (según enunciado)
    """

    def __init__(self) -> None:

        # ==================================================
        # CONTROL PID (Industrial)
        # ==================================================
        self.pid = ControlPID.PID(
            kP=2.0, kI=0.25, kD=0.04,
            out_min=0.0, out_max=100.0,
            tau_d=0.08, aw_gain=0.6
        )
        self.pid_habilitado = False

        # --- Setpoint (con rampa) ---
        self.set_velocidad = 0.0          # SP objetivo
        self.sp_vel_ramp = 0.0            # SP efectivo (ramp)
        self.sp_ramp_rate = 300.0         # rpm/s

        # --- Manual output (bumpless) ---
        self.valvula_manual = 0.0

        # ==================================================
        # SENSORES
        # ==================================================
        self.sensor_freno = False
        self.sensor_quemador_1 = False
        self.sensor_quemador_2 = False
        self.sensor_valvula_manual = False

        # ==================================================
        # ACTUADORES
        # ==================================================
        self.act_motor = False
        self.act_junta_neumatica = False
        self.act_chispero_1 = False
        self.act_chispero_2 = False
        self.act_freno = False

        # Emergencia (nuevos actuadores del enunciado)
        self.act_parada_emergencia = False
        self.act_valvula_escape_emergencia = False   # válvula 2 vías de escape
        self.act_quemador_chimenea = False           # chispero/salida emergencia

        # ==================================================
        # VARIABLES DE PROCESO
        # ==================================================
        self.velocidad = 0.0       # rpm
        self.presion = 0.0         # bar
        self.temperatura = 25.0    # °C
        self.valvula = 0.0         # %

        # ==================================================
        # CONFIGURACIÓN
        # ==================================================
        self.set_valvula = 0.0
        self.friccion = 0.22

        # ==================================================
        # PARÁMETROS FÍSICOS
        # ==================================================
        self.inercia = 8.0
        self.aceleracion_max = 300.0   # rpm/s
        self.temp_ambiente = 25.0
        self.temp_max = 450.0

        # ==================================================
        # ESTADO GENERAL
        # ==================================================
        self.modo_control = "LOCAL"
        self.etapa_actual = "DETENIDO"
        self.tiempo_estado = 0.0

        # ==================================================
        # COMANDOS
        # ==================================================
        self.cmd_start = False
        self.cmd_stop = True
        self.cmd_emergencia = False

        # ==================================================
        # ALARMAS / INTERLOCKS (E)
        # ==================================================
        self.alarma_overspeed = False
        self.alarma_overpressure = False
        self.alarma_overtemp = False
        self.alarma_lowpressure_30s = False

        self._lowpressure_timer = 0.0  # acumula tiempo de baja presión

        # Latch de emergencia (si dispara, queda hasta que reinicies el programa
        # o llames a ResetEmergencia()).
        self.emergencia_latch = False
        self.motivo_emergencia = ""

    # ==================================================
    # COMANDOS EXTERNOS
    # ==================================================
    def ComandoStart(self):
        self.cmd_start = True
        self.cmd_stop = False
        print(">> COMANDO START")

    def ComandoStop(self):
        self.cmd_start = False
        self.cmd_stop = True
        print(">> COMANDO STOP")

    def ComandoPE(self):
        self.cmd_emergencia = True
        print(">> COMANDO PARADA DE EMERGENCIA (MANUAL)")

    def ResetEmergencia(self):
        """
        Reset de emergencia (opcional).
        Úsalo solo si querés permitir rearme en la simulación.
        """
        self.cmd_emergencia = False
        self.emergencia_latch = False
        self.motivo_emergencia = ""
        self.alarma_overspeed = False
        self.alarma_overpressure = False
        self.alarma_overtemp = False
        self.alarma_lowpressure_30s = False
        self._lowpressure_timer = 0.0

        self.act_parada_emergencia = False
        self.act_valvula_escape_emergencia = False
        self.act_quemador_chimenea = False
        self.act_freno = False

        if self.etapa_actual == "PARADA_EMERGENCIA":
            self.etapa_actual = "DETENIDO"
            self.tiempo_estado = 0.0

        print(">> RESET EMERGENCIA")

    # ==================================================
    # ACTUADORES
    # ==================================================
    def acoplarMotor(self):
        self.act_motor = True
        time.sleep(1)
        self.act_junta_neumatica = True

    def desacoplarMotor(self):
        if self.act_motor and self.act_junta_neumatica:
            self.act_junta_neumatica = False
            time.sleep(1)
            self.act_motor = False

    # ==================================================
    # RAMPA DE SETPOINT
    # ==================================================
    def _aplicar_rampa_sp(self, dt):
        objetivo = self.set_velocidad
        actual = self.sp_vel_ramp
        max_delta = self.sp_ramp_rate * dt

        if actual < objetivo:
            actual = min(actual + max_delta, objetivo)
        elif actual > objetivo:
            actual = max(actual - max_delta, objetivo)

        self.sp_vel_ramp = actual

    # ==================================================
    # E) EVALUACIÓN DE CONDICIONES DE EMERGENCIA
    # ==================================================
    def _evaluar_emergencias(self, dt):
        """
        Implementa condiciones del enunciado:
        - Overspeed > 5500 rpm
        - Overpressure > 5.5 bar
        - Low pressure < 3.3 bar por 30s cuando vel > 4000 rpm
        - Overtemp > 350 °C
        - PE manual
        """

        # Si ya está latcheada, no re-evaluamos (queda en emergencia)
        if self.emergencia_latch:
            return

        # Overspeed
        if self.velocidad > 5500.0:
            self.alarma_overspeed = True
            self._disparar_emergencia("OVERSPEED > 5500 rpm")
            return

        # Overpressure
        if self.presion > 5.5:
            self.alarma_overpressure = True
            self._disparar_emergencia("OVERPRESSURE > 5.5 bar")
            return

        # Overtemp
        if self.temperatura > 350.0:
            self.alarma_overtemp = True
            self._disparar_emergencia("OVERTEMP > 350 °C")
            return

        # Low pressure por 30s cuando vel > 4000 rpm
        condicion_low = (self.velocidad > 4000.0 and self.presion < 3.3)
        if condicion_low:
            self._lowpressure_timer += dt
            if self._lowpressure_timer >= 30.0:
                self.alarma_lowpressure_30s = True
                self._disparar_emergencia("LOW PRESSURE < 3.3 bar por 30s a >4000 rpm")
                return
        else:
            self._lowpressure_timer = 0.0

        # PE manual
        if self.cmd_emergencia:
            self._disparar_emergencia("PE MANUAL")
            return

    def _disparar_emergencia(self, motivo: str):
        """
        Ejecuta acciones de emergencia:
        - Cierra válvula inmediata
        - Activa escape emergencia + quemador chimenea
        - Aplica freno inmediato
        - Deshabilita PID
        - Cambia estado a PARADA_EMERGENCIA
        """
        self.emergencia_latch = True
        self.motivo_emergencia = motivo

        self.act_parada_emergencia = True
        self.cmd_emergencia = True

        # Acciones
        self.pid_habilitado = False
        self.valvula = 0.0
        self.valvula_manual = 0.0

        self.act_valvula_escape_emergencia = True
        self.act_quemador_chimenea = True
        self.act_freno = True

        self.etapa_actual = "PARADA_EMERGENCIA"
        self.tiempo_estado = 0.0

        print(f">> !!! EMERGENCIA DISPARADA: {motivo}")

    # ==================================================
    # MAQUINA DE ESTADOS
    # ==================================================
    def maquina_estados(self, dt):
        self.tiempo_estado += dt

        # Si está en emergencia, forzar estado y acciones
        if self.cmd_emergencia or self.emergencia_latch:
            self.etapa_actual = "PARADA_EMERGENCIA"

        # ---------------- DETENIDO ----------------
        if self.etapa_actual == "DETENIDO":
            self.valvula = 0.0
            self.pid_habilitado = False
            self.act_motor = False
            self.act_junta_neumatica = False
            self.act_freno = False

            # reset suave del SP ramp
            self.sp_vel_ramp = 0.0

            if self.cmd_start and not self.cmd_emergencia:
                self.cmd_start = False
                self.etapa_actual = "ARRANQUE_MOTOR"
                self.tiempo_estado = 0.0
                print(">> ESTADO: ARRANQUE_MOTOR")

        # ---------------- ARRANQUE MOTOR ----------------
        elif self.etapa_actual == "ARRANQUE_MOTOR":
            self.act_motor = True
            self.act_junta_neumatica = True

            if self.velocidad >= 478:
                self.etapa_actual = "AUTOSUSTENTACION"
                self.tiempo_estado = 0.0
                print(">> ESTADO: AUTOSUSTENTACION")

        # ---------------- AUTOSUSTENTACION ----------------
        elif self.etapa_actual == "AUTOSUSTENTACION":
            self.act_chispero_1 = True
            self.act_chispero_2 = True

            if self.tiempo_estado >= 2.0:
                self.sensor_quemador_1 = True
                self.sensor_quemador_2 = True
                self.valvula = 10.0
                self.valvula_manual = self.valvula
                self.etapa_actual = "IGNICION"
                self.tiempo_estado = 0.0
                print(">> ESTADO: IGNICION")

        # ---------------- IGNICION ----------------
        elif self.etapa_actual == "IGNICION":
            if self.sensor_quemador_1 and self.sensor_quemador_2:
                self.valvula = 25.0
                self.valvula_manual = self.valvula
                self.etapa_actual = "ACELERACION"
                self.tiempo_estado = 0.0
                print(">> ESTADO: ACELERACION")

        # ---------------- ACELERACION ----------------
        elif self.etapa_actual == "ACELERACION":
            self.valvula = 25.0
            self.valvula_manual = self.valvula

            if self.velocidad >= 2750:
                self.desacoplarMotor()

                # Habilitar PID auto con bumpless
                self.pid_habilitado = True
                self.set_velocidad = 4600
                self.sp_vel_ramp = self.velocidad  # rampa desde PV
                self.etapa_actual = "REGIMEN"
                self.tiempo_estado = 0.0
                print(">> ESTADO: REGIMEN")

        # ---------------- REGIMEN ----------------
        elif self.etapa_actual == "REGIMEN":
            if self.cmd_stop:
                self.cmd_stop = False
                self.pid_habilitado = False
                self.valvula = 10.0
                self.valvula_manual = self.valvula
                self.etapa_actual = "PARADA_CONTROLADA"
                self.tiempo_estado = 0.0
                print(">> ESTADO: PARADA_CONTROLADA")

        # ---------------- PARADA CONTROLADA ----------------
        elif self.etapa_actual == "PARADA_CONTROLADA":
            if self.tiempo_estado >= 10.0:
                self.valvula = 0.0

            if self.velocidad <= 2500:
                self.act_freno = True

            if self.velocidad <= 50:
                self.act_freno = False
                self.etapa_actual = "DETENIDO"
                self.tiempo_estado = 0.0
                print(">> ESTADO: DETENIDO")

        # ---------------- PARADA EMERGENCIA ----------------
        elif self.etapa_actual == "PARADA_EMERGENCIA":
            # En emergencia, aseguramos acciones
            self.valvula = 0.0
            self.pid_habilitado = False
            self.act_freno = True
            self.act_parada_emergencia = True
            self.act_valvula_escape_emergencia = True
            self.act_quemador_chimenea = True

    # ==================================================
    # UPDATE: FÍSICA + PID + ALARMAS
    # ==================================================
    def update(self, dt):

        # 1) Máquina de estados (lógica)
        self.maquina_estados(dt)

        # 2) Modelo físico
        potencia = 0.0
        if self.act_motor and self.act_junta_neumatica:
            potencia += 400.0
        if self.sensor_quemador_1 and self.sensor_quemador_2:
            potencia += self.valvula * 20.0

        perdidas = self.friccion * self.velocidad

        aceleracion = (potencia - perdidas) / self.inercia
        if aceleracion > self.aceleracion_max:
            aceleracion = self.aceleracion_max
        if aceleracion < -self.aceleracion_max:
            aceleracion = -self.aceleracion_max

        self.velocidad += aceleracion * dt
        if self.velocidad < 0:
            self.velocidad = 0.0

        # Presión (4600 rpm -> 5 bar)
        self.presion = 5.0 * (self.velocidad / 4600.0)
        self.presion = max(0.0, min(self.presion, 6.0))

# ================= TEMPERATURA (MODELO INDUSTRIAL) =================

        # Potencia térmica proporcional a combustible
        potencia_termica = 0.0
        if self.sensor_quemador_1 and self.sensor_quemador_2:
            potencia_termica = self.valvula * 1.2   # ganancia térmica realista

        # Disipación (función de velocidad y ambiente)
        disipacion = 0.03 * self.velocidad + 5.0

        # Dinámica térmica con inercia
        dT = (potencia_termica - disipacion) * dt / 15.0
        self.temperatura += dT

        # Saturaciones físicas
        if self.temperatura < self.temp_ambiente:
            self.temperatura = self.temp_ambiente

        if self.temperatura > self.temp_max:
            self.temperatura = self.temp_max


        # 3) PID (si no está en emergencia)
        if self.pid_habilitado and not self.emergencia_latch:
            self._aplicar_rampa_sp(dt)
            self.valvula = self.pid.update(
                meas=self.velocidad,
                setpoint=self.sp_vel_ramp,
                dt=dt,
                mode_auto=True,
                manual_output=self.valvula_manual
            )
        else:
            self.valvula = self.pid.update(
                meas=self.velocidad,
                setpoint=self.set_velocidad,
                dt=dt,
                mode_auto=False,
                manual_output=self.valvula_manual
            )

        # 4) Evaluación de emergencias (según enunciado)
        self._evaluar_emergencias(dt)

    # ==================================================
    # CONFIGURACIÓN
    # ==================================================
    def ConfigTurbina(self, set_velocidad, set_valvula, friccion, modo_control):
        self.set_velocidad = float(set_velocidad)
        self.set_valvula = float(set_valvula)
        self.friccion = float(friccion)
        self.modo_control = str(modo_control)

        # Modo manual: salida manual = set_valvula
        self.valvula_manual = self.set_valvula

    # ==================================================
    # ESTADO PARA DASHBOARD
    # ==================================================
    def EstadoTurbina(self):
        return {
            # Sensores
            "Sensor_Quemador1": self.sensor_quemador_1,
            "Sensor_Quemador2": self.sensor_quemador_2,
            "Sensor_Freno": self.sensor_freno,
            "Sensor_Valvula": self.sensor_valvula_manual,

            # Actuadores
            "Actuador_Motor": self.act_motor,
            "Actuador_JuntaNeumatica": self.act_junta_neumatica,
            "Actuador_Chispero1": self.act_chispero_1,
            "Actuador_Chispero2": self.act_chispero_2,
            "Actuador_Freno": self.act_freno,
            "Actuador_PE": self.act_parada_emergencia,
            "Actuador_PID": self.pid_habilitado,

            # Nuevos actuadores emergencia
            "Actuador_EscapeEmergencia": self.act_valvula_escape_emergencia,
            "Actuador_QuemadorChimenea": self.act_quemador_chimenea,

            # Variables
            "Velocidad": self.velocidad,
            "Temperatura": self.temperatura,
            "Presion": self.presion,
            "Valvula": self.valvula,

            # Setpoints
            "VelocidadSet": self.set_velocidad,
            "ValvulaSet": self.set_valvula,
            "ModoControl": self.modo_control,
            "EtapaActual": self.etapa_actual,

            # Alarmas
            "Alarma_Overspeed": self.alarma_overspeed,
            "Alarma_Overpressure": self.alarma_overpressure,
            "Alarma_Overtemp": self.alarma_overtemp,
            "Alarma_LowPressure30s": self.alarma_lowpressure_30s,
            "MotivoEmergencia": self.motivo_emergencia,
        }
