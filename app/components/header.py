####################
#                  #
#    Page Header   #
#                  #
####################

# Import required packages
import dash_mantine_components as dmc
from dash_iconify import DashIconify


# Create a button group with icons
single_button_with_icon = dmc.Button(
    DashIconify(icon="bx:search", color="white", width=40),
    className="header-button"
)

three_buttons_group_with_icons = dmc.ButtonGroup(
    children=[
        dmc.Button(
            DashIconify(icon="ph:bell", color="white", width=35),
            className="header-button"
        ),

        dmc.Button(
            DashIconify(icon="mdi:envelope-outline", color="white", width=35),
            className="header-button"
        ),

        dmc.Button(
            DashIconify(icon="charm:person", color="white", width=35),
            className="header-button"
        )
    ])


# Create a page header
page_header = dmc.Header(
    height=60,
    children=[
        dmc.Grid(
            [
                dmc.Col(single_button_with_icon ,span=10),
                dmc.Col(three_buttons_group_with_icons, span=2),
            ],
            gutter="xl",
        )
    ],
    className="header",
),



