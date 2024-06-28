# Ejercicio:
# Factory IO: Llenado de Tanque.
# Datos: 
        # Height: 3 m
        # Diameter: 2 m
        # Discharge pipe radius: 0.125 m
        # Max. input flow: 0.25 m³/s
        # Max. output flow: 0.3543 m³/s
        # Capacitive sensors can detect liquid
# Ref: https://docs.factoryio.com/manual/parts/stations/#tank  
 
import matplotlib.pyplot as plt
from matplotlib.widgets import Button,TextBox
from pymodbus.client import ModbusTcpClient
from Tanques import TanqueConValvulas, Valvula
import time
 
# Crear un objeto cliente Modbus
client = ModbusTcpClient('192.168.1.5')

V1 = Valvula(tipo="Entrada", caudal=0.25, Direccion=0, cliente=client,esclavo=1)
V2 = Valvula(tipo="Salida", caudal=0.3543, Direccion=1, cliente=client,esclavo=1)

# Lista para almacenar los litros actuales del tanque
litros = []
# Crear un objeto Tanque
TQ1 = TanqueConValvulas(diametro=2, altura=3, nivel_maximo=1000, cliente=client, esclavo=1,sensorLevel=0, valvulas=[V1, V2])

# Crear una figura de Matplotlib para el gráfico
fig, ax = plt.subplots()

# Función para abrir la válvula de entrada 1
def abrir_valvula(event):
    TQ1.abrir_valvula(1)

# Función para cerrar la válvula de entrada 1
def cerrar_valvula(event):
    TQ1.cerrar_valvula(1)
# Función para abrir la válvula de salida 1
def abrir_valvula_salida(event):
    TQ1.abrir_valvula(2)  # Usamos el índice 2 para la válvula de salida

# Función para cerrar la válvula de salida 1
def cerrar_valvula_salida(event):
    TQ1.cerrar_valvula(2)  # Usamos el índice 2 para la válvula de salida

# Crear botones interactivos en la gráfica
abrir_button = Button(plt.axes([0.9, 0.75, 0.1, 0.05]), 'Abrir V1')
cerrar_button = Button(plt.axes([0.9, 0.7, 0.1, 0.05]), 'Cerrar V1')
abrir_button.on_clicked(abrir_valvula)
cerrar_button.on_clicked(cerrar_valvula)

abrir_button_salida = Button(plt.axes([0.9, 0.5, 0.1, 0.05]), 'Abrir V2')
cerrar_button_salida = Button(plt.axes([0.9, 0.55, 0.1, 0.05]), 'Cerrar V2')
abrir_button_salida.on_clicked(abrir_valvula_salida)
cerrar_button_salida.on_clicked(cerrar_valvula_salida)

# Crear un widget de texto para mostrar los litros actuales
litros_text = TextBox(plt.axes([0.81, 0.01, 0.3, 0.05]), 'Litros:')

# Función de actualización para el gráfico en tiempo real
def update_data():
    TQ1.update()
    litros_text.set_val(f'{TQ1.litros_actual:.2f}')
    litros.append(TQ1.litros_actual)
    ax.clear()
    ax.set_ylim(0, 1500)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Nivel del Tanque (L)')
    ax.set_title('Nivel del Tanque en Tiempo Real')
    ax.plot(litros)

# Actualizar el gráfico en tiempo real con plt.pause
while True:    
    update_data()
    plt.pause(1)  # Actualizar cada segundo

# Mostrar la gráfica y botones
plt.show()