import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
import io
import base64

def update_view(app):
    @app.callback(
        [
            Output("input_info", "children"),
            Output("background_info", "children"),
            Output("store", "data"),
        ],
        {
            "fileNames":Input("input", "filename"),
            "contents":Input("input", "contents"),
            "bg_fileNames":Input("input-bg", "filename"),
            "bg_contents":Input("input-bg", "contents"),
            "peak_table":Input("peak_table", "data"),
        },
        prevent_inital_call=True,
    )
    def switch_disables(**args):
        print(args['peak_table'])
        all_data = {}

        try:
            _, content_string = args['contents'].split(',')    
            decoded = base64.b64decode(content_string)

            raw = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            raw['Type'] = "raw"
            all_data['raw'] = raw.to_json()
            res = raw.copy()
            res['Type'] = "res"
        except:
            args['fileNames'] = "no input"


        try:
            _, bg_content_string = args['bg_contents'].split(',')    
            bg_decoded = base64.b64decode(bg_content_string)
            bg = pd.read_csv(io.StringIO(bg_decoded.decode('utf-8')))
            bg['Type'] = "bg"
        except:
            args['bg_fileNames'] = "no background settings"
            # pass
        try:
            res['Stress'] -= bg['Stress']
            all_data['bg'] = bg.to_json()
        except:
            pass
        for peak in args['peak_table']:
            try:
                d = pd.DataFrame()
                d['Strain'] = raw["Strain"]
                d["Stress"] = float(peak["Amplitude"]) * np.exp(-(d["Strain"] - float(peak["Center"]))**2 / (2*float(peak["Sigma"])**2))
                d["Type"] = peak['PeakID']
                res['Stress'] -= d['Stress']
                all_data[peak['PeakID']] = d.to_json()
            except:
                print("error")
        try:
            all_data['res'] = res.to_json()
        except:
            pass
        print(args['fileNames'], args['bg_fileNames'])
        return args['fileNames'], args['bg_fileNames'], all_data

def update_view_selector(app):

    @app.callback(
        Output("plot_selector", "options"),
        Input("store", "data"),
    )
    def render_content(data):
        return list(data.keys())

def render_spectrum(app):

    @app.callback(
        Output("graph", "figure"),
        [
            Input("store", "data"),
            Input("plot_selector", "value"),
        ],
    )
    def render_graph_by_dropdown(data, key):
        if key is None:
            fig = px.scatter()
        else:
            df = pd.DataFrame()
            for k in key:
                df = df.append(pd.read_json(data[k]))
            fig = px.line(
                df,
                x="Strain",
                y="Stress",
                color="Type",
                markers=True
            )

        return fig

def add_row(app):

    @app.callback(
        Output('peak_table', 'data'),
        Input('add-rows-button', 'n_clicks'),
        State('peak_table', 'data'),
        State('peak_table', 'columns'))
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c['id']: '' for c in columns})
        return rows
