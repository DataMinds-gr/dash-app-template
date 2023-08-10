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
        dmc.Title("Page Not Found", order=2, color="cyan"),
    ]
)