from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_uploader as du
from logic import wait_time

max_intervals = 10

run_button = html.Div(
    [
        dbc.Button("Run", id="btn-run", n_clicks=0, color="primary"),
    ],
    className="d-grid gap-2",
)

clear_button = html.Div(
    [
        dbc.Button("Clear", id="btn-clear", n_clicks=0, color="secondary"),
    ],
    className="d-grid gap-2",
)

download_result_button = html.Div(
    [
        dbc.Button(html.Span(["Result", html.Div(className="fas fa-download", style={"margin":"10px"})]), id="btn-result", n_clicks=0, color="primary"),
        dcc.Download(id="download-result")
    ],
    className="d-grid gap-2",
)

output_field = html.Div([
    html.Hr(),
    html.P("Output:"),
    html.Br(),
    dcc.Interval(id="progress-interval", n_intervals=0, interval=wait_time/max_intervals*1000, max_intervals=max_intervals, disabled=True),
    dbc.Progress(id="progress", striped=True, className="d-grid gap-2"),
    html.Br(),
    html.P(id='output_info'),
    html.P(id='output')
])

upload_box = dbc.Container([
    html.Hr(),
    html.H4("Upload with Dash-uploader"),
    dcc.Upload([
        'Drag and Drop or ',
        html.A('Select a File')
        ],
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center'
        },
        id='input',
    ),
    html.P(id='input_info'),
    html.Br(),
])

run_clear_buttons = dbc.Row([
    dbc.Col(run_button, width=2),
    dbc.Col(clear_button, width=2)
    ],
    justify="end"
    )
