from dash import html, dcc


def panel(children):
    return html.Div(
        children,
        style={
            "backgroundColor": "#2b2b2b",
            "color": "#e6e6e6",
            "borderRadius": "8px",
            "padding": "12px",
            "marginBottom": "12px",
            "boxShadow": "0 0 8px rgba(0,0,0,0.6)"
        }
    )


def title(text):
    return html.Div(
        text,
        style={
            "backgroundColor": "#1f77b4",
            "padding": "6px",
            "marginBottom": "10px",
            "fontWeight": "bold",
            "textAlign": "center",
            "borderRadius": "6px",
            "color": "white"
        }
    )


def value_box(label, value_id):
    return html.Div([
        html.Div(label, style={"fontSize": "12px"}),
        html.Div(
            id=value_id,
            children="0",
            style={
                "border": "1px solid #1f77b4",
                "borderRadius": "6px",
                "padding": "8px",
                "marginTop": "4px",
                "textAlign": "center",
                "backgroundColor": "#323232",
                "fontWeight": "bold"
            }
        )
    ], style={"marginBottom": "10px"})


def led(label, led_id):
    return html.Div([
        html.Div(label, style={"width": "160px"}),
        html.Div(
            id=led_id,
            style={
                "width": "28px",
                "height": "14px",
                "borderRadius": "7px",
                "backgroundColor": "#f85149"
            }
        )
    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center",
        "marginBottom": "6px"
    })


def input_row(label, input_id, unit):
    return html.Div([
        html.Div(label, style={"width": "180px"}),
        dcc.Input(
            id=input_id,
            type="number",
            style={
                "width": "120px",
                "backgroundColor": "#111",
                "color": "white"
            }
        ),
        html.Div(unit, style={"marginLeft": "10px"})
    ], style={
        "display": "flex",
        "alignItems": "center",
        "marginBottom": "8px"
    })


def boton_run(button_id):
    return html.Button(
        "RUN",
        id=button_id,
        n_clicks=0,
        style={
            "backgroundColor": "#3fb950",
            "padding": "14px 28px",
            "fontWeight": "bold",
            "borderRadius": "12px",
            "border": "none",
            "cursor": "pointer"
        }
    )


def boton_stop(button_id):
    return html.Button(
        "STOP",
        id=button_id,
        n_clicks=0,
        style={
            "backgroundColor": "#d29922",
            "padding": "14px 28px",
            "fontWeight": "bold",
            "borderRadius": "12px",
            "border": "none",
            "cursor": "pointer"
        }
    )


def boton_emergencia(button_id):
    return html.Button(
        "P.E",
        id=button_id,
        n_clicks=0,
        style={
            "backgroundColor": "#f85149",
            "color": "white",
            "padding": "18px 32px",
            "fontWeight": "bold",
            "borderRadius": "50%",
            "border": "3px solid black",
            "cursor": "pointer"
        }
    )
