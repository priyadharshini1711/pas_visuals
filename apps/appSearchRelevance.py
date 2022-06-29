import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_table

app = dash.Dash(__name__)

df = pd.read_csv('assets\search.csv',engine='python')

df = df.groupby('query', as_index=False)['relevance', 'relevance:variance'].sum()

df = df.sort_values(by="relevance:variance", ascending=False)

df.columns = ['Query', 'Relevance', 'Variance']

df = df.head(10)

fig = px.pie(df, values='Variance', names='Query')

layout = html.Div(children=[
    html.H1(children='Most Searched products on the Internet'),

    html.Div(children='''
        A pie chart for the most Searched products on the Internet.
    '''),

    dcc.Graph(
        id='pie-chart',
        figure=fig
    ),
])


