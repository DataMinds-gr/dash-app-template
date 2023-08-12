############################
#                          # 
#   Page 3 Callbacks       #
#                          #
############################

print("Importing page_3_callbacks.py")

# Import libraries
from config import app
from dash import Input, Output, State

@app.callback(
    Output("page3-button-clicks", "children"),
    Input("page3-button", "n_clicks"),
)
def on_button_click(n):
    if n is None:
        return "Button clicked 0 times"
    else:
        return f"Button clicked {n} times"
