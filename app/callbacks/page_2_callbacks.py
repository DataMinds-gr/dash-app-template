# Import libraries
from dash import Input, Output
from config import app

@app.callback(
    Output("date_range_picker", "style"),
    Input("segment_control", "value")
)
def show_date_range_picker(value):
    if value == "Custom":
        return {"display": "block"}
    else:
        return {"display": "none"}