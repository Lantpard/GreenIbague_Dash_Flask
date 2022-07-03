from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/")

layout = html.Div([
    
            html.Header( 
                html.H1("Green Ibagué")
                )
            ,

            html.Div([
    
                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/info.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Acerca de")),href="/acercade")
        
                ],className="widget1")
                
                ,

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/app.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Monitoreo")),href="/monitoreo")
                ],className="widget2"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/arbol2.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Árboles en Ibagué")),href="/arbolesenibague")
                ],className="widget3"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/prediccion.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Predicción")),href="/prediccion")
                ],className="widget4"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/equipo.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Equipo")),href="/equipo")
                ],className="widget5"),

                html.Div([
                    dbc.NavLink(
                    (html.Img(src='/assets/images/mail.png', height="100px", width="100px"),
                    html.Br(),
                    html.H3("Contáctanos")),href="/contactanos")
                ],className="widget6")

            ],className="contenido")

        ],className="contenedor")