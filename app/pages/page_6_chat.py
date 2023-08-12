############################
#                          #
#    PAGE 6: CHAT APP      #
#                          #
############################

# Import libraries
from dash import dcc, html, Input, Output, State
import dash_mantine_components as dmc

# Load components (temp)
from components.ui_textbox import textbox

app_header = dmc.Container(
    [
        dmc.Image(src="/assets/chatbot.jpg", height=80, width="100%"),
        dmc.Title("Dash GPT Chatbot", order=1, align="center"),
    ]
)


# Define Layout
conversation = html.Div(
    [
        html.Div(id="display-conversation"),
    ], style={
        "overflow-y": "auto",
        "display": "flex",
        "height": "calc(90vh - 190px)",
        "flex-direction": "column-reverse",
    }
)

controls = dmc.Grid(
    [
        dmc.Col(
            dmc.TextInput(id="user-input", placeholder="Write to the chatbot..."),
            span=8, offset=2
        ),
        dmc.Col(
            dmc.Button("Submit", id="submit"),
            span=2
        )
    ],
)


# Define the page layout
# ------------------------
layout = html.Div(
    [
        app_header,
        conversation,
        html.Div(
            [
                textbox("Hello Panos!", box="AI", name="Philippe"),
                textbox("Hello Philippe!", box="user", name="Panos")
            ]
        ),
        controls,
        dmc.Loader(id="loading-component"),
    ],  style = {"padding-bottom": "20px"}
)
