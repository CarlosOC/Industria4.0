from pymodbus.client import ModbusTcpClient
import time
import matplotlib.pyplot as plt
 
 
client = ModbusTcpClient('192.168.1.5') #Direccion del PC
client.connect()

cant_reg = 1
esclavo = 1

NivelTQ=[]

# Inputs:  read_discrete_inputs(StartBoton, 1, esclavo)         print(input.bits[0])
# Input 0: Start Boton
# Input 1: Reset Boton
# Input 2: Stop Boton
StartBoton = 0
ResetBoton = 1
StopBoton  = 2

# Inputs Register: read_input_registers(Level, 1, esclavo)       print(lectura.registers[0])
# REG 0: Level Meter
# REG 1: Flow Meter
# REG 2: Setpoint
Level       = 0
Flow        = 1
Setpoint    = 2

# COILS: write_coil(StartLight, False, esclavo)   # Luz en Boton
# COIL 0: Start Light
# COIL 1: Reset Light
# COIL 2: Stop Light
StartLight = 0
ResetLight = 1
StopLight = 2

# Holding Register write_register
# REG 0: Fill Valve  
# REG 1: Discharge Valve
# REG 2: SP
# REG 3: PV
FillValve = 0  
DischargeValve = 1  
SP = 2  
PV = 3  
 
# Inicializacion en Cero Todo
client.write_coil(StartLight, False, esclavo)   # Luz en Boton
client.write_coil(StopLight, False, esclavo)    # Luz en Boton
client.write_coil(ResetLight, False, esclavo)   # Luz en Boton
 
client.write_register(SP, 0, esclavo)           # Pantallita SP
client.write_register(PV, 0, esclavo)           # Pantallita PV
client.write_register(FillValve, 0, esclavo)
client.write_register(DischargeValve, 0, esclavo)
fig, ax = plt.subplots()

def update_data( NivelActual): 
    NivelTQ.append(NivelActual)
    ax.clear()
    ax.set_ylim(0, 1500)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Nivel del Tanque (L)')
    ax.set_title('Nivel del Tanque en Tiempo Real')
    ax.plot(NivelTQ)   

try:
    client.write_coil(StartLight, True, esclavo)  # Luz en Boton 
    client.write_register(SP, 50, esclavo)        # Pantallita SP
    # client.write_register(PV, 50, esclavo)        # Pantallita PV
    client.write_register(FillValve, 0, esclavo)
    client.write_register(DischargeValve, 0, esclavo) 
    while True:
        lectura = client.read_input_registers(Level, 1, esclavo)  
        print(lectura.registers[0]) 
        update_data( lectura.registers[0])     
        client.write_register(PV, lectura.registers[0], esclavo)           # Pantallita PV
        if lectura.registers[0] == 0:
            client.write_register(FillValve, 1000, esclavo)
            client.write_register(DischargeValve, 0, esclavo) 
        elif lectura.registers[0] == 1000:
            client.write_register(FillValve, 0, esclavo) 
            client.write_register(DischargeValve, 1000, esclavo)
        plt.pause(0.25)  # Actualizar cada segundo
except KeyboardInterrupt:
    client.close()
