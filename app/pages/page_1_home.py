######################
#                    #
#    PAGE 1: HOME    #
#                    #
######################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Import components
from components.ui_cards import complex_card
from components.ui_cards import numbers_and_rings_card

# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("Home", order=2, className="page-title"),

        dmc.Container(
            children=[
                dmc.Grid(
                    children=[
                        dmc.Col(complex_card(), span=6),
                        dmc.Col(complex_card(), span=6)
                    ],
                    gutter="md",
                    style={"margin-top": "20px"}
                )
            ]
        ),

        dmc.Center(
            children=[
                numbers_and_rings_card()
            ], style={"margin-top": "20px"}
        )
    ]
)
