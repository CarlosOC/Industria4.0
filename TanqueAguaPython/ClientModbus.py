from pymodbus.client import ModbusTcpClient
import time
import matplotlib.pyplot as plt

# Crear cliente Modbus TCP con la dirección IP del servidor
client = ModbusTcpClient('192.168.1.12')  # Dirección del PC
client.connect()

# Configuraciones iniciales
cant_reg = 1  # Cantidad de registros a leer
esclavo = 1   # Dirección del esclavo Modbus

# Lista para almacenar los niveles del tanque
NivelTQ=[]

# Definir las posiciones de los inputs discretos (botones)
# Inputs:  read_discrete_inputs(StartBoton, 1, esclavo)         print(input.bits[0])
# Input 0: Start Boton
# Input 1: Reset Boton
# Input 2: Stop Boton
StartBoton = 0
ResetBoton = 1
StopBoton  = 2

# Definir las posiciones de los registros de entrada
# Inputs Register: read_input_registers(Level, 1, esclavo)       print(lectura.registers[0])
# REG 0: Level Meter
# REG 1: Flow Meter
# REG 2: Setpoint
Level       = 0
Flow        = 1
Setpoint    = 2

# Definir las posiciones de las bobinas (coils)
# COILS: write_coil(StartLight, False, esclavo)   # Luz en Boton
# COIL 0: Start Light
# COIL 1: Reset Light
# COIL 2: Stop Light
StartLight = 0
ResetLight = 1
StopLight = 2

# Definir las posiciones de los registros de retención (holding registers)
# Holding Register write_register
# REG 0: Fill Valve  
# REG 1: Discharge Valve
# REG 2: SP
# REG 3: PV
FillValve = 0  
DischargeValve = 1  
SP = 2  
PV = 3  

# Inicialización de todos los elementos a cero
client.write_coil(StartLight, False, esclavo)   # Luz en Boton
client.write_coil(StopLight, False, esclavo)    # Luz en Boton
client.write_coil(ResetLight, False, esclavo)   # Luz en Boton

client.write_register(SP, 0, esclavo)           # Pantalla SP
client.write_register(PV, 0, esclavo)           # Pantalla PV
client.write_register(FillValve, 0, esclavo)
client.write_register(DischargeValve, 0, esclavo)

# Crear figura para la gráfica
fig, ax = plt.subplots()

# Función para actualizar los datos del nivel del tanque en la gráfica
def update_data(NivelActual):
    NivelTQ.append(NivelActual)
    ax.clear()
    ax.set_ylim(0, 1500)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Nivel del Tanque (L)')
    ax.set_title('Nivel del Tanque en Tiempo Real')
    ax.plot(NivelTQ)   

try:
    # Encender la luz del botón de inicio y establecer el setpoint a 50
    client.write_coil(StartLight, True, esclavo)  # Luz en Boton 
    client.write_register(SP, 50, esclavo)        # Pantalla SP
    # client.write_register(PV, 50, esclavo)        # Pantalla PV
    client.write_register(FillValve, 0, esclavo)
    client.write_register(DischargeValve, 0, esclavo)
    
    # Bucle principal
    while True:
        # Leer el nivel del tanque
        lectura = client.read_input_registers(Level, 1, esclavo)
        print(lectura.registers[0])
        
        # Actualizar los datos y la gráfica
        update_data(lectura.registers[0])
        client.write_register(PV, lectura.registers[0], esclavo)  # Pantalla PV
        
        # Controlar las válvulas de llenado y descarga
        if lectura.registers[0] == 0:
            client.write_register(FillValve, 1000, esclavo)
            client.write_register(DischargeValve, 0, esclavo)
        elif lectura.registers[0] == 1000:
            client.write_register(FillValve, 0, esclavo)
            client.write_register(DischargeValve, 1000, esclavo)
        
        plt.pause(0.25)  # Actualizar cada 0.25 segundos
except KeyboardInterrupt:
    # Cerrar la conexión al cliente Modbus cuando se interrumpe el programa
    client.close()
