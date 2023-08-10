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
                dmc.Title("About Us", align="center"),


                dmc.Grid(
                    [
                        dmc.Col(
                            dmc.Text("Welcome to our About Us page. We are a dedicated team"
                                     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod..."
                                     "If you want to learn more about our services and expertise, "
                                     "feel free to contact us using the form below.",
                                     align="center", size="lg", mt=20, mb=20),
                            span=6
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/team.jpg",
                                      alt="Team Image", fit="contain", m=20),
                            span=6
                        ),

                    ]

                ),

                dmc.Divider(variant="solid"),

                dmc.Title("Team", m=20, align="center"),

                dmc.Grid(
                    [
                        dmc.Col(
                            dmc.Image(src="/assets/person1.jpg",
                                      alt="Person 1", fit="contain", radius=300, width="80%"),
                            span=4, 
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/person2.jpg",
                                      alt="Person 2", fit="contain", radius=300, width="80%"),
                            span=4,  
                        ),
                        dmc.Col(
                            dmc.Image(src="/assets/person3.jpg",
                                      alt="Person 3", fit="contain", radius=300, width="80%"),
                            span=4,
                        )
                    ], m=20
                )
            ]
        )
    ]
)
