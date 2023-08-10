###########################
#                         #
#    PAGE 2: ANALYTICS    #
#                         #
###########################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc
import plotly.express as px

from components.ui_cards import create_card
from utils.graphs import line_plot, pie_plot


# Create a rows with cards
card1 = card2 = card3 = card4 = create_card()
cards_row = dmc.Grid(
    children=[
        dmc.Col(card1, span=3),
        dmc.Col(card2, span=3),
        dmc.Col(card3, span=3),
        dmc.Col(card4, span=3),
    ],
    gutter="xl",
)

# Segment Control for Time
segment_control = dmc.SegmentedControl(
    id="segment_control",
    data=["Day", "Week", "Month", "Year", "Custom"],
    value="Day",
    size="md",
)

# When Segment Control is "Custom" show DatePickerRange
date_range_picker = dmc.DateRangePicker(
    id="date_range_picker",
    size="md",
)

segment_control_and_date_range_picker = dmc.Grid(
        children=[
            dmc.Col(segment_control, span=3, offset=4),
            dmc.Col(date_range_picker, span=3, offset=1)
        ], gutter="md", style={"margin-top": "20px"}
)



# Create line graph
df = px.data.gapminder()
single_continent_country = df[df["country"] == "Greece"]

fig_line = line_plot(
    df=single_continent_country, 
    x="year", y="gdpPercap",
    title="GDP per capita in Greece", x_title="Year", y_title="GDP per capita")


# Create pie graph
df = px.data.tips()
fig_pie = pie_plot(df=df, labels="day", values="tip", title="Tips by day")


# Create a row with graphs
line_plot_and_pie_plot = dmc.Grid(
    children=[
        dmc.Col(
            dmc.Card(
                children=[
                    dcc.Graph(figure=fig_line)
                ],
                withBorder=True,
                shadow="sm",
                radius="md",
            ), span=8),
        dmc.Col(
            dmc.Card(
                children=[
                    dcc.Graph(figure=fig_pie)
                ],
                withBorder=True,
                shadow="sm",
                radius="md",
            ), span=4),
    ],
    gutter="md",
    style={"margin-top": "20px"}
)



# Define the page layout
# ------------------------
layout = html.Div(
    [
        dmc.Title("Analytics", order=2, className="page-title"),
        dmc.Container(
            children=[
                cards_row,
                segment_control_and_date_range_picker,
                line_plot_and_pie_plot,
                line_plot_and_pie_plot
            ],
            style={"margin": "20px", "width": "100%", "maxWidth": "95%"}
        ),
    ]
)






