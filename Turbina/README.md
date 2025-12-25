# 🏭 SCADA Turbina – Industria 4.0 (Python + Dash)
> Proyecto orientado a **Industria 4.0**, automatización industrial y control de procesos.

Sistema **SCADA educativo–industrial** desarrollado en Python que simula y controla una **turbina compresora a combustión**, basado en una **especificación funcional industrial realista** (Ingelearn – Python para la Industria 4.0).

El proyecto integra:
- Modelo dinámico del proceso
- Control PID industrial
- Interfaz SCADA moderna (Dash)
- Comunicación bidireccional en tiempo real
- Arquitectura modular y escalable



---

## 📄 Base funcional del sistema

Este desarrollo se basa en la **Descripción Funcional – Sistema Turbina**, la cual define:

- Turbina compresora ficticia para generación de gas a presión
- Presión de trabajo nominal: **5 bar**
- Velocidad nominal de régimen: **4600 rpm**
- Control local y remoto mediante HMI
- Sistema de arranque, ignición, aceleración, régimen y parada
- Protecciones y paradas de emergencia por condiciones de falla

---

## 🚀 Características principales

✔️ Simulación realista de una turbina industrial  
✔️ Secuencia de arranque en múltiples etapas  
✔️ Control PID automático/manual (4–20 mA equivalente)  
✔️ SCADA web en tiempo real (Dash / Plotly)  
✔️ Paro de emergencia local y remoto  
✔️ Visualización de sensores y actuadores  
✔️ Arquitectura desacoplada proceso ↔ HMI  

---

## 🔄 Secuencia de arranque implementada

La lógica de control reproduce la secuencia definida en la especificación:

1. **Arranque motor auxiliar**  
   - Acoplamiento mediante junta neumática  
   - Aceleración hasta velocidad de autosustentación (~478 rpm)

2. **Ignición**  
   - Activación de chisperos  
   - Apertura inicial de válvula (10 %)  
   - Verificación de llama en ambos quemadores

3. **Aceleración**  
   - Válvula fija al 25 %  
   - Desacople del motor auxiliar a 2750 rpm  

4. **Régimen automático**  
   - Control PID habilitado  
   - Consigna automática: 4600 rpm  

---

## 🛑 Paradas y protecciones

### Parada controlada
- Reducción de válvula al 10 %
- Cierre total posterior
- Aplicación de freno neumático a 2500 rpm

### Parada de emergencia
Se ejecuta inmediatamente ante:
- Pulsador de emergencia (local o tablero)
- Sobrevelocidad (> 5500 rpm)
- Sobrepresión (> 5.5 bar)
- Baja presión sostenida (< 3.3 bar)
- Sobretemperatura (> 350 °C)

Acciones:
- Cierre inmediato de válvula
- Descarga por chimenea de emergencia
- Activación de frenos

---

## 🖥️ Interfaz SCADA

### Variables de proceso
- Temperatura (°C)
- Presión (bar)
- Velocidad (rpm)
- Posición de válvula (%)

### Estado general
- Etapa del proceso
- Modo de control (LOCAL / REMOTO)

### Sensores
- Sensores de llama
- Sensor de freno
- Sensor de válvula

### Actuadores
- Motor auxiliar
- Junta neumática
- Chisperos
- Frenos
- Válvula de emergencia
- Control PID

---

## 🖥️ Capturas del SCADA

> Guardar las imágenes en una carpeta `screenshots/`

![Estados del proceso](screenshots/estados.png)
![Comandos y configuración](screenshots/comandos.png)
![Gráfico de velocidad](screenshots/grafico_velocidad.png)

---

## 🧠 Arquitectura del sistema

```
main.py
 ├─ Hilo de simulación del proceso
 ├─ Comunicación mediante Queues
 └─ Lanzamiento del SCADA

Componentes.py
 └─ Modelo dinámico de la turbina

ControlPID.py
 └─ Controlador PID industrial

dashboard/
 ├─ Dashboard.py   → callbacks y lógica Dash
 ├─ layout.py      → estructura visual
 ├─ components.py  → componentes reutilizables
 └─ styles.css     → estilos personalizados
```

---

## ▶️ Ejecución del proyecto

### Requisitos
- Python 3.10+
- Dash
- Plotly

Instalar dependencias:
```bash
pip install dash plotly
```

Ejecutar:
```bash
python main.py
```

Abrir navegador:
```
http://127.0.0.1:8050
```

---

## 🎯 Objetivo del proyecto

- 🎓 Uso académico (automatización y control)
- 🏭 Simulación industrial realista
- 🧠 Base para gemelos digitales
- 🔧 Plataforma de pruebas para control PID

---

## 👨‍💻 Autor

**Carlos Nicolás Oviedo Codigoni**  
Ingeniería / Automatización / Programación  
Docente Universitario – Programación & Control  
Argentina 🇦🇷  

---

## 📄 Licencia

Proyecto de uso educativo y demostrativo.  
Libre para estudio, modificación y mejora.

