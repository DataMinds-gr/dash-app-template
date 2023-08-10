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
#     children=[
#         DashIconify(icon="iconoir:brain-research", width=40, height=40, color="grey"),
#         dmc.Text("Powered by Dataminds", color="gray", weight=300),
#         ],
#     withBorder=False,
#     position={"bottom": 0, "left": 0},
#     style={"background-color": "red"}
# )

footer = dmc.Group(
    [
        DashIconify(icon="iconoir:brain-research", width=40, height=40, color="grey"),
        dmc.Text("Powered by Dataminds",  color="gray", weight=300),
    ]  
)