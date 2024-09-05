'use strict';
const sectorServicios = require('../model/app.model.compresorAtlas');

// Controlador para la inserción de datos del compresor
exports.putDataCompresor = async function (request, response) {
    try {
        const body = request.body;
        const data = await new Promise((resolve, reject) => {
            sectorServicios.putDataCompresor(body, (error, result) => {
                if (error) reject(error);
                else resolve(result);
            });
        });
        response.json(data);
    } catch (error) {
        console.error("Error en putDataCompresor:", error);
        response.status(500).send({ error: error.message });
    }
};

// Controlador para la obtención de datos del compresor
exports.getDataCompresor = async function (request, response) {
    try {
        const data = await new Promise((resolve, reject) => {
            sectorServicios.getDataCompresor((error, result) => {
                if (error) reject(error);
                else resolve(result);
            });
        });
        response.json(data);
    } catch (error) {
        console.error("Error en getDataCompresor:", error);
        response.status(500).send({ error: error.message });
    }
};