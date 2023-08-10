######################
#                    #
#    PAGE 1: HOME    #
#                    #
######################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("Home", order=2, color="cyan"),
    ]
)