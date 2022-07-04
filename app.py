import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html

import flask

server = flask.Flask(__name__)

app = dash.Dash(
    __name__, server=server, plugins=[dl.plugins.pages],external_stylesheets=[dbc.themes.CYBORG], update_title='Cargando...'
)

navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/info.png', height="30",className="center blanco")), href="/acercade"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/app.png', height="30",className="center blanco")), href="/monitoreo"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/arbol2.png', height="35",className="center blanco")), href="/arbolesenibague"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/prediccion.png', height="30",className="center blanco")), href="/prediccion"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/equipo.png', height="30",className="center blanco")), href="/equipo"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/images/mail.png', height="25",className="center blanco")), href="/contactanos"),class_name="mx-3")
    
    ],
    brand="Team 123",
    brand_href="/",
    color= "dask",
    dark=True,
    
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)

@server.route('/result', methods=['POST'])
def on_post():
    data = flask.request.form
    print(data)
    return flask.redirect(flask.request.url)


if __name__ == "__main__":
    app.run_server(debug=False)