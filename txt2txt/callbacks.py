from dash.dependencies import Input, Output, State
from dash import dcc, html
import dash_bootstrap_components as dbc
import datetime
import pandas as pd
import logic
import validator

def download(app, download_id, button_id, file_path):

    @app.callback(
        Output(download_id, "data"),
        Input(button_id, "n_clicks"),
        prevent_inital_call=True,
    )
    def func(n_clicks):
        if n_clicks > 0:
            return dcc.send_file(
                file_path
            )

def document_modal(app):

    @app.callback(
        Output("modal-doc", "is_open"),
        Input("open-doc", "n_clicks"),
        State("modal-doc", "is_open"),
    )

    def toggle_modal(n1, is_open):
        if n1:
            return not is_open
        return is_open


def run(app, input_names):

    @app.callback(
        [
            Output("input_info", "children"),
            Output("btn-run", "n_clicks"),
            Output("output", "children"),
        ],
        [
            {input_name:Input(input_name, "value") for input_name in input_names},
            Input("btn-run", "n_clicks"),
        ],
        prevent_inital_call=True,
    )
    def validation(args, n_clicks):
        is_invalid, message = validator.before_run(args)
        if is_invalid:
            return message, 0, ""
        else:
            if n_clicks > 0:
                return message, 0, logic.main(args)
            else:
                return message, 0, ""

    @app.callback(
        Output("btn-run", "disabled"),
        {input_name:Input(input_name, "value") for input_name in input_names},
        prevent_inital_call=True,
    )
    def switch_disables(**args):
        is_invalid, _ = validator.before_run(args)
        return is_invalid

def clear(app, input_names):

    @app.callback(
        {input_name:Output(input_name, "value") for input_name in input_names},
        Input("btn-clear", "n_clicks"),
        prevent_inital_call=True,
    )
    def run(n_clicks):
        return {input_name:"" for input_name in input_names}

def result(app):

    @app.callback(
        Output("btn-result", "disabled"),
        Input("output", "children"),
        prevent_inital_call=True,
    )
    def switch_disable(output_value):
        is_invalid_result = validator.after_run(output_value)
        if is_invalid_result:
            return True
        else:
            return False
    