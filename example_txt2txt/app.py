import dash
import dash_bootstrap_components as dbc
from dash import html
import dash_uploader as du

import callbacks
from common_components import jumbotron
from io_components import output_field, run_clear_buttons, multi_inputs_field
from logic import input_names

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME])
du.configure_upload(app, "./uploads")

#----------------------------------
app.layout = dbc.Container([
    jumbotron,
    multi_inputs_field(input_names),
    run_clear_buttons,
    output_field,
    html.Hr(),
])

#----------------------------------
callbacks.download(app, "download-data", "btn-download", "./example.txt")
callbacks.document_modal(app)
callbacks.run(app, input_names)
callbacks.clear(app, input_names)

app.run_server(debug=True)