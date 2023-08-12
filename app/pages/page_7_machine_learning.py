##################################
#                                #
#    PAGE 6: MACHINE LEARNING    #
#                                #
##################################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import date

# Import components
from components.ui_modal import modal

# Generate Apps Header
header = html.Div([
    dmc.Container(
        children=[
            dmc.Text(
                "Machine Learning App",
                size=36,
                weight=700,
                align="center",
                color="indigo",
            ),
            dmc.Text(
                "Generate Predictions",
                size="md",
                align="center",
                color="gray"
            ),
        ]
    )
])


# Create a Tooltip component
tooltip_icon = DashIconify(icon="ph:question-light")

tooltip = dmc.Tooltip(
    label="Enter the Prediction Parameters to generate a prediction",
    position="top",
    children=tooltip_icon,
    color="gray",
)

# Create a Divider component
text_divider = dmc.Divider(
    label=dmc.Text("Prediction Parameters", color="gray", size="lg"),
    labelPosition="center",
    orientation="horizontal",
    size="md",
)

text_divider_and_tooltip = dmc.Grid(
    children=[
        dmc.Col(text_divider, span=11),
        dmc.Col(tooltip, span=1)
    ]
)

# Create a NumberInput component
customer_id_input = dmc.NumberInput(
    id="customer-id-input",
    label=dmc.Text(f"Customer ID", color="gray", size="sm"),
    icon=DashIconify(icon="material-symbols:person", color="gray", height=20, width=20),
    value=1_000,
    min=1_000,
    max=10_000,
    step=1,
    required=True,
    withAsterisk=False,
    style={"width": 250, "margin-top": 20},
)


# Prediction Type radio group
prediction_type_data = [
    ["interpolative", "Interpolative"],
    ["extrapolative", "Extrapolative"]
]

prediction_type_radio_group = dmc.RadioGroup(
    [dmc.Radio(l, value=k, color="green") for k, l in prediction_type_data],
    id="prediction-type-radio-group",
    value="interpolative",
    label=dmc.Text("Prediction Type:", color="gray", size="sm"),
    size="sm",
    style={"margin-top": 20},
)

# Date Type radio group
date_type_data = [
    ["datetime_range", "Datetime Range"],
    ["timestamp", "Timestamp"]
]

date_type_radio_group = dmc.RadioGroup(
    [dmc.Radio(l, value=k, color="green") for k, l in date_type_data],
    id="date-type-radio-group",
    value="timestamp",
    label=dmc.Text("Date Type:", color="gray", size="sm"),
    size="sm",
    style={"margin-top": 20},
)

# Start Datetime Picker component
start_date_picker = dmc.DatePicker(
    id="start-date-picker",
    label=dmc.Text("Start Datetime:", color="gray", size="sm"),
    minDate=date(2022, 1, 1),
    maxDate=date(2023, 12, 31),
    amountOfMonths=1,
    dropdownPosition="bottom",
    required=True,
    withAsterisk=False,
    icon=DashIconify(icon="mdi:calendar-outline", color="gray", height=20, width=20),
)

start_time_picker = dmc.TimeInput(
    id="start-time-picker",
    label=dmc.Text("", size="sm"),
    required=True,
    withAsterisk=False,
    icon=DashIconify(icon="ph:clock", color="gray", height=20, width=20),
)

# Combine the Date and Time Pickers
start_datetime_picker = dmc.Grid(
    children=[
        dmc.Col(start_date_picker, span=6),
        dmc.Col(start_time_picker, span=6),
    ],
    style={"margin-top": 20},
)

# End Datetime Picker component
end_date_picker = dmc.DatePicker(
    id="end-date-picker",
    label=dmc.Text("End Datetime:", color="gray", size="sm"),
    minDate=date(2022, 1, 1),
    maxDate=date(2023, 12, 31),
    amountOfMonths=1,
    dropdownPosition="bottom",
    required=True,
    withAsterisk=False,
    icon=DashIconify(icon="mdi:calendar-outline", color="gray", height=20, width=20),
)

end_time_picker = dmc.TimeInput(
    id="end-time-picker",
    label=dmc.Text("", size="sm"),
    required=True,
    withAsterisk=False,
    icon=DashIconify(icon="ph:clock", color="gray", height=20, width=20),
)

# Combine the Date and Time Pickers
end_datetime_picker = dmc.Grid(
    children=[
        dmc.Col(end_date_picker, span=6),
        dmc.Col(end_time_picker, span=6),
    ],
    style={"margin-top": 20},
)

# Create a Time Interval component
time_interval_input = dmc.NumberInput(
    id="time-interval-input",
    label=dmc.Text("Time Interval (hours)", color="gray", size="sm"),
    value=12,
    min=1,
    max=24,
    step=1,
    required=True,
    withAsterisk=False,
    style={"width": 250, "margin-top": 20},
)

# Create a style dictionary
main_container_style = {
    "height": 600,
    "width": 500,
    "border": "1px solid indigo",
    "margin-top": 25,
    "padding": 40,
    "border-radius": 10,
    "background-color": "white"
}

# Create a Container component
prediction_container = html.Div(
    children=[
        dmc.Container(
            children=[
                text_divider_and_tooltip,
                customer_id_input,
                prediction_type_radio_group,
                date_type_radio_group,
                start_datetime_picker,
                end_datetime_picker,
                time_interval_input,
            ],
            size="xs", px="xs", style=main_container_style
        ),
    ], style={"display": "flex", "justify-content": "center"}
)


# Create a Reset Button component
reset_button = dmc.Button(
    id="page-7-reset-button",
    children=dmc.Text("Reset", weight=500, color="green"),
    color="green",
    variant="outline",
    size="md",
    fullWidth=True,
    style={"margin-top": 20, "margin-right": 10},
)

# Create a Submit Button component
submit_button = dmc.Button(
    id="page-7-submit-button",
    children=dmc.Text("Submit", weight=500, color="white"),
    color="green",
    variant="gradient",
    gradient={"from": "teal", "to": "lime", "deg": 105},
    size="md",
    fullWidth=True,
    style={"margin-top": 20, "margin-right": 10},
)

# Combine the Reset and Submit buttons
button_group = html.Div(
    [
        dmc.Grid(
            children=[
                dmc.Col(reset_button, span=6),
                dmc.Col(submit_button, span=6),
            ],
            style={"margin-top": 20},
        )
    ], style={"width": 500, "margin": "auto", "margin-bottom": 25}
)


# Define the page layout
# ------------------------
layout = html.Div(
    [
        header,
        prediction_container,
        button_group,
        modal,
    ],
)
