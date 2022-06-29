import pandas as pd
from decimal import Decimal
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def get_amount(max_val, min_val):
  min_val = min_val.strip()
  max_val = max_val.strip()
  min_val = min_val.split("-")
  max_val = max_val.split("-")
  if len(min_val) > 1 or len(max_val) > 1:
    return 0
  else:
    min_val = min_val[0].strip()[1:]
    max_val = max_val[0].strip()[1:]

    return float(max_val) - float(min_val)
  

with open('assets\\amazon_uk_shoes_dataset.json', 'r') as datafile:
    data = json.load(datafile)
df = pd.DataFrame(data)
# df = pd.read_json("D:\Dashboard1\Dashboard\assets\amazon_uk_shoes_dataset.json.json")
df = df.dropna()
df_min = df.groupby("brand")['price'].min()
df_min = df_min.to_frame()
df_min = df_min.reset_index()
df_max = df.groupby("brand")['price'].max()
df_max = df_max.to_frame()
df_max = df_max.reset_index()

df_main = pd.merge(df_min, df_max, on='brand')

df_main.rename(columns = {'price_x':'min_price', 'price_y':'max_price'}, inplace = True)

df_main['range'] = [get_amount(df_main.loc[i, "max_price"] , df_main.loc[i, "min_price"]) for i in range(len(df_main))]

df_main = df_main.sort_values(by='range', ascending = False)

df_main= df_main[df_main['range'] > 0.00]

fig = px.scatter(df_main, x="range", y="brand", hover_data=['brand'])

layout = html.Div(children=[
    html.H1(children='Range of Branded Shoes Price'),
    html.Div(children='''A range plot of minimum and maximum value of the branded shoes price
    '''),
     dcc.Graph(
        id='example-graph',
        figure=fig
    )
])