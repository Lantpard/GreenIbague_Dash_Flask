import dash
import flask
import dash_labs as dl
import dash_bootstrap_components as dbc

server = flask.Flask(__name__)

app = dash.Dash(
    __name__, server=server, plugins=[dl.plugins.pages],external_stylesheets=[dbc.themes.CYBORG], update_title='Cargando...'
)

server = app.server


