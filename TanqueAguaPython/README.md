# Conexión Modbus con Factory I/O

Este proyecto utiliza el software Factory I/O para realizar una conexión Modbus y controlar las válvulas de entrada y salida de agua, además de graficar los datos de nivel de agua obtenidos en la simulación.
A continuación se detallan las configuraciones y los datos del tanque utilizados en la simulación.


## Configuración del Proyecto

### Software Utilizado

- **Factory I/O**: Software de simulación industrial utilizado para crear y simular sistemas automatizados.
- **Python**: Lenguaje de programación utilizado para realizar la conexión Modbus y manejar los datos.
- **pymodbus**: Librería Python para comunicaciones Modbus.

### Conexión Modbus

Se utiliza el protocolo Modbus TCP para la comunicación entre Factory I/O y el servidor. La configuración de la conexión es la siguiente:

- **Dirección IP del servidor**: `192.168.1.12`
- **Puerto**: El puerto por defecto de Modbus TCP (502)

### Datos del Tanque

Los datos del tanque utilizados en la simulación son los siguientes:

- **Altura**: 3 metros
- **Diámetro**: 2 metros
- **Radio de la cañería de salida**: 0.125 metros
- **Máximo caudal de entrada**: 0.25 m³/s
- **Máximo caudal de salida**: 0.3543 m³/s
- **Sensor**: Sensor capacitivo

Estos datos han sido obtenidos de la documentación oficial de Factory I/O, que se puede encontrar [aquí](https://docs.factoryio.com/manual/parts/stations/#tank).

## Código

### Control.py

Este script se encarga de controlar el llenado y vaciado de un tanque utilizando válvulas de entrada y salida a través de una conexión Modbus. A continuación se describen sus principales componentes y funcionalidades:

- **Importación de librerías**: Se importan librerías esenciales como `matplotlib` para visualización y `pymodbus` para la comunicación Modbus.
- **Conexión Modbus**: Se establece una conexión Modbus TCP con el servidor en la dirección IP `192.168.1.5`.
- **Definición de válvulas**: Se crean objetos válvula para controlar el caudal de entrada y salida.
- **Definición del tanque**: Se crea un objeto tanque que incluye las válvulas definidas.
- **Interfaz gráfica**: Se crea una interfaz gráfica utilizando `matplotlib` con botones para abrir y cerrar válvulas.
- **Actualización de datos**: Se actualizan y muestran en tiempo real los litros actuales del tanque mediante un gráfico.

### Tanques.py

Este script define las clases `Tanque`, `TanqueConValvulas`, y `Valvula` que se utilizan en el control del tanque en el script `Control.py`. A continuación se describen sus principales componentes y funcionalidades:

- **Clase `Tanque`**: Define un tanque con métodos para llenar, vaciar y medir el nivel y los litros actuales del tanque.
- **Clase `TanqueConValvulas`**: Hereda de la clase `Tanque` y añade la funcionalidad de manejo de válvulas para controlar el flujo de entrada y salida de líquidos.
- **Clase `Valvula`**: Define una válvula con métodos para abrir y cerrar, así como para actualizar su estado a través de la comunicación Modbus.

## Capturas de pantalla

| Tanque Vacio | Tanque Llenandose | Tanque Lleno | Tanque Vaciandose |
|--------------|-------------------|--------------|-------------------|
| ![Tanque Vacio](https://github.com/CarlosOC/Industria4.0/blob/main/TanqueAguaPython/ScreenShot/Inicio.png) | ![Tanque Llenandose](https://github.com/CarlosOC/Industria4.0/blob/main/TanqueAguaPython/ScreenShot/TanqueLlenandose.png) | ![Tanque Lleno](https://github.com/CarlosOC/Industria4.0/blob/main/TanqueAguaPython/ScreenShot/TanqueLleno.png) | ![Tanque Vaciandose](https://github.com/CarlosOC/Industria4.0/blob/main/TanqueAguaPython/ScreenShot/TanqueVaciandose.png) |![Configuracion Factory I/O](https://github.com/CarlosOC/Industria4.0/blob/main/TanqueAguaPython/ScreenShot/TanqueFactory.png) |

---
