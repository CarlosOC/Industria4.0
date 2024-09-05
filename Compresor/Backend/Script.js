const axios = require('axios');
const chalk = require('chalk');
const moment = require('moment');
const Datos = require('./WebScraping.js');
let Data;
let URLAPI="http://192.168.40.95:3010/compresor/atlas"
let identificadorIntervaloDeTiempo = 60000
async function main()
{
    setInterval(async () => {
        try {
            Data = await Datos.DataWeb();
            console.log(Data);
            await Database(Data);  
            SalidaTerminal();
        } catch (error) {
            console.error("Error en la ejecución del scraping:", error);
        }
    }, identificadorIntervaloDeTiempo);
}
async function Database(DataCompresor)
{
    let aux = DataCompresor.DataTimeData[1].split("/", 3);
    DataCompresor.DataTimeData[1] = aux[2] + "/" + aux[1] + "/" + aux[0];

    try {
        const resultApi = await axios.put(URLAPI, DataCompresor);
        console.log("Datos enviados a la API:", resultApi.data);
    } catch (error) {
        console.error("Error al enviar los datos a la API:", error);
    }
  console.log(DataCompresor)
}
function SalidaTerminal() 
    {
           const FechaHoraSistema = new Date();
        console.log(chalk.green("Script ATLAS DATA: "), chalk.blue("[Envia Datos del Compresor ATLAS a la DB]"));
        console.log(chalk.red("Fecha [Sistema]: " + moment(FechaHoraSistema).format('DD/MM/YYYY') + " - " + "Hora [Sistema]: " + moment(FechaHoraSistema).format('LTS')));
  }

main()
