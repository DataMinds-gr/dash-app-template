############################
#                          #
#    PAGE 5: CONTACT FORM  #
#                          #
############################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("Contact Form", order=2,  className="page-title"),

        dmc.Container(
            [
                dmc.Group(
                    [
                        dmc.Title("Contact Us", align="center"),
                        dmc.Text(
                            "Welcome to our Contact Us page. We are a dedicated team...",
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
            ]
        )
    ]
)
