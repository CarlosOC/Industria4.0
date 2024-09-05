const express = require('express');
var   cors = require('cors');
const os = require('os');
const fs = require('fs');
const moment=require('moment');
// const crypto = require('crypto');

// let puerto= 3011 //debe ir en el 3010
let puerto= 3010
app = express();

app.use(cors());
app.use(express.json())

 
// Middleware para registrar el tiempo de inicio de la petición
app.use((req, res, next) => {
    req.startTime = performance.now(); // Registrar el tiempo de inicio de la petición
    next();
  });

// Middleware para almacenar información del dispositivo en archivo de texto
app.use(function(req, res, next) {
    // Obtener IP y MAC del dispositivo
    const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
  
    // Obtener tipo de petición
    const metodo = req.method;
  
    // Obtener URL de la petición
    const url = req.originalUrl;
  
    // Obtener la fecha y hora actual
    const timestamp = new Date().toISOString();
    const tiempoRespuesta = performance.now() - req.startTime;
    // Obtener el código de respuesta HTTP
    const codigoRespuesta = res.statusCode;
  
    // Obtener información del servidor
    const nombreServidor = process.env.HOSTNAME; // ejemplo con variable de entorno para el nombre del servidor
    const versionNode = process.version; // versión de Node.js
    const versionAPI = '1.0.0'; // ejemplo con versión de la API fija
  
    // Crear objeto con la información
    const deviceInfo = 
    {
      timestamp: timestamp,
      ip: ip,
      metodo: metodo,
      url: url,
      codigoRespuesta: codigoRespuesta,
      tiempoRespuesta:tiempoRespuesta,
      nombreServidor: nombreServidor,
      versionNode: versionNode,
      versionAPI: versionAPI,
    };
  
    // Convertir objeto a string
    const deviceInfoString = JSON.stringify(deviceInfo);
    // Escribir la información en archivo de texto
    let ruta="./logs/"
    let fecha=new Date

    fecha=moment(fecha).format('YYYY-MM-DD')
    let archivo=(fecha)+'.txt'
    
    fs.appendFile(ruta+archivo, deviceInfoString + '\n', function(err) {
      if (err) throw err;
      console.log('Device info written to file');
    });
    next();
  });

const routes_sectorCompresorAtlas         = require('./app/routes/app.route.compresorAtlas'); 
routes_sectorCompresorAtlas(app);
 
app.listen(puerto,function(){console.log("API Compresor ATLAS:"+ puerto);});

module.exports=app;













 