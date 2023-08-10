###############################
#                             #
#    Design React Tables      #
#                             #
###############################

# Import libraries
from dash_mantine_react_table import DashMantineReactTable

def dash_mantine_react_table(data):
    if data is None:
        grid = DashMantineReactTable(
            data=[],
            columns=[],
            mrtProps={
                "enableHiding": False,
                "enableColumnFilters": False,
                "initialState": {"density": "sm"},
                "mantineTableProps": {"fontSize": "sm"},
                "mantineTableHeadCellProps": {"style": {"fontWeight": 500}},
            },
            mantineProviderProps={
                "theme": {
                    "colorScheme": "dark",
                },
            },
        )
    else:

        grid = DashMantineReactTable(
                data=data.to_dict("records"),
                columns=[{"accessorKey": i, "header": i} for i in data.columns],
                mrtProps={
                    "enableHiding": False,
                    "enableColumnFilters": False,
                    "initialState": {"density": "sm"},
                    "mantineTableProps": {"fontSize": "sm"},
                    "mantineTableHeadCellProps": {"style": {"fontWeight": 500}},
                }
            )
    
    return grid
