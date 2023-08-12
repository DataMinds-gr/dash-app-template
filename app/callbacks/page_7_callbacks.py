############################
#                          # 
#   Page 7 Callbacks       #
#                          #
############################

# Import required libraries
from dash import Input, Output, State
from config import app
from dash.exceptions import PreventUpdate

@app.callback( 
    Output(component_id="customer-id-input", component_property="value"),
    Output(component_id="prediction-type-radio-group", component_property="value"),
    Output(component_id="date-type-radio-group", component_property="value"),
    Output(component_id="start-date-picker", component_property="value"),
    Output(component_id="start-time-picker", component_property="value"),
    Output(component_id="end-date-picker", component_property="value"),
    Output(component_id="end-time-picker", component_property="value"),
    Output(component_id="time-interval-input", component_property="value"),
    Input(component_id="page-7-reset-button", component_property="n_clicks")   
)
def reset_prediction_container(n_clicks):
    print("Resetting the ML Prediction inputs")
    print(f"n_clicks = {n_clicks}")
    if n_clicks is None:
        raise PreventUpdate
    else:
        return [
            1000, 
            "interpolative",
            "timestamp",
            None,
            None,
            None,
            None,
            12
        ]




# Callback to generate a prediction and open the modal
@app.callback(
    # Outputs
    Output(component_id="prediction-modal", component_property="opened"),
    Output(component_id="prediction-text", component_property="children"),

    # Inputs
    Input(component_id="page-7-submit-button", component_property="n_clicks"),
    Input(component_id="prediction-modal-close-button", component_property="n_clicks"),

    # Modal State
    State("prediction-modal", "opened"),
    
    # Machine Learning Model Inputs
    State(component_id="customer-id-input", component_property="value"),
    State(component_id="prediction-type-radio-group", component_property="value"),
    State(component_id="date-type-radio-group", component_property="value"),
    State(component_id="start-date-picker", component_property="value"),
    State(component_id="start-time-picker", component_property="value"),
    State(component_id="end-date-picker", component_property="value"),
    State(component_id="end-time-picker", component_property="value"),
    State(component_id="time-interval-input", component_property="value"),
    prevent_initial_call=True,
)
def generate_prediction(
    n_clicks_submit_button,
    n_clicks_prediction_modal_close_button,
    prediction_modal_opened,
    customer_id_input,
    prediction_type_radio_group,
    date_type_radio_group,
    start_date,
    start_time,
    end_date,
    end_time,
    time_interval
):
    print("Generating a prediction")
    
    print("===== Parameters =====")
    print("customer_id_input: ", customer_id_input)
    print("prediction_type_radio_group: ", prediction_type_radio_group)
    print("date_type_radio_group: ", date_type_radio_group)
    print("start_date: ", start_date)
    print("start_time: ", start_time)
    print("end_date: ", end_date)
    print("end_time: ", end_time)
    print("time_interval: ", time_interval)
    print("======================")

    if prediction_type_radio_group == "interpolative" and date_type_radio_group == "timestamp":
        prediction = "Class A" 
    elif prediction_type_radio_group == "interpolative" and date_type_radio_group == "datetime_range":
        prediction = "Class B"
    elif prediction_type_radio_group == "extrapolative" and date_type_radio_group == "timestamp":
        prediction = "Class C"
    elif prediction_type_radio_group == "extrapolative" and date_type_radio_group == "datetime_range":
        prediction = "Class D"
    else:
        prediction = "No Prediction"

    return not prediction_modal_opened, prediction


@app.callback(
    Output(component_id="page7-output-1", component_property="children"),
    Input(component_id="page7-button-1", component_property="n_clicks"),
)
def button_press(n_clicks):
    print("Button pressed callback page 7", end="\n")
    if n_clicks == 0:
        return "Button pressed 0 times"
    else:
        return f"Button pressed {n_clicks} times"