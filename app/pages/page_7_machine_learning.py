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

)

# Create a Divider component
text_divider = dmc.Divider(
    label="Prediction Parameters",
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
id_input = dmc.NumberInput(
    label=dmc.Text("Customer ID", color="gray", size="sm"),
    value=1_000,
    min=1_000,
    max=10_000,
    step=1,
    style={"width": 250, "margin-top": 20},
)

# Prediction Type radio group
prediction_type_data = [
    ["interpolative", "Interpolative"],
    ["extrapolative", "Extrapolative"]
]

prediction_type_radio_group = dmc.RadioGroup(
    [dmc.Radio(l, value=k) for k, l in prediction_type_data],
    id="radiogroup-interpolative-extrapolative",
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
    [dmc.Radio(l, value=k) for k, l in date_type_data],
    id="radiogroup-date-type",
    value="timestamp",
    label=dmc.Text("Date Type:", color="gray", size="sm"),
    size="sm",
    style={"margin-top": 20},
)

# Create a Time Interval component
time_interval_input = dmc.NumberInput(
    label=dmc.Text("Time Interval (hours)", color="gray", size="sm"),
    value=12,
    min=1,
    max=24,
    step=1,
    style={"width": 250, "margin-top": 20},
)

# Start Datetime Picker component
start_date_picker = dmc.DatePicker(
    id="start-date-picker",
    label=dmc.Text("Start Datetime:", color="gray", size="sm"),
    minDate=date(2022, 1, 1),
    maxDate=date(2023, 12, 31),
    amountOfMonths=1,
    dropdownPosition="bottom"
)

start_time_picker = dmc.TimeInput(
    label=dmc.Text("", size="sm"),
    id="start-time-picker"
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
    dropdownPosition="bottom"
)

end_time_picker = dmc.TimeInput(
    label=dmc.Text("", size="sm"),
    id="end-time-picker"
)

# Combine the Date and Time Pickers
end_datetime_picker = dmc.Grid(
    children=[
        dmc.Col(end_date_picker, span=6),
        dmc.Col(end_time_picker, span=6),
    ],
    style={"margin-top": 20},
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
                id_input,
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
    id="reset-button",
    children=dmc.Text("Reset", weight=500),
    variant="outline",
    size="md",
    fullWidth=True,
)

# Create a Submit Button component
submit_button = dmc.Button(
    id="submit-button",
    children=dmc.Text("Submit", weight=500, color="white"),
    variant="gradient",
    gradient={"from": "indigo", "to": "cyan", "deg": 105},
    size="md",
    fullWidth=True,
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
        button_group
    ],
)
