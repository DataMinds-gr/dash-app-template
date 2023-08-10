# Desc: Configuration file for the app

# Import required libraries
from dash import Dash
import dash_auth

# Create the app
app = Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

# Authentification
with open('.env', 'r') as file:
    content = file.read()

VALID_USERNAME_PASSWORD_PAIRS = eval(content)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)