##########################
#                        #
#    PAGE 3: SETTINGS    #
#                        #
##########################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc
from components.ui_tables import dash_mantine_react_table

# Import data
import plotly.express as px
data = px.data.gapminder()


# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("Settings", order=2),

        html.Div(
            [
                dash_mantine_react_table(data)
            ], style={"margin-left": "20px", "margin-right": "20px"}
        )
    ]
)