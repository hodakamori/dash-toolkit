import os

import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_uploader as du

import callbacks
from common_components import jumbotron
from io_components import output_field, run_button, upload_box, download_result_button

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME])
os.makedirs('./uploads', exist_ok=True)

du.configure_upload(app, "./uploads")

#----------------------------------
app.layout = dbc.Container([
    jumbotron,
    upload_box,
    run_button,
    output_field,
    download_result_button,
    html.Hr(),
])

#----------------------------------
callbacks.download(app, "download-data", "btn-download", "./example.txt")
callbacks.document_modal(app)
callbacks.run(app)
callbacks.result(app)
callbacks.download_result(app)

app.run_server(host="0.0.0.0", debug=True)