############################
#                          # 
#   Page 6 Callbacks       #
#                          #
############################

# Load libraries
from dash import Input, Output, State
from config import app
import os
from textwrap import dedent
import openai

# Load components
from components.ui_textbox import textbox

# OpenAI Authentication
openai.api_key = os.getenv("OPENAI_API_KEY")


# System message
description = """
Philippe is the principal architect at a condo-development firm in Paris.\
He lives with his girlfriend of five years in a 2-bedroom condo, with a small dog named Coco.\
Since the pandemic, his firm has seen a  significant drop in condo requests.\
As such, he’s been spending less time designing and more time on cooking,  his favorite hobby.\
He loves to cook international foods, venturing beyond French cuisine.\
But, he is eager  to get back to architecture and combine his hobby with his occupation.\
That’s why he’s looking to create a  new design for the kitchens in the company’s current inventory. 
Can you give him advice on how to do that?
"""


@app.callback(
    Output("display-conversation", "children"), 
    Input("store-conversation", "data")
)
def update_display(chat_history):
    """
    Update the chat history display.
    """
    print("update_display", end="\n")
    return [
        textbox(x, box="user") if i % 2 == 0 else textbox(x, box="AI")
        for i, x in enumerate(chat_history.split("<split>")[:-1])
    ]


@app.callback(
    Output("user-input", "value"),
    Input("submit", "n_clicks"),
    Input("user-input", "n_submit"),
)
def clear_input(n_clicks, n_submit):
    """
    Clear the input box after the user submits a message.
    """
    print("clear_input", end="\n")
    return ""


@app.callback(
    Output("store-conversation", "data"),
    Output("loading-component", "children"),
    Input("submit", "n_clicks"),
    Input("user-input", "n_submit"),
    State("user-input", "value"),
    State("store-conversation", "data"),
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    """
    Run the chatbot and update the conversation history.
    """
    print("run_chatbot", end="\n")

    if n_clicks == 0 and n_submit is None:
        return "", None

    if user_input is None or user_input == "":
        return chat_history, None

    name = "Philippe"

    prompt = dedent(
        f"""
    {description}

    You: Hello {name}!
    {name}: Hello! Glad to be talking to you today.
    """
    )

    # First add the user input to the chat history
    chat_history += f"You: {user_input}<split>{name}:"

    model_input = prompt + chat_history.replace("<split>", "\n")

    response = openai.Completion.create(
        engine="davinci",
        prompt=model_input,
        max_tokens=250,
        stop=["You:"],
        temperature=0.9,
    )
    model_output = response.choices[0].text.strip()

    chat_history += f"{model_output}<split>"

    print("chat_history: ", chat_history)
    return chat_history, None

