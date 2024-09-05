# Proyecto de Compresor Atlas

Este proyecto es un sistema completo para el monitoreo y manejo de datos de un compresor de aire Atlas. Está compuesto por tres partes principales: la API, el backend para la recolección de datos, y el frontend para la visualización de datos.

## Especificaciones del Compresor

El compresor ZH560+ tiene las siguientes especificaciones:

- **Máxima presión de trabajo**: 8.8 bar
- **Potencia total nominal**: 541.1 Kw
- **Velocidad del eje de rotación**: 2980 r/min
- **Datos de rendimiento**:
  - A 7 barg: 6566 m³/h
  - A 8 barg: 6397 m³/h
  - A 9 barg: 5908 m³/h
  - A 10.4 barg: 5476 m³/h
  - A 13 barg: 4864 m³/h

## Estructura del Proyecto

El proyecto está dividido en las siguientes carpetas:

- **API**: Contiene el código para la API REST que envia la informacion a la Base de Datos. 

- **Backend**: Contiene el código para el web scraping. Este componente extrae información relevante y la envía a la API.

- **Frontend**: Implementado en React.js, proporciona la interfaz de usuario para visualizar y gestionar los datos del compresor.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, realiza un fork del repositorio y abre un pull request con tus cambios.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo:

- Correo electrónico: carlosoviedolr@gmail.com
- Linkedin: [https://www.linkedin.com/in/carlosnicolasoviedocodigoni/]
 
Happy coding! 🚀
