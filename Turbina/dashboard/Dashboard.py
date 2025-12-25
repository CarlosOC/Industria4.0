from dash import Dash, Input, Output, State, callback_context, html, dcc
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
import queue
import time

from .layout import (
    create_layout,
    layout_estados,
    layout_comandos,
    layout_grafico
)


def create_dashboard(data_queue, accion_queue):

    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = create_layout()

    # ---------------- RENDER TABS ----------------
    @app.callback(
        Output("tabs-content", "children"),
        Input("tabs", "value")
    )
    def render_tabs(tab):
        if tab == "ESTADOS":
            return layout_estados()
        elif tab == "COMANDOS":
            return layout_comandos()
        elif tab == "GRAFICO":
            return layout_grafico()
        return html.Div("Tab no válida")

    # ---------------- UPDATE DISPLAY ----------------
    @app.callback(
        [
            Output("valor-temperatura", "children"),
            Output("valor-presion", "children"),
            Output("valor-velocidad", "children"),
            Output("valor-valvula", "children"),

            Output("modo-control", "children"),
            Output("etapa-actual", "children"),

            Output("sensor-quemador1", "style"),
            Output("sensor-quemador2", "style"),
            Output("sensor-freno", "style"),
            Output("sensor-valvula", "style"),

            Output("actuador-motor", "style"),
            Output("actuador-juntaneu", "style"),
            Output("actuador-chipero1", "style"),
            Output("actuador-chipero2", "style"),
            Output("actuador-freno", "style"),
            Output("actuador-PID", "style"),
            Output("actuador-paradaemergencia", "style"),
        ],
        Input("tabs", "value")
    )
    def update_display(_):

        if data_queue.empty():
            raise PreventUpdate

        data = data_queue.get()

        def led_style(active):
            return {
                "backgroundColor": "#3fb950" if active else "#f85149",
                "width": "28px",
                "height": "14px",
                "borderRadius": "7px"
            }

        return (
            f"{data['temperatura']:.2f}",
            f"{data['presion']:.2f}",
            f"{data['velocidad']:.2f}",
            f"{data['valvula']:.2f}",

            data["modo_control"],
            data["etapa_actual"],

            led_style(data["sensor_quemador1"]),
            led_style(data["sensor_quemador2"]),
            led_style(data["sensor_freno"]),
            led_style(data["sensor_valvula"]),

            led_style(data["actuador_motor"]),
            led_style(data["actuador_juntaneu"]),
            led_style(data["actuador_chipero1"]),
            led_style(data["actuador_chipero2"]),
            led_style(data["actuador_freno"]),
            led_style(data["actuador_pid"]),
            led_style(data["pe_activo"]),
        )

    # ---------------- COMANDOS ----------------
    @app.callback(
        Output("tabs", "value", allow_duplicate=True),
        [
            Input("boton-marcha", "n_clicks"),
            Input("boton-parada", "n_clicks"),
            Input("boton-emergencia", "n_clicks"),
            Input("boton-guardar", "n_clicks"),
        ],
        [
            State("input-velocidad", "value"),
            State("input-valvula", "value"),
            State("input-friccion", "value"),
            State("input-kp", "value"),
            State("input-ki", "value"),
            State("input-kd", "value"),
        ],
        prevent_initial_call=True
    )
    def enviar_comandos(
        m, p, e, g,
        vel, valv, fric, kp, ki, kd
    ):

        ctx = callback_context
        if not ctx.triggered:
            raise PreventUpdate

        boton = ctx.triggered[0]["prop_id"].split(".")[0]

        accion = 0
        payload = {}

        if boton == "boton-marcha":
            accion = 1
        elif boton == "boton-parada":
            accion = 2
        elif boton == "boton-emergencia":
            accion = 3
        elif boton == "boton-guardar":
            accion = 4
            payload = {
                "velocidad": vel,
                "valvula": valv,
                "friccion": fric,
                "kp": kp,
                "ki": ki,
                "kd": kd,
            }

        accion_queue.put({
            "accion": accion,
            **payload
        })

        return "ESTADOS"

    # ---------------- GRAFICO ----------------
    tiempos = []
    velocidades = []

    @app.callback(
        Output("grafico_velocidad", "figure"),
        Input("tabs", "value")
    )
    def update_graph(_):

        if data_queue.empty():
            raise PreventUpdate

        data = data_queue.get()

        tiempos.append(time.time())
        velocidades.append(data["velocidad"])

        if len(tiempos) > 50:
            tiempos.pop(0)
            velocidades.pop(0)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=tiempos,
            y=velocidades,
            mode="lines",
            line=dict(color="#1f77b4")
        ))

        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Tiempo",
            yaxis_title="Velocidad [rpm]"
        )

        return fig

    return app
