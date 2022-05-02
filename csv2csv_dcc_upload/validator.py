import os
import io
import base64
import pandas as pd
from dash import html

def invalid_message(message):
    invalid_message = html.P([
        html.Div(className="fas fa-times", style={"margin":"10px"}),
        message,
        ],
        style={"textAlign":"right", "color":"#dc3545"},
    )

    return invalid_message

def valid_message(message):
    valid_message = html.P([
        html.Div(className="fas fa-check", style={"margin":"10px"}),
        message,
        ],
        style={"textAlign":"right", "color":"#28a745"},
    )

    return valid_message

def before_run(args):

    for key, value in args.items():
        if value == "" or value is None:
            message = "ERROR: No input was found."
            return True, invalid_message(message)

    if not args['fileNames'].endswith('.csv'):
        message = f"ERROR: {args['fileNames']} is invalid file. Only CSV file is valid"
        return True, invalid_message(message)

    _, content_string = args['contents'].split(',')    
    decoded = base64.b64decode(content_string)
    
    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        message = f"INFO: {args['fileNames']} is valid file."
        print(df)
        return False, valid_message(message)

    except Exception as e:
        print(e)
        message = f"ERROR: {args['fileNames']} has an error processing this file. {e}"
        return True, invalid_message(message)

def after_run(output_value):
    if os.path.isfile(output_value):
        return False
    else:
        return True

