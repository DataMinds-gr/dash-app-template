from dash import Dash
import dash_bootstrap_components as dbc
import dash_auth

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True

with open('.env', 'r') as file:
    content = file.read()

VALID_USERNAME_PASSWORD_PAIRS = eval(content)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)