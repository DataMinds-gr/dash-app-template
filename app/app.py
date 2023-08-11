#####################################################################
#                                                                   #
# Multipage Dash App using Bootstrap Components and CSS Stylesheets #
#                                                                   #
#####################################################################

# Import the required libraries
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

# Import app
from config import app

# Import components
from components.navbar import sidebar as sidebar
from components.header import page_header as page_header
from components.footer import footer as footer

# Import pages
import pages.page_1_home as page_1_home
import pages.page_2_analytics as page_2_analytics
import pages.page_3_settings as page_3_settings
import pages.page_4_about as page_4_about
import pages.page_5_contact as page_5_contact
import pages.page_6_chat as page_6_chat
import pages.page_7_machine_learning as page_7_machine_learning
import pages.page_404_not_found as page_404_not_found

# Import callbacks
import callbacks.navbar_callbacks
# import callbacks.page_1_callbacks
import callbacks.page_2_callbacks
# import callbacks.page_3_callbacks
# import callbacks.page_4_callbacks
# import callbacks.page_5_callbacks
import callbacks.page_6_callbacks
import callbacks.page_7_callbacks


# Define the app layout
app_layout = html.Div([

    dcc.Location(id='url', refresh=False),

    sidebar,

    html.Div(page_header),

    html.Div(id='page-content', className="content"),

    html.Div(footer, "sticky-footer")

])

# Define the app theme
app.layout = dmc.MantineProvider(
    theme={
        "primaryColor": "indigo",
        "components": {
            "Header": {"styles": {"root": {
                "backgroundColor": dmc.theme.DEFAULT_COLORS.get("indigo")[6],
                "padding-top": "0.4rem",
            }}
            },
            # "Button": {"styles": {"root": {"fontWeight": 400}}},
            # "Alert": {"styles": {"title": {"fontWeight": 500}}},
            # "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=app_layout
)


# Define the app-wrapper callback
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # print(f"Pathname: {pathname}")
    if pathname == '/':
        return page_1_home.layout
    elif pathname == '/page-2-analytics':
        return page_2_analytics.layout
    elif pathname == '/page-3-settings':
        return page_3_settings.layout
    elif pathname == '/page-4-about':
        return page_4_about.layout
    elif pathname == '/page-5-contact':
        return page_5_contact.layout
    elif pathname == '/page-6-chat':
        return page_6_chat.layout
    elif pathname == '/page-7-ml':
        return page_7_machine_learning.layout
    else:
        return page_404_not_found.layout


# Run the app
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")
