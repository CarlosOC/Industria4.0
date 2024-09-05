# API para el Compresor Atlas

Este proyecto proporciona una API REST para manejar datos relacionados con un compresor de aire Atlas. La API permite realizar operaciones básicas como obtener información del rendimiento del compresor a diferentes niveles de presión.


## Características

- **Obtención de datos del compresor**: Puedes obtener el rendimiento del compresor en función de la presión ingresada.
- **API REST**: Se implementa una API RESTful utilizando Node.js y Express.

## Requisitos

Para ejecutar este proyecto necesitas tener instalado:

- [Node.js](https://nodejs.org/) (v12 o superior)
- [npm](https://www.npmjs.com/) (v6 o superior)

## Estructura de la API

├── routes/
│   └── app.route.compresorAtlas.js  # Definición de rutas para la API del compresor
├── server.js                        # Archivo principal del servidor
├── package.json                     # Dependencias y configuración del proyecto
└── README.md                        # Documentación del proyecto
