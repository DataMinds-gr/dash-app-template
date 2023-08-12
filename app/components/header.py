####################
#                  #
#    Page Header   #
#                  #
####################

# Import required packages
import dash_mantine_components as dmc
from dash_iconify import DashIconify


# Create app logo element
app_logo = dmc.Image(src="/assets/LOGO-removebg.png", alt="logo", width=200, height="3.5rem")

three_buttons_group_with_icons = dmc.ButtonGroup(
    children=[
        dmc.Button(
            DashIconify(icon="ph:bell", width=25, height=25),
        ),

        dmc.Button(
            DashIconify(icon="mdi:envelope-outline", width=25, height=25),
        ),

        dmc.Button(
            DashIconify(icon="charm:person", width=25, height=25),
        )
    ])


# Create a page header
page_header = dmc.Header(
    height="3.5rem",
    children=[
        dmc.Grid(
            [
                dmc.Col(app_logo,span=10),
                dmc.Col(three_buttons_group_with_icons, span=2),
            ],
            gutter="xl",
        )
    ],
    fixed=True,
),



