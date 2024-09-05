'use strict';
const pool = require('./dbconfig.js');
const sql = require('mssql');
const moment = require('moment');

// Definición de la función Datos para manejar la estructura del dato
var Datos = function (dato) { };

// Función para insertar o actualizar los datos del compresor
Datos.putDataCompresor = async function putDataCompresor(body, result) {
    try {
        // Desestructuración de los datos provenientes del cuerpo del request
        let {
            dPFitroAireData,
            dPFitroAceiteData,
            SalidaElemento3Data,
            SuministroAceiteCajaEngranajeData,
            EntradaAguaRefrigeracionData,
            MotorAccionamientoData,
            EntradaElemento2Data,
            EntradaElemento3Data,
            SalidaCompresorTemperaturaData,
            CarterAceiteData,
            DevanadoMotorUData,
            DevanadoMotorVData,
            DevanadoMotorWData,
            RodamientoMotorLAData,
            RodamientoMotorLNAData,
            CorrienteMotorData,
            VibracionElemento1Data,
            VibracionElemento2Data,
            VibracionElemento3Data,
            SalidaCompresorPresionData,
            DPToberaElemento2Data,
            DPElemento2Data,
            IGVAbiertaPorcentualData,
            BOVCerradaPorcentualData,
            AceiteCajaEngranajeData,
            HoraMarchaData,
            HoraenCargaData,
            ArranquesMotorData,
            ArranquesRapidosData,
            HorasdelModuloData,
            ReleCargaData,
            ContadorBombeosData,
            ContadorParadasEmergenciasData,
            ArranquesAcopladosData,
            ContadorBombeosAcumuladosData,
            Refrigerador1AproxData,
            Refrigerador2AproxData,
            RefrigeradorPosteriorAproxData,
            EstadoMaquinaData,
            SobreCargaMotorData,
            ContactoRealimentacionArranqueData,
            ParadasEmergenciaData,
            ArranqueParadaRemotoData,
            CargaDescargaRemotoData,
            SelecAjustePresionData,
            ParadaAlarmaRemotaData,
            PurgaCondensadosICData,
            EntradaPurgaCondensadosIC2Data,
            PurgaCondensadosACData,
            SobreCargaBombaAceiteAuxiliarData,
            SobreCargaVentiladorDemistorData,
            SobreCargaCalentadorAceiteData,
            InterruptorNivelAceiteData,
            ContactordeLineaData,
            ContactordeEstrellaData,
            ContactordeTrianguloData,
            CargaDescargaData,
            ControlCalentadorData,
            ControlBombaAceiteAuxiliarData,
            OperacionAutomaticaData,
            AvisoGeneralData,
            ParadaAlarmaGeneralData,
            PurgaRefrigeradorIntermedioData,
            SalidaPurgaCondensadosIC2Data,
            SalidaPurgaRefrigeradorPosteriorData,
            ValvulaRetencionAguaData,
            PreparadoData,
            ControlVentiladorDemistorData,
            PlanServicioAData,
            PlanServicioBData,
            PlanServicioCData,
            PlanServicioDData,
            PlanServicioIData,
            DataTimeData
        } = body;

        // Validación de los datos mínimos requeridos
        if (!DataTimeData || DataTimeData.length < 2) {
            throw new Error('Faltan los campos de fecha y hora.');
        }

        let FechaCarga = DataTimeData[1], HoraCarga = DataTimeData[0];
        const placeholders = Array.from({ length: Object.keys(body).length + 1 }, () => "?").join(", ");

        // Consulta de inserción o actualización a la base de datos
        const response = await pool.query(
            `CALL alpacladd.SectorServicio_CompresorAtlas_ADDUPDATE (${placeholders})`,
            [
                FechaCarga, HoraCarga,
                dPFitroAireData, dPFitroAceiteData, SalidaElemento3Data, SuministroAceiteCajaEngranajeData,
                EntradaAguaRefrigeracionData, MotorAccionamientoData, EntradaElemento2Data, EntradaElemento3Data,
                SalidaCompresorTemperaturaData, CarterAceiteData, DevanadoMotorUData, DevanadoMotorVData,
                DevanadoMotorWData, RodamientoMotorLAData, RodamientoMotorLNAData, CorrienteMotorData,
                VibracionElemento1Data, VibracionElemento2Data, VibracionElemento3Data, SalidaCompresorPresionData,
                DPToberaElemento2Data, DPElemento2Data, IGVAbiertaPorcentualData, BOVCerradaPorcentualData,
                AceiteCajaEngranajeData, HoraMarchaData, HoraenCargaData, ArranquesMotorData, ArranquesRapidosData,
                HorasdelModuloData, ReleCargaData, ContadorBombeosData, ContadorParadasEmergenciasData,
                ArranquesAcopladosData, ContadorBombeosAcumuladosData, Refrigerador1AproxData,
                Refrigerador2AproxData, RefrigeradorPosteriorAproxData, EstadoMaquinaData, SobreCargaMotorData,
                ContactoRealimentacionArranqueData, ParadasEmergenciaData, ArranqueParadaRemotoData,
                CargaDescargaRemotoData, SelecAjustePresionData, ParadaAlarmaRemotaData, PurgaCondensadosICData,
                EntradaPurgaCondensadosIC2Data, PurgaCondensadosACData, SobreCargaBombaAceiteAuxiliarData,
                SobreCargaVentiladorDemistorData, SobreCargaCalentadorAceiteData, InterruptorNivelAceiteData,
                ContactordeLineaData, ContactordeEstrellaData, ContactordeTrianguloData, CargaDescargaData,
                ControlCalentadorData, ControlBombaAceiteAuxiliarData, OperacionAutomaticaData, AvisoGeneralData,
                ParadaAlarmaGeneralData, PurgaRefrigeradorIntermedioData, SalidaPurgaCondensadosIC2Data,
                SalidaPurgaRefrigeradorPosteriorData, ValvulaRetencionAguaData, PreparadoData,
                ControlVentiladorDemistorData, PlanServicioAData, PlanServicioBData, PlanServicioCData,
                PlanServicioDData, PlanServicioIData
            ]
        );

        // Consulta para obtener advertencias de la base de datos
        const warnings = await pool.query('SHOW WARNINGS');
        if (warnings.length > 0) {
            console.warn('Advertencias:', warnings);
        }

        // Respuesta final
        if (response.serverStatus === 0 || response.serverStatus === 2) {
            response.info = 'Operación completada exitosamente';
        }

        result(null, response);
    } catch (error) {
        console.error("Error en la operación:", error);
        result(null, { error: error.message });
    }
};

// Función para obtener datos del compresor
Datos.getDataCompresor = async function getDataCompresor(result) {
    try {
        let SetPoints = {
            // Aquí se definen los valores de los puntos de ajuste
            "dPFitroAire": 0.5,
            "dPFitroAceite": 1,
            "SalidaElemento3": 0,
            // ... (otros puntos de ajuste)
        };

        // Consulta para obtener el estado más reciente del compresor
        const response = await pool.query("SELECT * FROM alpacladd.sectorservicios_compresor_atlas_operationstate ORDER BY id DESC;");
        
        const Datos = {
            DatosActuales: response[0],
            SetPoints: SetPoints
        };

        result(null, Datos);
    } catch (error) {
        console.error("Error al obtener los datos:", error);
        result(null, { error: error.message });
    }
};

module.exports = Datos;