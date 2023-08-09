#################################################
#                                               #
#   Home Navbar with Dash Bootstrap Components  #
#                                               #
#################################################

# Imports
import dash
import dash_mantine_components as dmc
from dash import html, Input, Output, dcc
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, width=40, height=40, color="grey")


# Create the app
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

# Create the navbar
sidebar = html.Div(
    [   
        dcc.Location(id='url', refresh=False),
        html.Div(
            [
                dmc.Title("Energy Disagregation", order=3, color="cyan"),
            ],
            className="sidebar-header",
        ),
        dmc.Navbar(
            [
                dmc.NavLink(
                    id="analytics",
                    href="/analytics",
                    label=dmc.Title("Analytics", order=5),
                    icon=get_icon(icon="fluent:data-pie-20-regular"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="reports",
                    href="/reports",
                    label=dmc.Title("Reports", order=5),
                    icon=get_icon(icon="raphael:barchart"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="downloads",
                    href="/downloads",
                    label=dmc.Title("Downloads", order=5),
                    icon=get_icon(icon="solar:download-linear"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="settings",
                    href="/settings",
                    label=dmc.Title("Settings", order=5),
                    icon=get_icon(icon="mdi:gear"),
                    style={"margin-top": "20px"},
                    color="cyan",
                ),
                dmc.NavLink(
                    id="help",
                    href="/help",
                    label=dmc.Title("Help", order=5),
                    icon=get_icon(icon="tabler:activity"),
                    style={"margin-top": "20px"},
                    color="cyan",
                )
            ],
        ),
    ],
    className="sidebar",
)


# Create the app layout
app.layout = html.Div(
    [
        sidebar,
        html.Div(
            [
                dmc.Title("Page Content", order=1),
                dmc.Text("This is the content of the page"),
            ],
            className="content",
        ),
    ]
)

# Set as active the selected page
@app.callback(
    Output("analytics", "active"),
    Output("reports", "active"),
    Output("downloads", "active"),
    Output("settings", "active"),
    Output("help", "active"),
    Input("url", "pathname"),
)
def set_active_page(pathname):
    print("pathname:", pathname)
    if pathname == "/analytics":
        return True, False, False, False, False
    elif pathname == "/reports":
        return False, True, False, False, False
    elif pathname == "/downloads":
        return False, False, True, False, False
    elif pathname == "/settings":
        return False, False, False, True, False
    elif pathname == "/help":
        return False, False, False, False, True
    else:
        return False, False, False, False, False

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
