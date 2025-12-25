"""
==========================================================
CONTROL PID INDUSTRIAL DISCRETO
----------------------------------------------------------
Características:
• Anti-windup (back-calculation)
• Derivada sobre medición
• Bumpless transfer MAN ↔ AUTO
• Límites de salida
==========================================================
"""

from threading import Thread
from multiprocessing import Queue
import time

from dashboard.Dashboard import create_dashboard
from Componentes import Turbina


# ==========================================================
# LOOP PRINCIPAL: PROCESO ↔ SCADA
# ==========================================================
def update_data(turbina, data_queue, accion_queue, sample_time):
    """
    Hilo en segundo plano que:
    - Lee comandos del SCADA
    - Actualiza el modelo de la turbina
    - Envía el estado actual al Dashboard

    turbina      : instancia del modelo físico
    data_queue   : cola → datos hacia el SCADA
    accion_queue : cola ← comandos desde el SCADA
    sample_time  : tiempo de muestreo [s]
    """

    # Origen del paro de emergencia (local / remoto)
    pe_origen = "LOCAL"

    while True:

        # --------------------------------------------------
        # 1️⃣ COMANDOS DESDE SCADA
        # --------------------------------------------------
        if not accion_queue.empty():
            info = accion_queue.get()
            accion = info.get("accion", 0)

            # RUN
            if accion == 1:
                turbina.ComandoStart()

            # STOP
            elif accion == 2:
                turbina.ComandoStop()

            # PARO DE EMERGENCIA REMOTO
            elif accion == 3:
                turbina.ComandoPE()
                pe_origen = "REMOTO"

            # GUARDAR CONFIGURACIÓN
            elif accion == 4:
                turbina.ConfigTurbina(
                    info.get("velocidad", turbina.set_velocidad),
                    info.get("valvula", turbina.set_valvula),
                    info.get("friccion", turbina.friccion),
                    "REMOTO"
                )

                # --- Parámetros PID ---
                if info.get("kp") is not None:
                    turbina.pid.kP = info["kp"]
                if info.get("ki") is not None:
                    turbina.pid.kI = info["ki"]
                if info.get("kd") is not None:
                    turbina.pid.kD = info["kd"]

                print(">> CONFIGURACIÓN APLICADA DESDE SCADA")

        # --------------------------------------------------
        # 2️⃣ ACTUALIZAR MODELO FÍSICO
        # --------------------------------------------------
        turbina.update(sample_time)

        # Obtener snapshot del estado actual
        estado = turbina.EstadoTurbina()

        # --------------------------------------------------
        # 3️⃣ PREPARAR PAYLOAD PARA SCADA
        # --------------------------------------------------
        payload = {
            # Variables de proceso
            "velocidad": estado.get("Velocidad", 0.0),
            "temperatura": estado.get("Temperatura", 25.0),
            "presion": estado.get("Presion", 0.0),
            "valvula": estado.get("Valvula", 0.0),

            # Setpoints
            "Set_velocidad": estado.get("VelocidadSet", 0.0),
            "Set_valvula": estado.get("ValvulaSet", 0.0),

            # Estado general
            "modo_control": estado.get("ModoControl", ""),
            "etapa_actual": estado.get("EtapaActual", ""),

            # Sensores
            "sensor_quemador1": estado.get("Sensor_Quemador1", False),
            "sensor_quemador2": estado.get("Sensor_Quemador2", False),
            "sensor_freno": estado.get("Sensor_Freno", False),
            "sensor_valvula": estado.get("Sensor_Valvula", False),

            # Actuadores
            "actuador_motor": estado.get("Actuador_Motor", False),
            "actuador_juntaneu": estado.get("Actuador_JuntaNeumatica", False),
            "actuador_chipero1": estado.get("Actuador_Chispero1", False),
            "actuador_chipero2": estado.get("Actuador_Chispero2", False),
            "actuador_freno": estado.get("Actuador_Freno", False),
            "actuador_pid": estado.get("Actuador_PID", False),

            # Emergencia
            "pe_activo": estado.get("Actuador_PE", False),
            "pe_origen": pe_origen,
        }

        # Limpiar cola para no acumular datos viejos
        while data_queue.qsize() > 5:
            try:
                data_queue.get_nowait()
            except:
                break

        data_queue.put(payload)

        time.sleep(sample_time)


# ==========================================================
# MAIN
# ==========================================================
def main():
    """
    Punto de entrada del sistema
    """

    # ---------- Colas de comunicación ----------
    data_queue = Queue()    # Proceso → SCADA
    accion_queue = Queue()  # SCADA → Proceso

    # ---------- Modelo ----------
    turbina = Turbina()
    sample_time = 0.5  # segundos

    # ---------- Hilo de simulación ----------
    hilo_proceso = Thread(
        target=update_data,
        args=(turbina, data_queue, accion_queue, sample_time),
        daemon=True
    )
    hilo_proceso.start()

    # ---------- Dashboard ----------
    app = create_dashboard(data_queue, accion_queue)

    app.run_server(
        debug=True,
        host="127.0.0.1",
        port=8050
    )


if __name__ == "__main__":
    main()
