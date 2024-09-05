'user strict';
// // Para MYSQL El siguiente Script
const mysql = require('mysql2');
const arnoa_dev = {
    host: '192.168.40.95',
    user: 'lulu',
    password: 'Kvm13568791*',
    database: 'alpacladd',
    multipleStatements: true
};

const config = arnoa_dev;
const pool = mysql.createPool(config);
module.exports = pool;

