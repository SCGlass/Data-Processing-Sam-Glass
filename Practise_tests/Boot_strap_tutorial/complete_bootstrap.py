import datetime

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import plotly_express as px
from dash import dcc, html
from dash.dependencies import Input, Output

# start = datetime.datetime(2020, 1 , 1) # using datetime to select where to start
# end = datetime.datetime(2020, 12, 3) # using datetime to select where to end
# # This will pull the data from a website called "stooq.com" and create a df
# df = web.DataReader(['AMZN', 'GOOGL','FB','PFE','BNTX','MRNA'],'stooq', start=start, end=end)
# df = df.stack().reset_index() # stacking the headers into one
# print(df[:15]) # Shows the first 15 lines of the pulled dataframe

# saving as csv file to work with so we dont overload from the API
# df.to_csv("Practise_tests\Boot_strap_tutorial\mystocks.csv", index=False)

df = pd.read_csv(
    "Practise_tests\Boot_strap_tutorial\mystocks.csv"
)  # Now importing dataframe from file
print(df[:15])

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ],  # using flask in background for the app adn setting the visual theme
    meta_tags=[
        {
            "name": "viewport",  # The next two lines responds to a mobile layout and makes it smaller for that
            "content": "width=device-width, initial-scale=1.0",
        }
    ],
)


#   Layout section: Bootstrap
# ------------------------------------------------------------------------------------
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "Stock Market Dashboard",
                        className="text-center text-primary, mb-4", # makes center and blue mb4 gives a little space under the title
                    )
                )  
            ]
        ),
        dbc.Row([]),
        dbc.Row([]),
    ]
)

# need this code to run the app for dash
if __name__ == "__main__":
    app.run_server(debug=True, port=3000)
