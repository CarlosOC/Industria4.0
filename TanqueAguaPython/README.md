# Conexión Modbus con Factory I/O

Este proyecto utiliza el software Factory I/O para realizar una conexión Modbus a un servidor. A continuación se detallan las configuraciones y los datos del tanque utilizados en la simulación.

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

