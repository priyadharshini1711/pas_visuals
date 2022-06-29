import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import appLocationBasedSales, appSocialInfluence, appRangeOfPrice, appSearchRelevance, appHighestDiscountShoeBrand, appElectronicsProductReviews

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "overflow-y": "scroll"
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem", 
    "overflow-x": "scroll",
    "width": "calc(100% - 18rem)"
}

sidebar = html.Div(
    [
        html.H2("PAS Visuals", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Electronics Product Rating", href="/page-1", id="page-1-link"),
                dbc.NavLink("Highest Discounted Shoe", href="/page-2", id="page-2-link"),
                dbc.NavLink("Location Based Sales", href="/page-3", id="page-3-link"),
                dbc.NavLink("Range of Branded Shoes Price", href="/page-4", id="page-4-link"),
                dbc.NavLink("Most Searched Products", href="/page-5", id="page-5-link"),
                dbc.NavLink("Online Influence Marketing", href="/page-6", id="page-6-link"),
                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
    
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return appElectronicsProductReviews.layout
    elif pathname == "/page-2":
        return appHighestDiscountShoeBrand.layout
    elif pathname == "/page-3":
        return appLocationBasedSales.layout
    elif pathname == "/page-4":
        return appRangeOfPrice.layout
    elif pathname == "/page-5":
        return appSearchRelevance.layout
    elif pathname == "/page-6":
        return appSocialInfluence.layout
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8050, debug=True)