import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv('assets\data.csv', encoding = 'unicode_escape')

sold_quantity = data[data.Quantity > 0]

aggregate_value = sold_quantity.groupby(['Country'], as_index=False).agg({'Quantity':sum})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.scatter(aggregate_value, x=aggregate_value.Country, y=aggregate_value.Quantity)

layout = html.Div(children=[
    html.H1(children='Quantity of Stocks sold in a Country'),
    html.Div(children='''
        A plot of products sold in a region
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])