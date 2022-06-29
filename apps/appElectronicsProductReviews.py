import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


data = pd.read_csv('assets\electronics_reviews.csv')

data.columns =[column.replace(".", "_") for column in data.columns] 

data.query('reviews_doRecommend == True', inplace = True)

data_min = data.groupby(['brand'], as_index=False).agg(min=('reviews_rating', 'min'))

data_max = data.groupby(['brand'], as_index=False).agg(max=('reviews_rating', 'max'))

data_avg = data.groupby(['brand'], as_index=False).agg(mean=('reviews_rating', 'mean'))

data_min = data_min.sort_values(by="min", ascending=False)

data_max = data_max.sort_values(by="max", ascending=False)

data_avg = data_avg.sort_values(by="mean", ascending=False)

trace1 = go.Bar(
    x=data_min['brand'],
    y=data_min['min'],
    name='Min'
)
trace2 = go.Bar(
    x=data_max['brand'],
    y=data_max['max'],
    name='MAX'
)
trace3 = go.Bar(
    x=data_avg['brand'],
    y=data_avg['mean'],
    name='MEAN'
)

layout = html.Div(children=[
    html.H1(children='Rating of Products'),

    html.Div(children='''
       Customer Review On Various Electronic Products.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=go.Figure(data=[trace1, trace2, trace3],
                               layout=go.Layout(barmode='group'))
    )
])