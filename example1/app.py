import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_uploader as du
from dash.dependencies import Input, Output, State
import callbacks
from common_components import jumbotron
from io_components import output_field, run_clear_buttons, download_result_button, multi_inputs_field

import datetime
import pandas as pd
from logic import input_names

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME])
du.configure_upload(app, "./uploads")

#----------------------------------
app.layout = dbc.Container([
    jumbotron,
    multi_inputs_field(input_names),
    run_clear_buttons,
    output_field,
    download_result_button,
    html.Hr(),
])

#----------------------------------
callbacks.download(app, "download-data", "btn-download", "./hello.txt")
callbacks.document_modal(app)
callbacks.run(app, input_names)
callbacks.clear(app, input_names)
callbacks.download(app, "download-result", "btn-result", "./result.csv")
callbacks.result(app)

app.run_server(debug=True)