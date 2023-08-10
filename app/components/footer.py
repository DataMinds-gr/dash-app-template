##############
#            #
#   Footer   #
#            #
##############

# Import packages
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# footer = dmc.Footer(
#     height=60,
#     position={"bottom": 1000, "left": 100, "right": 50},
#     children=[
#         DashIconify(icon="iconoir:brain-research", width=40, height=40, color="grey"),
#         dmc.Text("Powered by Dataminds",  color="gray", weight=300),
#         ]
# )

footer = dmc.Group(
    [
        DashIconify(icon="iconoir:brain-research", width=40, height=40, color="grey"),
        dmc.Text("Powered by Dataminds",  color="gray", weight=300),
    ]  
)