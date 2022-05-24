import dash
import dash_bootstrap_components as dbc
from components.common import common_nav_bar
from components.spectrum import settings, spectrum_view, metric_view, optimize, note
from callbacks import callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME])

#----------------------------------
app.layout = dbc.Container([
    dbc.Row([common_nav_bar], className="m-2"),
    dbc.Row([
        dbc.Col([
            dbc.Row(settings, className="my-2 mx-2 border bg-white flex-grow-1")], width=3),
        dbc.Col([
            dbc.Row(spectrum_view, className="my-2 mx-1 border bg-white")], width=6),
        dbc.Col([
            dbc.Row(metric_view, className="m-2 border bg-white"),
            dbc.Row(optimize, className="my-2 mx-2 border bg-white"),
            dbc.Row(note, className="my-2 mx-2 border bg-white"),
        ], width=3),
    ])
], className="bg-light", fluid=True)

callbacks.update_view(app)
callbacks.update_view_selector(app)
callbacks.render_spectrum(app)
callbacks.add_row(app)

app.run_server(host="0.0.0.0", debug=True)