from dash.dependencies import Input, Output, State
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
    transparent_button_with_icon("btn-mail", "far fa-envelope", "Contact"),
    href=f"mailto:{appinfo['email']}",
)

download_button = html.Div([
    transparent_button_with_icon("btn-download", "far fa-arrow-alt-circle-down", "Download"),
    dcc.Download(id="download-data")
])

clock_button = html.Div([
    transparent_button_with_icon("btn-clock", "far fa-clock", "Clock"),
    dbc.Tooltip(
        datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),
        target="btn-clock",
        placement="bottom",
    )
])

user_button = html.Div([
    transparent_button_with_icon("btn-user", "far fa-user", "user"),
    dbc.Popover(
        dbc.PopoverBody("Hi! I am user."),
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
    dbc.Col(download_button, width=2),
    dbc.Col(clock_button, width=2),
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

