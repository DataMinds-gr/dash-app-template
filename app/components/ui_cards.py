###############################
#                             #
#    Design beutiful cards    #
#                             #
###############################


# Import libraries
from dash import dcc, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
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
def numbers_and_ring_card(
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

# Card with number and comparison
def numbers_and_comparison_card(
        title: str = "Revenue",
        num: int = 13456,
        perc: int = 87
):
    if perc > 0:
        col = "green"
        icon = DashIconify(icon="mdi:arrow-top-right", color="green", width=25, height=25)
        msg = "increase compared to last month"
    elif perc < 0:
        col = "red"
        icon = DashIconify(icon="mdi:arrow-bottom-right", color="red", width=30, height=30)
        msg = "decrease compared to last month"
    else:
        col = "grey"
        icon = DashIconify(icon="mdi:arrow-right", color="grey", width=20, height=20)
        msg = "no change compared to last month"

    info_stack = dmc.Stack(
        [
            dmc.Title(title, order=5, size="sm"),
            dmc.Title(f"{num:,}$", order=2),
            dmc.Group([
                dmc.Text(f"{perc}%", color=col, size="sm"),
                dmc.Text(msg, color="grey", size="sm"),
            ], spacing=2)
        ]
    )

    card = dmc.Card(
        [
            dmc.Grid(
                [
                    dmc.Col(info_stack, span=10),
                    dmc.Col(icon, span=2, mt="lg"),
                ]
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
    )

    return card


# Create a complex card component
def complex_card_with_image():
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
