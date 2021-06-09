from jupyter_dash import JupyterDash
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import import_ipynb

from app  import app
from app  import server

#hello
# Connect to your app pages
# from apps import bar, mount
# from ipynb.fs.full.apps.mount import *
# from ipynb.fs.full.apps.bar import *
from apps import bar
from apps import mount
from apps import knn
app.css.append_css({"external_url": "http://10.1.1.128:8888/edit/Dash/assets/custom.css#"})

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": 'MediumSeaGreen',
}
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H2("Dashboard"),
        html.Hr(),
        html.P("Plotly Dash Graphing Library", className="lead"),
        dbc.Nav(
         [
             dbc.NavLink("Home", href="/apps/bar", active="exact"),
             dbc.NavLink("Knn", href="/apps/knn", active="exact"),
            dbc.NavLink("Themes", href="/apps/mount", active="exact"),
                 ],
            vertical=True,
            pills=True,),
         ],style=SIDEBAR_STYLE),
    html.Div(id='page-content', children=[])
    
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/bar':
        return bar.layout
    if pathname == '/apps/mount':
        return mount.layout
    if pathname == '/apps/knn':
        return knn.layout
    else:
        return bar.layout


if __name__ == '__main__':
    app.run_server(debug=True,host = "10.1.1.128", port=8050)
