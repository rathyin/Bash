from jupyter_dash import JupyterDash
import dash
import dash_bootstrap_components as dbc

# meta_tags are required for the app layout to be mobile responsive
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True