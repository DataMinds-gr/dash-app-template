###################################
#                                 #
#   ERROR 404 - PAGE NOT FOUND    #
#                                 #
###################################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title(
            "You have found a secret place.",
            order=5),
        
        dmc.Text(
            "Unfortunately, this is only a 404 page. You may have mistyped the address, or the page has been moved to another URL.",
        ),
    ], style={"padding-top": "80rem", "padding-bottom": "80rem"}
)
