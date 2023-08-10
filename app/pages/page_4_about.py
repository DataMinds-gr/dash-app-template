#######################
#                     #
#    PAGE 4: ABOUT    #
#                     #
#######################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("About", order=2,  className="page-title"),

        dmc.Container(
            [

                dmc.Text(
                    [
                        dmc.Title("About Us", align="center"),
                        dmc.Text(
                            "Welcome to our About Us page. We are a dedicated team...",
                            align="center"
                        ),
                        dmc.Text(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod...",
                            align="center"
                        ),
                        dmc.Text(
                            "If you want to learn more about our services and expertise, "
                            "feel free to contact us using the form below.",
                            align="center"
                        ),
                    ],
                ),

                dmc.Grid(
                    [
                        dmc.Col(
                            dmc.Image(src="/assets/team.jpg",
                                      alt="Team Image", fit="contain"),
                            span=6,
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/person1.jpg",
                                      alt="Person 1", fit="contain"),
                            span=2,
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/person2.jpg",
                                      alt="Person 2", fit="contain"),
                            span=2,
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/person3.jpg",
                                      alt="Person 3", fit="contain"),
                            span=2,
                        ),
                    ],
                )
            ]
        )
    ]
)
