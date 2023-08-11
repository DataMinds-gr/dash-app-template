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

        dmc.Container(
            [
                dmc.Text("404", style={"fontWeight": 900,
                                       "color": "lightgrey",
                                       "fontSize": "20rem"}),

                dmc.Title("You have found a secret place.", order=1),

                dmc.Space(h="1rem"),

                dmc.Text(
                    "Unfortunately, this is only a 404 page. You may have mistyped the address, or the page has been moved to another URL.",
                    color = "grey",
                    weight=500,
                ),

                dmc.Center(
                    dmc.Button(
                        dmc.Anchor("Go back to the homepage",
                                   href="/", underline=False),
                        variant="subtle",
                        size="md",
                        style={"margin-top": "2rem"}
                    )
                )

            ],
            ta="center",
            size="sm"
        )
    ],
)
