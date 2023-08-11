###############################
#                             #
#    Design UI  Textbox       #
#                             #
###############################

# Import libraries
import dash_mantine_components as dmc
from dash import html

def textbox(text, box="AI", name="Philippe"):
    text = text.replace(f"{name}:", "").replace("You:", "")
    
    style = {
        "max-width": "60%",
        "width": "max-content",
        "padding": "5px 10px",
        "border-radius": 25,
        "margin-bottom": 20,
    }

    if box == "user":
        style["margin-left"] = "auto"
        style["margin-right"] = 0

        return dmc.Card(text, style=style)

    elif box == "AI":
        style["margin-left"] = 0
        style["margin-right"] = "auto"

        thumbnail = html.Img(
            src="/assets/robot.jpg",
            style={
                "border-radius": 50,
                "height": 36,
                "margin-right": 5,
                "float": "left",
            },
        )
        textbox = dmc.Card(text, style=style)
        
        print("==== TEXTBOX ====")
        print(textbox)

        return html.Div([thumbnail, textbox])
    else:
        raise ValueError("Incorrect option for `box`.")