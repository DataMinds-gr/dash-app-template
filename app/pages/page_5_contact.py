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
        dmc.Title("Get in touch", order=1, align="center"),

        dmc.Text("If you have any questions or comments, "
                 "please fill out the form below and we will get back to you as soon as possible.",
                 size="md", align="center", mb=20),

        dmc.Container(
            children=[
                dmc.SimpleGrid(
                    cols=2,
                    breakpoints=[
                        {"maxWidth": "sm", "cols": 1},
                    ],
                    children=[
                        dmc.TextInput(
                            label="Name", placeholder="Your name", variant="filled"),
                        dmc.TextInput(
                            label="Email", placeholder="Your email", variant="filled")
                    ], mt="xl"
                ),


                dmc.TextInput(label="Subject", placeholder="Subject",
                              mt="md", variant="filled"),

                dmc.Textarea(
                    label="Message",
                    placeholder="Your messages...",
                    autosize=True,
                    minRows=5,
                    maxRows=10,
                    variant="filled",
                    mt="md"
                ),

                dmc.Center(
                    dmc.Button("Submit",
                               variant="gradient",
                               gradient={"from": "indigo", "to": "cyan"},
                               size="md",
                               mt="xl"),
                )
            ]
        )
    ], style = {"height":"90vh"}
)
