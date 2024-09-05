const puppeteer = require('puppeteer');

async function webScraping() {
  let Data;
  let URLCompresor ='http://192.168.100.100/'
  // Inicializar Puppeteer
  const browser = await puppeteer.launch({
    headless: 'new',
    //slowMo: 200,
  });
  const page = await browser.newPage();

  try {
    // Navegar a la página web
    await page.goto(URLCompresor);

    // Esperar a que aparezcan los elementos deseados
    await page.waitForSelector('tr.row, tr.row1');
    await page.waitForSelector('p');
    await page.waitForSelector('td');
    await page.waitForSelector('img');

    // Protecciones Especiales
    // Obtencion del elemento Imagen
    const imgPresionControlNoValida = await page.$(`td.icon#SPECIALPROTECTIONSR0C2 img`);
    const imgParadaForzadaporPlandeReserva = await page.$(`td.icon#SPECIALPROTECTIONSR1C2 img`);
    const imgAjusteLíneaBombeonoEjecutado = await page.$(`td.icon#SPECIALPROTECTIONSR2C2 img`);
    const imgComunicaciónMóduloExpansión = await page.$(`td.icon#SPECIALPROTECTIONSR3C2 img`);
    const imgTiempodepurgaelectrónica1expirado = await page.$(`td.icon#SPECIALPROTECTIONSR4C2 img`);
    const imgTiempodepurgaelectrónica3expirado = await page.$(`td.icon#SPECIALPROTECTIONSR5C2 img`);
    const imgBombeodetectado = await page.$(`td.icon#SPECIALPROTECTIONSR6C2 img`);
    const imgDescargadebidaabombeo = await page.$(`td.icon#SPECIALPROTECTIONSR7C2 img`);
    const imgParadaporalarmadebidoabombeo = await page.$(`td.icon#SPECIALPROTECTIONSR8C2 img`);
    const imgVerificacióndeposiciónIGV = await page.$(`td.icon#SPECIALPROTECTIONSR9C2 img`);
    const imgVerificacióndeposiciónBOV = await page.$(`td.icon#SPECIALPROTECTIONSR10C2 img`);
    const imgErrorVálvulaIGV = await page.$(`td.icon#SPECIALPROTECTIONSR11C2 img`);
    const imgErrordeválvuladeventeo = await page.$(`td.icon#SPECIALPROTECTIONSR12C2 img`);
    const imgParámetrosmotornodefinidos = await page.$(`td.icon#SPECIALPROTECTIONSR13C2 img`);
    const imgAlarmadeservicioparainspeccióndelacoplamiento = await page.$(`td.icon#SPECIALPROTECTIONSR14C2 img`);
    const imgFallobombadeaceiteprincipal = await page.$(`td.icon#SPECIALPROTECTIONSR15C2 img`);
    const imgAltaTemperaturaConvertidorBOV = await page.$(`td.icon#SPECIALPROTECTIONSR16C2 img`);
    const imgSobretempdelconvertidordelaIGV = await page.$(`td.icon#SPECIALPROTECTIONSR17C2 img`);
    // Obtencion del valor OK
    const PresionControlNoValida = ((await imgPresionControlNoValida.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const ParadaForzadaporPlandeReserva = ((await imgParadaForzadaporPlandeReserva.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const AjusteLíneaBombeonoEjecutado = ((await imgAjusteLíneaBombeonoEjecutado.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const ComunicaciónMóduloExpansión = ((await imgComunicaciónMóduloExpansión.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Tiempodepurgaelectrónica1expirado = ((await imgTiempodepurgaelectrónica1expirado.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Tiempodepurgaelectrónica3expirado = ((await imgTiempodepurgaelectrónica3expirado.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Bombeodetectado = ((await imgBombeodetectado.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Descargadebidaabombeo = ((await imgDescargadebidaabombeo.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Paradaporalarmadebidoabombeo = ((await imgParadaporalarmadebidoabombeo.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const VerificacióndeposiciónIGV = ((await imgVerificacióndeposiciónIGV.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const VerificacióndeposiciónBOV = ((await imgVerificacióndeposiciónBOV.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const ErrorVálvulaIGV = ((await imgErrorVálvulaIGV.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Errordeválvuladeventeo = ((await imgErrordeválvuladeventeo.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Parámetrosmotornodefinidos = ((await imgParámetrosmotornodefinidos.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Alarmadeservicioparainspeccióndelacoplamiento = ((await imgAlarmadeservicioparainspeccióndelacoplamiento.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const Fallobombadeaceiteprincipal = ((await imgFallobombadeaceiteprincipal.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const AltaTemperaturaConvertidorBOV = ((await imgAltaTemperaturaConvertidorBOV.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];
    const SobretempdelconvertidordelaIGV = ((await imgSobretempdelconvertidordelaIGV.evaluate((element) => element.getAttribute('src'))).split('images/', 2)[1]).split('.gif', 2)[0];

    const data = await page.evaluate(() => {
      // Obtener todos los elementos
      //  Entradas Analogicas 
      const AceiteCajaEngranaje = Array.from(document.querySelectorAll('td#ANALOGINPUTSR0C2'));
      const dPFitroAire = Array.from(document.querySelectorAll('td#ANALOGINPUTSR1C2'));
      const dPFitroAceite = Array.from(document.querySelectorAll('td#ANALOGINPUTSR2C2'));
      const SalidaElemento3 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR3C2'));
      const SuministroAceiteCajaEngranaje = Array.from(document.querySelectorAll('td#ANALOGINPUTSR4C2'));
      const EntradaAguaRefrigeracion = Array.from(document.querySelectorAll('td#ANALOGINPUTSR5C2'));
      const MotorAccionamiento = Array.from(document.querySelectorAll('td#ANALOGINPUTSR6C2'));
      const EntradaElemento2 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR7C2'));
      const EntradaElemento3 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR8C2'));
      const SalidaCompresorTemperatura = Array.from(document.querySelectorAll('td#ANALOGINPUTSR9C2'));
      const CarterAceite = Array.from(document.querySelectorAll('td#ANALOGINPUTSR10C2'));
      const DevanadoMotorU = Array.from(document.querySelectorAll('td#ANALOGINPUTSR11C2'));
      const DevanadoMotorV = Array.from(document.querySelectorAll('td#ANALOGINPUTSR12C2'));
      const DevanadoMotorW = Array.from(document.querySelectorAll('td#ANALOGINPUTSR13C2'));
      const RodamientoMotorLA = Array.from(document.querySelectorAll('td#ANALOGINPUTSR14C2'));
      const RodamientoMotorLNA = Array.from(document.querySelectorAll('td#ANALOGINPUTSR15C2'));
      const CorrienteMotor = Array.from(document.querySelectorAll('td#ANALOGINPUTSR16C2'));
      const VibracionElemento1 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR17C2'));
      const VibracionElemento2 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR18C2'));
      const VibracionElemento3 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR19C2'));
      const SalidaCompresorPresion = Array.from(document.querySelectorAll('td#ANALOGINPUTSR20C2'));
      const DPToberaElemento2 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR21C2'));
      const DPElemento2 = Array.from(document.querySelectorAll('td#ANALOGINPUTSR22C2'));
      // Salidas Analogicas
      const IGVAbiertaPorcentual = Array.from(document.querySelectorAll('td#ANALOGOUTPUTSR0C2'));
      const BOVCerradaPorcentual = Array.from(document.querySelectorAll('td#ANALOGOUTPUTSR1C2'));
      // Contadores
      const HoraMarcha = Array.from(document.querySelectorAll('td#COUNTERSR0C2'));
      const HoraenCarga = Array.from(document.querySelectorAll('td#COUNTERSR1C2'));
      const ArranquesMotor = Array.from(document.querySelectorAll('td#COUNTERSR2C2'));
      const ArranquesRapidos = Array.from(document.querySelectorAll('td#COUNTERSR3C2'));
      const HorasdelModulo = Array.from(document.querySelectorAll('td#COUNTERSR4C2'));
      const ReleCarga = Array.from(document.querySelectorAll('td#COUNTERSR5C2'));
      const ContadorBombeos = Array.from(document.querySelectorAll('td#COUNTERSR6C2'));
      const ContadorParadasEmergencias = Array.from(document.querySelectorAll('td#COUNTERSR7C2'));
      const ArranquesAcoplados = Array.from(document.querySelectorAll('td#COUNTERSR8C2'));
      const ContadorBombeosAcumulados = Array.from(document.querySelectorAll('td#COUNTERSR9C2'));
      // Entradas Calculadas
      const Refrigerador1Aprox = Array.from(document.querySelectorAll('td#CALCULATEDANALOGINPUTSR0C2'));
      const Refrigerador2Aprox = Array.from(document.querySelectorAll('td#CALCULATEDANALOGINPUTSR1C2'));
      const RefrigeradorPosteriorAprox = Array.from(document.querySelectorAll('td#CALCULATEDANALOGINPUTSR2C2'));
      // Informacion 
      const EstadoMaquina = Array.from(document.querySelectorAll('td#MACHINESTATER0C2'));
      // Entradas Digitales
      const SobreCargaMotor = Array.from(document.querySelectorAll('td#DIGITALINPUTSR0C2'));
      const ContactoRealimentacionArranque = Array.from(document.querySelectorAll('td#DIGITALINPUTSR1C2'));
      const ParadasEmergencia = Array.from(document.querySelectorAll('td#DIGITALINPUTSR2C2'));
      const ArranqueParadaRemoto = Array.from(document.querySelectorAll('td#DIGITALINPUTSR3C2'));
      const CargaDescargaRemoto = Array.from(document.querySelectorAll('td#DIGITALINPUTSR4C2'));
      const SelecAjustePresion = Array.from(document.querySelectorAll('td#DIGITALINPUTSR5C2'));
      const ParadaAlarmaRemota = Array.from(document.querySelectorAll('td#DIGITALINPUTSR6C2'));
      const PurgaCondensadosIC = Array.from(document.querySelectorAll('td#DIGITALINPUTSR7C2'));
      const EntradaPurgaCondensadosIC2 = Array.from(document.querySelectorAll('td#DIGITALINPUTSR8C2'));
      const PurgaCondensadosAC = Array.from(document.querySelectorAll('td#DIGITALINPUTSR9C2'));
      const SobreCargaBombaAceiteAuxiliar = Array.from(document.querySelectorAll('td#DIGITALINPUTSR10C2'));
      const SobreCargaVentiladorDemistor = Array.from(document.querySelectorAll('td#DIGITALINPUTSR11C2'));
      const SobreCargaCalentadorAceite = Array.from(document.querySelectorAll('td#DIGITALINPUTSR12C2'));
      const InterruptorNivelAceite = Array.from(document.querySelectorAll('td#DIGITALINPUTSR13C2'));
      // Salidas Digitales
      const ContactordeLinea = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR0C2'));
      const ContactordeEstrella = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR1C2'));
      const ContactordeTriangulo = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR2C2'));
      const CargaDescarga = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR3C2'));
      const ControlCalentador = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR4C2'));
      const ControlBombaAceiteAuxiliar = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR5C2'));
      const OperacionAutomatica = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR6C2'));
      const AvisoGeneral = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR7C2'));
      const ParadaAlarmaGeneral = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR8C2'));
      const PurgaRefrigeradorIntermedio = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR9C2'));
      const SalidaPurgaCondensadosIC2 = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR10C2'));
      const SalidaPurgaRefrigeradorPosterior = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR11C2'));
      const ValvulaRetencionAgua = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR12C2'));
      const Preparado = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR13C2'));
      const ControlVentiladorDemistor = Array.from(document.querySelectorAll('td#DIGITALOUTPUTSR14C2'));
      // Plan de Servicio
      const PlanServicioA = Array.from(document.querySelectorAll('div#SERVICEPLANR0C3LEVEL'));
      const PlanServicioB = Array.from(document.querySelectorAll('div#SERVICEPLANR1C3LEVEL'));
      const PlanServicioC = Array.from(document.querySelectorAll('div#SERVICEPLANR2C3LEVEL'));
      const PlanServicioD = Array.from(document.querySelectorAll('div#SERVICEPLANR3C3LEVEL'));
      const PlanServicioI = Array.from(document.querySelectorAll('div#SERVICEPLANR4C3LEVEL'));
      // DataTime
      const DataTime = Array.from(document.querySelectorAll('span#load_time'));
      // Extraer el contenido de los elementos    
      const AceiteCajaEngranajeData = AceiteCajaEngranaje.map(elemento => elemento.textContent);
      const dPFitroAireData = dPFitroAire.map(elemento => elemento.textContent);
      const dPFitroAceiteData = dPFitroAceite.map(elemento => elemento.textContent);
      const SalidaElemento3Data = SalidaElemento3.map(elemento => elemento.textContent);
      const SuministroAceiteCajaEngranajeData = SuministroAceiteCajaEngranaje.map(elemento => elemento.textContent);
      const EntradaAguaRefrigeracionData = EntradaAguaRefrigeracion.map(elemento => elemento.textContent);
      const MotorAccionamientoData = MotorAccionamiento.map(elemento => elemento.textContent);
      const EntradaElemento2Data = EntradaElemento2.map(elemento => elemento.textContent);
      const EntradaElemento3Data = EntradaElemento3.map(elemento => elemento.textContent);
      const SalidaCompresorTemperaturaData = SalidaCompresorTemperatura.map(elemento => elemento.textContent);
      const CarterAceiteData = CarterAceite.map(elemento => elemento.textContent);
      const DevanadoMotorUData = DevanadoMotorU.map(elemento => elemento.textContent);
      const DevanadoMotorVData = DevanadoMotorV.map(elemento => elemento.textContent);
      const DevanadoMotorWData = DevanadoMotorW.map(elemento => elemento.textContent);
      const RodamientoMotorLAData = RodamientoMotorLA.map(elemento => elemento.textContent);
      const RodamientoMotorLNAData = RodamientoMotorLNA.map(elemento => elemento.textContent);
      const CorrienteMotorData = CorrienteMotor.map(elemento => elemento.textContent);
      const VibracionElemento1Data = VibracionElemento1.map(elemento => elemento.textContent);
      const VibracionElemento2Data = VibracionElemento2.map(elemento => elemento.textContent);
      const VibracionElemento3Data = VibracionElemento3.map(elemento => elemento.textContent);
      const SalidaCompresorPresionData = SalidaCompresorPresion.map(elemento => elemento.textContent);
      const DPToberaElemento2Data = DPToberaElemento2.map(elemento => elemento.textContent);
      const DPElemento2Data = DPElemento2.map(elemento => elemento.textContent);
      // Salidas Analogicas
      const IGVAbiertaPorcentualData = IGVAbiertaPorcentual.map(elemento => elemento.textContent);
      const BOVCerradaPorcentualData = BOVCerradaPorcentual.map(elemento => elemento.textContent);
      // Contadores
      const HoraMarchaData = HoraMarcha.map(elemento => elemento.textContent);
      const HoraenCargaData = HoraenCarga.map(elemento => elemento.textContent);
      const ArranquesMotorData = ArranquesMotor.map(elemento => elemento.textContent);
      const ArranquesRapidosData = ArranquesRapidos.map(elemento => elemento.textContent);
      const HorasdelModuloData = HorasdelModulo.map(elemento => elemento.textContent);
      const ReleCargaData = ReleCarga.map(elemento => elemento.textContent);
      const ContadorBombeosData = ContadorBombeos.map(elemento => elemento.textContent);
      const ContadorParadasEmergenciasData = ContadorParadasEmergencias.map(elemento => elemento.textContent);
      const ArranquesAcopladosData = ArranquesAcoplados.map(elemento => elemento.textContent);
      const ContadorBombeosAcumuladosData = ContadorBombeosAcumulados.map(elemento => elemento.textContent);
      // Entradas Calculadas
      const Refrigerador1AproxData = Refrigerador1Aprox.map(elemento => elemento.textContent);
      const Refrigerador2AproxData = Refrigerador2Aprox.map(elemento => elemento.textContent);
      const RefrigeradorPosteriorAproxData = RefrigeradorPosteriorAprox.map(elemento => elemento.textContent);
      // Informacion 
      const EstadoMaquinaData = EstadoMaquina.map(elemento => elemento.textContent);
      // Entradas Digitales
      const SobreCargaMotorData = SobreCargaMotor.map(elemento => elemento.textContent);
      const ContactoRealimentacionArranqueData = ContactoRealimentacionArranque.map(elemento => elemento.textContent);
      const ParadasEmergenciaData = ParadasEmergencia.map(elemento => elemento.textContent);
      const ArranqueParadaRemotoData = ArranqueParadaRemoto.map(elemento => elemento.textContent);
      const CargaDescargaRemotoData = CargaDescargaRemoto.map(elemento => elemento.textContent);
      const SelecAjustePresionData = SelecAjustePresion.map(elemento => elemento.textContent);
      const ParadaAlarmaRemotaData = ParadaAlarmaRemota.map(elemento => elemento.textContent);
      const PurgaCondensadosICData = PurgaCondensadosIC.map(elemento => elemento.textContent);
      const EntradaPurgaCondensadosIC2Data = EntradaPurgaCondensadosIC2.map(elemento => elemento.textContent);
      const PurgaCondensadosACData = PurgaCondensadosAC.map(elemento => elemento.textContent);
      const SobreCargaBombaAceiteAuxiliarData = SobreCargaBombaAceiteAuxiliar.map(elemento => elemento.textContent);
      const SobreCargaVentiladorDemistorData = SobreCargaVentiladorDemistor.map(elemento => elemento.textContent);
      const SobreCargaCalentadorAceiteData = SobreCargaCalentadorAceite.map(elemento => elemento.textContent);
      const InterruptorNivelAceiteData = InterruptorNivelAceite.map(elemento => elemento.textContent);
      // Salidas Digitales
      const ContactordeLineaData = ContactordeLinea.map(elemento => elemento.textContent);
      const ContactordeEstrellaData = ContactordeEstrella.map(elemento => elemento.textContent);
      const ContactordeTrianguloData = ContactordeTriangulo.map(elemento => elemento.textContent);
      const CargaDescargaData = CargaDescarga.map(elemento => elemento.textContent);
      const ControlCalentadorData = ControlCalentador.map(elemento => elemento.textContent);
      const ControlBombaAceiteAuxiliarData = ControlBombaAceiteAuxiliar.map(elemento => elemento.textContent);
      const OperacionAutomaticaData = OperacionAutomatica.map(elemento => elemento.textContent);
      const AvisoGeneralData = AvisoGeneral.map(elemento => elemento.textContent);
      const ParadaAlarmaGeneralData = ParadaAlarmaGeneral.map(elemento => elemento.textContent);
      const PurgaRefrigeradorIntermedioData = PurgaRefrigeradorIntermedio.map(elemento => elemento.textContent);
      const SalidaPurgaCondensadosIC2Data = SalidaPurgaCondensadosIC2.map(elemento => elemento.textContent);
      const SalidaPurgaRefrigeradorPosteriorData = SalidaPurgaRefrigeradorPosterior.map(elemento => elemento.textContent);
      const ValvulaRetencionAguaData = ValvulaRetencionAgua.map(elemento => elemento.textContent);
      const PreparadoData = Preparado.map(elemento => elemento.textContent);
      const ControlVentiladorDemistorData = ControlVentiladorDemistor.map(elemento => elemento.textContent);
      // Plan de Servicio
      const PlanServicioAData = PlanServicioA.map(elemento => elemento.textContent);
      const PlanServicioBData = PlanServicioB.map(elemento => elemento.textContent);
      const PlanServicioCData = PlanServicioC.map(elemento => elemento.textContent);
      const PlanServicioDData = PlanServicioD.map(elemento => elemento.textContent);
      const PlanServicioIData = PlanServicioI.map(elemento => elemento.textContent);
      // DataTime
      const DataTimeData = DataTime.map(elemento => elemento.textContent)
      const Datajson = {
        dPFitroAireData: dPFitroAireData[0].split(' ', 2)[0],
        dPFitroAceiteData: dPFitroAceiteData[0].split(' ', 2)[0],
        SalidaElemento3Data: SalidaElemento3Data[0].split(' ', 2)[0],
        SuministroAceiteCajaEngranajeData: SuministroAceiteCajaEngranajeData[0].split(' ', 2)[0],
        EntradaAguaRefrigeracionData: EntradaAguaRefrigeracionData[0].split(' ', 2)[0],
        MotorAccionamientoData: MotorAccionamientoData[0].split(' ', 2)[0],
        EntradaElemento2Data: EntradaElemento2Data[0].split(' ', 2)[0],
        EntradaElemento3Data: EntradaElemento3Data[0].split(' ', 2)[0],
        SalidaCompresorTemperaturaData: SalidaCompresorTemperaturaData[0].split(' ', 2)[0],
        CarterAceiteData: CarterAceiteData[0].split(' ', 2)[0],
        DevanadoMotorUData: DevanadoMotorUData[0].split(' ', 2)[0],
        DevanadoMotorVData: DevanadoMotorVData[0].split(' ', 2)[0],
        DevanadoMotorWData: DevanadoMotorWData[0].split(' ', 2)[0],
        RodamientoMotorLAData: RodamientoMotorLAData[0].split(' ', 2)[0],
        RodamientoMotorLNAData: RodamientoMotorLNAData[0].split(' ', 2)[0],
        CorrienteMotorData: CorrienteMotorData[0].split(' ', 2)[0],
        VibracionElemento1Data: VibracionElemento1Data[0].split(' ', 2)[0],
        VibracionElemento2Data: VibracionElemento2Data[0].split(' ', 2)[0],
        VibracionElemento3Data: VibracionElemento3Data[0].split(' ', 2)[0],
        SalidaCompresorPresionData: SalidaCompresorPresionData[0].split(' ', 2)[0],
        DPToberaElemento2Data: DPToberaElemento2Data[0].split(' ', 2)[0],
        DPElemento2Data: DPElemento2Data[0].split(' ', 2)[0],
        IGVAbiertaPorcentualData: IGVAbiertaPorcentualData[0].split(' ', 2)[0],
        BOVCerradaPorcentualData: BOVCerradaPorcentualData[0].split(' ', 2)[0],
        AceiteCajaEngranajeData: AceiteCajaEngranajeData[0].split(' ', 2)[0],
        HoraMarchaData: HoraMarchaData[0].split(' ', 2)[0],
        HoraenCargaData: HoraenCargaData[0].split(' ', 2)[0],
        ArranquesMotorData: ArranquesMotorData[0].split(' ', 2)[0],
        ArranquesRapidosData: ArranquesRapidosData[0].split(' ', 2)[0],
        HorasdelModuloData: HorasdelModuloData[0].split(' ', 2)[0],
        ReleCargaData: ReleCargaData[0].split(' ', 2)[0],
        ContadorBombeosData: ContadorBombeosData[0].split(' ', 2)[0],
        ContadorParadasEmergenciasData: ContadorParadasEmergenciasData[0].split(' ', 2)[0],
        ArranquesAcopladosData: ArranquesAcopladosData[0].split(' ', 2)[0],
        ContadorBombeosAcumuladosData: ContadorBombeosAcumuladosData[0].split(' ', 2)[0],
        Refrigerador1AproxData: Refrigerador1AproxData[0].split(' ', 2)[0],
        Refrigerador2AproxData: Refrigerador2AproxData[0].split(' ', 2)[0],
        RefrigeradorPosteriorAproxData: RefrigeradorPosteriorAproxData[0].split(' ', 2)[0],
        EstadoMaquinaData: EstadoMaquinaData[0].split(' ', 2)[0],
        SobreCargaMotorData: SobreCargaMotorData[0].split(' ', 2)[0],
        ContactoRealimentacionArranqueData: ContactoRealimentacionArranqueData[0].split(' ', 2)[0],
        ParadasEmergenciaData: ParadasEmergenciaData[0].split(' ', 2)[0],
        ArranqueParadaRemotoData: ArranqueParadaRemotoData[0].split(' ', 2)[0],
        CargaDescargaRemotoData: CargaDescargaRemotoData[0].split(' ', 2)[0],
        SelecAjustePresionData: SelecAjustePresionData[0],
        ParadaAlarmaRemotaData: ParadaAlarmaRemotaData[0].split(' ', 2)[0],
        PurgaCondensadosICData: PurgaCondensadosICData[0],
        EntradaPurgaCondensadosIC2Data: EntradaPurgaCondensadosIC2Data[0],
        PurgaCondensadosACData: PurgaCondensadosACData[0],
        SobreCargaBombaAceiteAuxiliarData: SobreCargaBombaAceiteAuxiliarData[0].split(' ', 2)[0],
        SobreCargaVentiladorDemistorData: SobreCargaVentiladorDemistorData[0].split(' ', 2)[0],
        SobreCargaCalentadorAceiteData: SobreCargaCalentadorAceiteData[0].split(' ', 2)[0],
        InterruptorNivelAceiteData: InterruptorNivelAceiteData[0].split(' ', 2)[0],
        ContactordeLineaData: ContactordeLineaData[0],
        ContactordeEstrellaData: ContactordeEstrellaData[0].split(' ', 2)[0],
        ContactordeTrianguloData: ContactordeTrianguloData[0].split(' ', 2)[0],
        CargaDescargaData: CargaDescargaData[0].split(' ', 2)[0],
        ControlCalentadorData: ControlCalentadorData[0].split(' ', 2)[0],
        ControlBombaAceiteAuxiliarData: ControlBombaAceiteAuxiliarData[0].split(' ', 2)[0],
        OperacionAutomaticaData: OperacionAutomaticaData[0].split(' ', 2)[0],
        AvisoGeneralData: AvisoGeneralData[0].split(' ', 2)[0],
        ParadaAlarmaGeneralData: ParadaAlarmaGeneralData[0].split(' ', 2)[0],
        PurgaRefrigeradorIntermedioData: PurgaRefrigeradorIntermedioData[0].split(' ', 2)[0],
        SalidaPurgaCondensadosIC2Data: SalidaPurgaCondensadosIC2Data[0].split(' ', 2)[0],
        SalidaPurgaRefrigeradorPosteriorData: SalidaPurgaRefrigeradorPosteriorData[0].split(' ', 2)[0],
        ValvulaRetencionAguaData: ValvulaRetencionAguaData[0].split(' ', 2)[0],
        PreparadoData: PreparadoData[0],
        ControlVentiladorDemistorData: ControlVentiladorDemistorData[0],
        PlanServicioAData: PlanServicioAData[0].split(' ', 2)[0],
        PlanServicioBData: PlanServicioBData[0].split(' ', 2)[0],
        PlanServicioCData: PlanServicioCData[0].split(' ', 2)[0],
        PlanServicioDData: PlanServicioDData[0].split(' ', 2)[0],
        PlanServicioIData: PlanServicioIData[0].split(' ', 2)[0],
        DataTimeData: (DataTimeData[0].split('Página mostrada en ', 2)[1]).split('  ', 2)
      };

      return { Datajson };

    });
    // Agregamos las Protecciones Especiales
    data.Datajson.PresionControlNoValida = PresionControlNoValida;
    data.Datajson.ParadaForzadaporPlandeReserva = ParadaForzadaporPlandeReserva;
    data.Datajson.AjusteLíneaBombeonoEjecutado = AjusteLíneaBombeonoEjecutado;
    data.Datajson.ComunicaciónMóduloExpansión = ComunicaciónMóduloExpansión;
    data.Datajson.Tiempodepurgaelectrónica1expirado = Tiempodepurgaelectrónica1expirado;
    data.Datajson.Tiempodepurgaelectrónica3expirado = Tiempodepurgaelectrónica3expirado;
    data.Datajson.Bombeodetectado = Bombeodetectado;
    data.Datajson.Descargadebidaabombeo = Descargadebidaabombeo;
    data.Datajson.Paradaporalarmadebidoabombeo = Paradaporalarmadebidoabombeo;
    data.Datajson.VerificacióndeposiciónIGV = VerificacióndeposiciónIGV;
    data.Datajson.VerificacióndeposiciónBOV = VerificacióndeposiciónBOV;
    data.Datajson.ErrorVálvulaIGV = ErrorVálvulaIGV;
    data.Datajson.Errordeválvuladeventeo = Errordeválvuladeventeo;
    data.Datajson.Parámetrosmotornodefinidos = Parámetrosmotornodefinidos;
    data.Datajson.Alarmadeservicioparainspeccióndelacoplamiento = Alarmadeservicioparainspeccióndelacoplamiento;
    data.Datajson.Fallobombadeaceiteprincipal = Fallobombadeaceiteprincipal;
    data.Datajson.AltaTemperaturaConvertidorBOV = AltaTemperaturaConvertidorBOV;
    data.Datajson.SobretempdelconvertidordelaIGV = SobretempdelconvertidordelaIGV;

    Data = data.Datajson

    // Convertimos los datos en float si es numerico
    for (const key in data.Datajson) {
      const value = data.Datajson[key];
      if (key !== 'DataTimeData' && !isNaN(parseFloat(value))) {
        Data[key] = parseFloat(value);
      } else {
        Data[key] = value;
      }
    }
    // console.log("Valores",Data);

  } catch (error) {
    console.error('Ocurrió un error:', error);
  } finally {
    await browser.close();
  }
  return (Data)
}
 
exports.DataWeb = webScraping;
