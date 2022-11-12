import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly_express as px
import dash_bootstrap_components as dbc
import pandas_datareader.data as web
import datetime
import pandas as pd

# start = datetime.datetime(2020, 1 , 1) # using datetime to select where to start
# end = datetime.datetime(2020, 12, 3) # using datetime to select where to end
# # This will pull the data from a website called "stooq" and create a df
# df = web.DataReader(['AMZN', 'GOOGL','FB','PFE','BNTX','MRNA'],'stooq', start=start, end=end)
# df = df.stack().reset_index() # stacking the headers into one
# print(df[:15]) # Shows the first 15 lines of the pulled dataframe

# saving as csv file to work with so we dont have to pull from the API all the time
#df.to_csv("Practise_tests\Boot_strap_tutorial\mystocks.csv", index=False)

df = pd.read_csv("Practise_tests\Boot_strap_tutorial\mystocks.csv") # Now importing dataframe from file
print(df[:15])






