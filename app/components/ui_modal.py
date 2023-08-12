#########################
#                       # 
#   Prediction Modal    #
#                       #
#########################

# Import required libraries
import dash_mantine_components as dmc

modal = dmc.Modal(
            title=dmc.Text("Machine Learning Model Prediction", size="xl"),
            id="prediction-modal",
            zIndex=10000,
            opened = False,
            children=[
                dmc.Text(
                    "Based on the input parameters, the machine learning model predicts the following:"
                    ),
                dmc.Space(h=20),
                dmc.Text(
                    children=[],
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan", "deg": 45},
                    style={"fontSize": 20},
                    id="prediction-text"
                ),

                dmc.Space(h=20),
                dmc.Group(
                    [
                        dmc.Button(
                            "Ok",
                            variant="outline",
                            id="prediction-modal-close-button",
                        ),
                    ],
                    position="right",
                )
            ]
        )