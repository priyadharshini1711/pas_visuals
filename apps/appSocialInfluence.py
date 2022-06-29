import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data2 = pd.read_csv('assets\Whatsgoodly - Thought Catalog Influencers.csv', encoding = 'unicode_escape')

data2 = data2.sort_values(by=["Count"], ascending=False)

questions = data2.groupby(["Question", "Answer"]).size().reset_index()

records = data2.groupby(["Question", "Answer"])

records = records.first()

questions["id"] = [i for i in range(1,25)]

records["id"] = [i for i in range(1, 25)]

data = pd.merge(questions, records, on='id')

del data[0]

del data['id']

layout = html.Div(children=[
    html.H1(children='Online Influence Marketing'),
    html.Div(children='''
        A table of most asked questions and answers
    '''),
     dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in data.columns],
    data=data.to_dict('records'),
    style_cell={'textAlign': 'left'},
)
])