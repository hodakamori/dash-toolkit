from dash import dcc, html
import dash_bootstrap_components as dbc

import json

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
with open("appinfo.json") as fi:
    appinfo = json.load(fi)

with open("instruction.md") as gi:
    instruction = gi.readlines()

def transparent_button_with_icon(button_id, icon, text):

    button = html.Button(html.Div([
        html.Div(className=icon, style={"margin":"10px"}),
        text
        ]),
        style={
            "background-color":"transparent",
            "border":"none",
        },
        id=button_id,
        n_clicks=0,
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
        dbc.Button("Instruction", id="open-doc", className="me-1 d-md-block", n_clicks=0),
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

common_nav_bar =  dbc.Navbar(
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                dbc.Col(dbc.NavbarBrand("My Awesome App", className="ms-2")),
            ],
            align="center",
            className="g-2",
        ),
        dbc.Row(document_button, className="ms-auto"),
        dbc.Row(mail_button),
        dbc.Row(code_button),
        dbc.Row(user_button),
        ],
        fluid=True,
    ),
)