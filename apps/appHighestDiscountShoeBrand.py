import pandas as pd
import numpy as np
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('assets\Adidas final.csv', sep=';')

df = df.groupby('Brand', as_index=False)['Discount']

df = df.mean()

df = df.reset_index()

fig = px.bar(df, x='Brand', y='Discount')

layout = html.Div(children=[
    html.H1(children='Highest Discounts on Adidas Shoe'),

    html.Div(children='''
        A bar graph for highest discounted adidas shoe.
    '''),

    dcc.Graph(
        id='bar-chart',
        figure=fig
    ),
])