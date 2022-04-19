from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_uploader as du

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
    className="d-grid gap-2 col-6 mx-auto",
)

output_field = html.Div([
    html.Hr(),
    html.P("Output:"),
    html.P(id='output_info'),
    html.P(id='output')
])

upload_box = dbc.Container([
    html.Hr(),
    html.H4("Upload with Dash-uploader"),
    du.Upload(
        id='input',
        max_file_size=1800,
        filetypes=['csv'],
        max_files=1,
        cancel_button=True,
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
