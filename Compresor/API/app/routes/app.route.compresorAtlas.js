'use strict';
module.exports = function(app) {
    const compresorAtlas = require('../controller/app.controller.compresorAtlas');

    // Ruta para insertar o actualizar datos del compresor
    app.route('/api/compresor/putData')
        .post(compresorAtlas.putDataCompresor);

    // Ruta para obtener los datos del compresor
    app.route('/api/compresor/getData')
        .get(compresorAtlas.getDataCompresor);
};