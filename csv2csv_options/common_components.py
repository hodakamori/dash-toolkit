from dash import dcc, html
import dash_bootstrap_components as dbc
import datetime

import json


with open("appinfo.json") as fi:
    appinfo = json.load(fi)

with open("instruction.md") as gi:
    instruction = gi.readlines()

def transparent_button_with_icon(button_id, icon, text):

    button = html.Button([
        html.Div(className=icon, style={"margin":"10px"}),
        text
        ],
        style={
            "background-color":"transparent",
            "border":"none",
        },
        id=button_id,
        n_clicks=0
    )
    return button


mail_button = html.A(
    transparent_button_with_icon("btn-mail", "fas fa-envelope", "Contact"),
    href=f"mailto:{appinfo['email']}",
)

example_button = html.Div([
    transparent_button_with_icon("btn-download", "fas fa-arrow-alt-circle-down", "Example"),
    dcc.Download(id="download-data")
])

code_button = html.A(
    transparent_button_with_icon("btn-clock", "fas fa-code", "Code"),
    href='https://github.com/hodakamori/dash-toolkit.git',
    target="_blank"
)

user_button = html.Div([
    transparent_button_with_icon("btn-user", "fas fa-user", "user"),
    dbc.Popover(
        dbc.PopoverBody("Hi! I am developper."),
        trigger="click",
        target="btn-user",
    )
])


document_button = html.Div(
    [
        dbc.Button("Instruction", id="open-doc", className="me-1", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Instruction")),
                dbc.ModalBody(dcc.Markdown(instruction)),
            ],
            id="modal-doc",
            size="xl",
            is_open=False,
            scrollable=True
        ),
    ])

common_buttons = dbc.Row([
    dbc.Col(document_button, width=2),
    dbc.Col(mail_button, width={"size":2, "offset":2}),
    dbc.Col(example_button, width=2),
    dbc.Col(code_button, width=2),
    dbc.Col(user_button, width=2)
    ],
    justify="end")

jumbotron = dbc.Col(
    html.Div(
        [
            html.H4(appinfo['title'], className="display-7"),
            html.Hr(className="my-2"),
            html.P(appinfo["description"]),
            common_buttons,
        ],
        className="h-60 p-4 bg-light",
    ),
)

