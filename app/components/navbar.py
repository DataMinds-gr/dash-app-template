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
    return DashIconify(icon=icon, width=40, height=40, color="grey")

# Create the navbar
sidebar = html.Div(
    [   
        html.Div(
            [
                dmc.Title("Energy Disagregation", order=3, color="cyan"),
            ],
            className="sidebar-header",
        ),
        dmc.Navbar(
            [
                dmc.NavLink(
                    id="home",
                    href="/",
                    label=dmc.Title("Home", order=5),
                    icon=get_icon(icon="tabler:activity"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="analytics",
                    href="/page-2-analytics",
                    label=dmc.Title("Analytics", order=5),
                    icon=get_icon(icon="fluent:data-pie-20-regular"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="settings",
                    href="/page-3-settings",
                    label=dmc.Title("Settings", order=5),
                    icon=get_icon(icon="raphael:barchart"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="about",
                    href="/page-4-about",
                    label=dmc.Title("About", order=5),
                    icon=get_icon(icon="solar:download-linear"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="contact",
                    href="/page-5-contact",
                    label=dmc.Title("Contact", order=5),
                    icon=get_icon(icon="mdi:gear"),
                    style={"margin-top": "20px"},
                    color="cyan",
                )
            ],
        ),
    ],
    className="sidebar",
)
