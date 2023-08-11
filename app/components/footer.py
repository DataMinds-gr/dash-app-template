##############
#            #
#   Footer   #
#            #
##############

# Import packages
from dash import html
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

text_with_icon = dmc.Group(
    [
        DashIconify(icon="iconoir:brain-research",
                    width=25, height=25, color="grey"),
        dmc.Text("Powered by Dataminds",  color="gray", weight=300),
    ]
)

footer_links = dmc.Group(
            [
                dmc.Anchor("About", href="/about", underline=False),
                dmc.Anchor("Contact", href="/about", underline=False),
                dmc.Anchor("Privacy", href="/about", underline=False),
            ]
        )

footer = html.Div(
    [
        dmc.Grid(
            [
                dmc.Col(text_with_icon, span=10),
                dmc.Col(footer_links, span=2),
            ]
        )
    ], style={"margin-left": "4rem"}
)
