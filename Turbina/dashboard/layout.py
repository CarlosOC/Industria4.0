from dash import html, dcc
from .components import (
    panel,
    title,
    led,
    input_row,
    boton_run,
    boton_stop,
    boton_emergencia
)

# ==========================================================
# LAYOUT PRINCIPAL
# ==========================================================
def create_layout():
    return html.Div([

        # ---------- HEADER ----------
        html.Div(
            [
                html.Div("SCADA TURBINA", style={
                    "fontSize": "18px",
                    "fontWeight": "bold",
                    "letterSpacing": "0.5px"
                }),
                html.Div("Operario", style={"opacity": "0.85"})
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "backgroundColor": "#0b3c5d",
                "color": "white",
                "padding": "12px 20px",
                "boxShadow": "0 8px 20px rgba(0,0,0,0.4)"
            }
        ),

        # ---------- TABS ----------
        dcc.Tabs(
            id="tabs",
            value="ESTADOS",
            children=[
                dcc.Tab(label="ESTADOS", value="ESTADOS"),
                dcc.Tab(label="COMANDOS", value="COMANDOS"),
                dcc.Tab(label="GRAFICO", value="GRAFICO"),
            ]
        ),

        html.Div(id="tabs-content")

    ], style={
        "backgroundColor": "#121212",
        "minHeight": "100vh"
    })


# ==========================================================
# TAB: ESTADOS
# ==========================================================
def layout_estados():
    return html.Div([

        # ---------- KPIs ----------
        html.Div([
            kpi("Temperatura", "valor-temperatura", "°C", "#ff9f43"),
            kpi("Presión", "valor-presion", "bar", "#a29bfe"),
            kpi("Velocidad", "valor-velocidad", "rpm", "#4dabf7"),
            kpi("Válvula", "valor-valvula", "%", "#2ecc71"),
        ], style={
            "display": "grid",
            "gridTemplateColumns": "repeat(4, 1fr)",
            "gap": "15px",
            "padding": "20px"
        }),

        # ---------- ESTADO GENERAL ----------
        panel([
            title("ESTADO GENERAL"),

            html.Div([
                estado_inline("Etapa", "etapa-actual"),
                estado_inline("Modo", "modo-control"),
            ], style={
                "display": "flex",
                "gap": "40px",
                "alignItems": "center",
                "padding": "10px"
            })
        ]),

        # ---------- SENSORES + ACTUADORES ----------
        html.Div([

            panel([
                title("SENSORES"),
                led("Quemador 1", "sensor-quemador1"),
                led("Quemador 2", "sensor-quemador2"),
                led("Freno", "sensor-freno"),
                led("Válvula", "sensor-valvula"),
            ]),

            panel([
                title("ACTUADORES"),
                led("Motor", "actuador-motor"),
                led("Junta Neumática", "actuador-juntaneu"),
                led("Chispero 1", "actuador-chipero1"),
                led("Chispero 2", "actuador-chipero2"),
                led("Freno", "actuador-freno"),
                led("PID", "actuador-PID"),
                led("Paro Emergencia", "actuador-paradaemergencia"),
            ])

        ], style={
            "display": "grid",
            "gridTemplateColumns": "1fr 1fr",
            "gap": "20px",
            "padding": "0 20px 20px"
        })

    ])


# ==========================================================
# TAB: COMANDOS
# ==========================================================
def layout_comandos():
    return html.Div([

        panel([
            title("COMANDOS"),
            html.Div([
                boton_run("boton-marcha"),
                boton_stop("boton-parada"),
                boton_emergencia("boton-emergencia"),
            ], style={
                "display": "flex",
                "justifyContent": "space-around",
                "alignItems": "center",
                "padding": "10px"
            })
        ]),

        panel([
            title("CONFIGURACIÓN"),

            html.Div("SETPOINTS", section_label()),
            html.Div([
                input_row("Velocidad SET", "input-velocidad", "rpm"),
                input_row("Válvula SET", "input-valvula", "%"),
            ], style={"display": "flex", "gap": "15px"}),

            input_row("Fricción", "input-friccion", ""),

            html.Hr(style={"borderColor": "rgba(255,255,255,0.15)"}),

            html.Div("CONTROL PID", section_label()),
            html.Div([
                input_row("KP", "input-kp", ""),
                input_row("KI", "input-ki", ""),
                input_row("KD", "input-kd", ""),
            ], style={"display": "flex", "gap": "15px"}),

            html.Div(
                html.Button("Guardar", id="boton-guardar", n_clicks=0,
                    style={
                        "backgroundColor": "#1f77b4",
                        "color": "white",
                        "padding": "10px 22px",
                        "borderRadius": "10px",
                        "border": "none",
                        "fontWeight": "600",
                        "boxShadow": "0 8px 18px rgba(0,0,0,0.35)",
                        "cursor": "pointer"
                    }),
                style={"textAlign": "right", "marginTop": "12px"}
            )
        ])

    ], style={"padding": "20px"})


# ==========================================================
# TAB: GRAFICO
# ==========================================================
def layout_grafico():
    return html.Div([
        panel([
            title("VELOCIDAD EN EL TIEMPO"),
            dcc.Graph(id="grafico_velocidad")
        ])
    ], style={"padding": "20px"})


# ==========================================================
# COMPONENTES AUXILIARES
# ==========================================================
def kpi(label, value_id, unit, color):
    return html.Div([
        html.Div(label, style={
            "fontSize": "13px",
            "color": "#d0d0d0",
            "marginBottom": "6px"
        }),
        html.Div(id=value_id, style={
            "fontSize": "30px",
            "fontWeight": "800",
            "color": color,
            "textShadow": "0 6px 20px rgba(0,0,0,0.45)"
        }),
        html.Div(unit, style={
            "fontSize": "12px",
            "color": "#7fb7ff",
            "marginTop": "4px"
        }),
    ], style={
        "background": "linear-gradient(145deg, #2a2a2a, #1f1f1f)",
        "borderRadius": "14px",
        "padding": "16px",
        "textAlign": "center",
        "boxShadow": "inset 0 0 0 1px rgba(255,255,255,0.05), 0 0 14px rgba(0,0,0,0.55)"
    })


def estado_inline(label, value_id):
    return html.Div([
        html.Span(f"{label}:", style={
            "fontSize": "14px",
            "color": "#d0d0d0",
            "marginRight": "10px"
        }),
        html.Span(id=value_id, style={
            "padding": "6px 16px",
            "borderRadius": "16px",
            "backgroundColor": "#1f77b4",
            "color": "white",
            "fontWeight": "700",
            "fontSize": "14px",
            "boxShadow": "0 6px 14px rgba(0,0,0,0.35)"
        })
    ], style={"display": "flex", "alignItems": "center"})


def section_label():
    return {
        "color": "#7fb7ff",
        "fontSize": "12px",
        "letterSpacing": "1px",
        "margin": "10px 0"
    }
