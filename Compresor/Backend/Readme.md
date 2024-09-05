# Web Scraping para Datos de Compresores

Este proyecto realiza web scraping para obtener datos de un sistema de compresores usando Node.js, Puppeteer y Axios. El objetivo es extraer información crítica del compresor y enviarla a una base de datos a través de una API REST. El script recoge y analiza datos de diversos sensores, protecciones y otras variables relevantes.

## Características

- **Scraping de datos**: Utiliza `Puppeteer` para navegar y extraer información de una interfaz web del compresor.
- **Manejo de datos**: Extrae valores de sensores, protecciones especiales y variables analógicas/digitales.
- **Integración con API**: Envia los datos obtenidos a una API REST usando `Axios`.
- **Actualización periódica**: Los datos se obtienen y envían a intervalos regulares.

## Estructura del Proyecto

### Archivos principales

- `Script.js`: El archivo principal que ejecuta el scraping a intervalos regulares y envía los datos a la base de datos.
- `WebScraping.js`: Contiene la lógica de scraping, incluyendo la extracción de datos de la interfaz web.

### Dependencias

Este proyecto usa las siguientes bibliotecas:

- [`puppeteer`](https://pptr.dev/): Para la automatización de la navegación y scraping web.
- [`axios`](https://github.com/axios/axios): Para hacer solicitudes HTTP a la API.
- [`chalk`](https://github.com/chalk/chalk): Para dar formato a la salida en la terminal.
- [`moment`](https://momentjs.com/): Para manejar y formatear fechas.

## Instalación

### Prerrequisitos

- Node.js (v12 o superior)
- NPM (v6 o superior)

- ## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo:

- Correo electrónico: carlosoviedolr@gmail.com
- Linkedin: [https://www.linkedin.com/in/carlosnicolasoviedocodigoni/] 

Happy coding! 🚀
