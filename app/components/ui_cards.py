# Import libraries
import dash_mantine_components as dmc

# Create a card component
def create_card(title: str = "Title per hour", number: int = 10100):
    return dmc.Card(
        children=[
            dmc.Text(children=title, weight=300),
            dmc.Center(dmc.Title(children=f"{number} Kwh", order=3), m="md"),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
    )