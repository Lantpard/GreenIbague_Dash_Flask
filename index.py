import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html

from app import app
from app import server

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


if __name__ == '__main__':
    app.run_server(debug=False)
