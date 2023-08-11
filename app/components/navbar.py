##############
#            #
#   Navbar   #
#            #
##############

# Imports
import dash
import dash_mantine_components as dmc
from dash import html, Input, Output, dcc
from dash_iconify import DashIconify


def get_icon(icon):
    """Returns a DashIconify component with the specified icon."""
    return DashIconify(icon=icon, width=25, height=25, color="grey")


# Create the navbar
sidebar = html.Div(
    [
        
        dmc.Navbar(
            [
                dmc.NavLink(
                    id="home",
                    href="/",
                    label=dmc.Title("Home", order=5),
                    icon=get_icon(icon="carbon:home"),
                    style={"margin-top": "0.5rem"},
                ),
                dmc.NavLink(
                    id="analytics",
                    href="/page-2-analytics",
                    label=dmc.Title("Analytics", order=5),
                    icon=get_icon(icon="fluent:data-pie-20-regular"),
                    style={"margin-top": "0.5rem"},
                ),
                dmc.NavLink(
                    id="settings",
                    href="/page-3-settings",
                    label=dmc.Title("Settings", order=5),
                    icon=get_icon(icon="mdi:gear"),
                    style={"margin-top": "0.5rem"},
                ),
                dmc.NavLink(
                    id="about",
                    href="/page-4-about",
                    label=dmc.Title("About", order=5),
                    icon=get_icon(icon="mdi:about-circle-outline"),
                    style={"margin-top": "0.5rem"},
                ),
                dmc.NavLink(
                    id="contact",
                    href="/page-5-contact",
                    label=dmc.Title("Contact", order=5),
                    icon=get_icon(icon="ic:outline-email"),
                    style={"margin-top": "0.5rem"}
                )
            ],
        ),
        dmc.Space(h="20rem"),
        html.Div(
            [
                dmc.Card(
                    [
                        dmc.Group(
                            [
                                DashIconify(icon="iconoir:brain-research",
                                            width=20, height=20, color="grey"),
                                dmc.Container(
                                    [
                                        dmc.Title(
                                            "Panos Papaemmanouil", order=4),
                                        dmc.Title("Data Scientist", order=6),
                                        dmc.Text("panos@dataminds.gr",
                                                 color="gray"),
                                    ]
                                )
                            ]
                        )
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                )
            ],
            className="sidebar-header",
        ),
    ],
    className="sidebar",
)
