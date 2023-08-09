#####################################################################
#                                                                   #
# Multipage Dash App using Bootstrap Components and CSS Stylesheets #
#                                                                   #
#####################################################################

# Import the required libraries
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Import app
from app.config import app

# Import pages
from components.navbar import navbar as navbar
from components.footer import footer as footer
import pages.page_1_home as page_1_home
import pages.page_2_localization as page_2_localization
import pages.page_3_map as page_3_map
import pages.page_4_network as page_4_network
import pages.page_5_alerts as page_5_alerts
import pages.page_6_growth as page_6_growth
import pages.page_7_about as page_7_about
import pages.page_404_not_found as page_404_not_found
       
# Import callbacks
import callbacks.navbar_callbacks
import callbacks.map_callbacks
import callbacks.simple_callback

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', className="main-content"),
    footer
], className="app-wrapper")

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # print(f"Pathname: {pathname}")
    if pathname == '/':
        return page_1_home.layout
    elif pathname == '/page-2-localization':
        return page_2_localization.layout
    elif pathname == '/page-3-map':
        return page_3_map.layout
    elif pathname == '/page-4-network':
        return page_4_network.layout
    elif pathname == '/page-5-alerts':
        return page_5_alerts.layout
    elif pathname == '/page-6-growth':
        return page_6_growth.layout
    elif pathname == '/page-7-about':
        return page_7_about.layout
    else:
        return page_404_not_found.layout


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")