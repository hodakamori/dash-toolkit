import os

from dash import html

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
        if value == "" or value is None:
            return True, invalid_message
    
    return False, valid_message

def after_run(output_value):
    if os.path.isfile(output_value):
        return False
    else:
        return True

