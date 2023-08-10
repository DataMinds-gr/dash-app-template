# Import libraries
from config import app
from dash import Input, Output

# Set as active the selected page
@app.callback(
    Output("home", "active"),
    Output("analytics", "active"),
    Output("settings", "active"),
    Output("about", "active"),
    Output("contact", "active"),
    Input("url", "pathname"),
)
def set_active_page(pathname):
    if pathname == "/":
        return True, False, False, False, False
    elif pathname == "/page-2-analytics":
        return False, True, False, False, False
    elif pathname == "/page-3-settings":
        return False, False, True, False, False
    elif pathname == "/page-4-about":
        return False, False, False, True, False
    elif pathname == "/page-5-contact":
        return False, False, False, False, True
    else:
        return False, False, False, False, False