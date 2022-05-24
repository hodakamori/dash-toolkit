from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import html, dash_table
import pandas as pd
import numpy as np

split_spectrum = pd.DataFrame(np.full((1, 6), np.nan), columns=["PeakID", "Center", "Sigma", "Amplitude", "Area", "Assign"])

settings = [
    html.H5("Settings:", className="my-2"),
    html.H5("1. Upload file to analyze: "),
    dcc.Upload([
        'Drag and Drop',
        ],
        style={
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'height': '50px',
        },
        id='input',
    ),
    html.P(),
    html.H6("Loaded file is:"),
    html.P(id='input_info'),
    html.Hr(),
    html.H5("2. Background correction:"),
    dbc.RadioItems(
        options=[
            {"label": "Auto-correction", "value": "auto-correction", "disabled": True},
            {"label": "Load from file", "value": "from-file"},
        ],
        value="from-file",
        id="bgcorrection-method",
    ),
    html.Br(),
    dcc.Upload([
        'Drag and Drop',
        ],
        style={
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'height': '50px'
        },
        id='input-bg',
    ),
    html.P(),
    html.H6("Loaded file is:"),
    html.P(id='background_info'),
    dbc.Button("Auto correction", id="btn-correct-bg", className="d-grid col-6 mx-auto", disabled=True),
    html.P(id='background_info_2'),
    html.Hr(),
    html.H5("3. Find peak(s):"),
    dbc.RadioItems(
        options=[
            {"label": "Gaussian", "value": "gaussian"},
            {"label": "Lorentian", "value": "lolentian", "disabled": True},
            {"label": "Customized", "value": "customized", "disabled": True},
        ],
        value="gaussian",
        id="basis-function",
    ),
    html.Br(),
    dbc.Button("Find peak(s)", id="btn-auto-peak-find", className="d-grid gap-2 col-6 mx-auto", disabled=True),
    html.P(id='peak-find-info'),
    html.Br(),
]

spectrum_view = [
    html.H5("Spectrum:", className="my-2"),
    dcc.Store(id="store"),
    dbc.Container([
            dcc.Dropdown(
                [],
                multi=True,
                id="plot_selector",
                className="m-2"
            ),
            dcc.Graph(
                id='graph',
                animate=True,
            )
        ]),
    html.H5("Peak detail(s):", className="my-2"),
    dash_table.DataTable(
        split_spectrum.to_dict('records'),
        [{"name": i, "id": i} for i in split_spectrum.columns],
        style_table={'overflow': 'hidden',},
        style_cell_conditional=[
            {
                'if': {'column_id': 'PeakID'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'Center'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'Sigma'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'Amplitude'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'Area'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'Assign'},
                'width': '100px'
            },
        ],
        fixed_rows={'headers': True},
        page_size=5,
        editable=True,
        row_deletable=True,
        id="peak_table",
    ),
    dbc.Button('Add Peak', id='add-rows-button', className="m-2", n_clicks=0, style={'width': "200px",}), 
]

metric_view = [
    html.H5("Fitting metrics:", className="my-2"),
    dbc.ListGroup(
        [
            dbc.ListGroupItem("MAE:"),
            dbc.ListGroupItem("RMSE"),
            dbc.ListGroupItem("Max Error"),
        ],
        flush=True,
        className="ms-auto", style={"width":"95%"}
    ),
]

optimize = [
    html.H5("Optimize:", className="my-2"),
    dbc.Label("Method:"),
    dbc.RadioItems(
        options=[
            {"label": "BFGS", "value": "bfgs", "disabled": True},
            {"label": "Bayesian", "value": "bayesian", "disabled": True},
        ],
        id="optimize-method",
    ),
    dbc.Label("Target:"),
    dbc.RadioItems(
        options=[
            {"label": "MAE", "value": "mae", "disabled": True},
            {"label": "RMSE", "value": "rmse", "disabled": True},
        ],
        id="optimize-target",
    ),
    dbc.Button("Optimize peak(s)", id="btn-optimize-peak", className="d-grid gap-2 col-6 mx-auto", disabled=True),
    html.P(),
]

note = [
    html.H5("Note:", className="my-2"),
    dbc.Textarea(placeholder="A Textarea", style={'width': "95%", "height": "200px"}, className="m-auto"),
    html.P(),
]