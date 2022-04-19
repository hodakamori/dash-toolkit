from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_uploader as du

def before_run(args):

    invalid_message = html.P([
        html.Div(className="fas fa-times", style={"margin":"10px"}),
        "Invalid input",
        ],
        style={"textAlign":"right", "color":"#dc3545"},
    )

    valid_message = html.P([
        html.Div(className="fas fa-check", style={"margin":"10px"}),
        "Valid input!",
        ],
        style={"textAlign":"right", "color":"#28a745"},
    )
    for value in args.values():
        if value == "" or type(value) is None:
            return True, invalid_message
    
    return False, valid_message

def after_run(output_value):

    if output_value == "" or output_value is None or output_value is False:
        return True
    else:
        return False

