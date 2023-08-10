###############################
#                             #
#    Design beutiful cards    #
#                             #
###############################


# Import libraries
from dash import dcc, html
import dash_mantine_components as dmc
from utils.graphs import percentage_ring_plot


# Create a simple card component
def simple_card(title: str = "Title per hour", number: int = 10100):
    card = dmc.Card(
        children=[
            dmc.Text(children=title, weight=300),
            dmc.Center(dmc.Title(children=f"{number} Kwh", order=3), m="md"),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
    )
    return card


# Create a informative card component
def numbers_and_rings_card(
        title: str = "Project Tasks",
        num1: int = 100, num2: int = 70, num3: int = 30,
        perc: int = 87
):

    fig = percentage_ring_plot(perc)

    left_section = dmc.Stack(
        [
            dmc.Title(title, order=2),
            dmc.Stack([
                dmc.Title(num1, order=3),
                dmc.Text("Completed", color="grey", size="sm"),
            ], spacing=1),

            dmc.Group(
                [
                    dmc.Stack([
                        dmc.Title(num2, order=3),
                        dmc.Text("Remaining",  color="grey", size="sm"),
                    ],  spacing=1),
                    dmc.Stack([
                        dmc.Title(num3, order=3),
                        dmc.Text("In Progress",  color="grey", size="sm"),
                    ],  spacing=1)
                ]
            )
        ]
    )

    right_section = dcc.Graph(figure=fig, config={"displayModeBar": False})

    card = dmc.Card(
        [
            dmc.Grid(
                [
                    dmc.Col(left_section, span=7),
                    dmc.Col(right_section, span=5),
                ]
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        # style={"width": 650, "height": 250},
    )

    return card


# Create a complex card component
def complex_card():
    card = dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                    height=160,
                )
            ),
            dmc.Group(
                [
                    dmc.Text("Norway Fjord Adventures", weight=500),
                    dmc.Badge("On Sale", color="red", variant="light"),
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                size="sm",
                color="dimmed",
            ),
            dmc.Button(
                "Book classic tour now",
                variant="light",
                color="blue",
                fullWidth=True,
                mt="md",
                radius="md",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 350},
    )

    return card
