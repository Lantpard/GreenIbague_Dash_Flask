from dash import html,dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/contactanos")

layout = html.Div([
        html.Header( 
                html.H1("Contáctanos")
                )
            ,
        html.Div([
                html.Div([
                html.H3("Redes Sociales Alcaldía Ibagué:")
                
                ],className="redes")
                ,
                html.Div([
                    dbc.NavLink((

                    html.Img(src='/assets/images/face.webp', height="30")
                    ),href="https://es-la.facebook.com/alcaldiaibague/", target="_blank",class_name="link")
                ] ,className="facebook text-center textblanco")
                ,
                html.Div([
                    dbc.NavLink((   
                    html.Img(src='/assets/images/twitter.webp', height="30")
                    ),href="https://twitter.com/Alcaldiaibague", target="_blank")
                    
                ],className="twitter")
                ,
                html.Div([
                    dbc.NavLink((
                    html.Img(src='/assets/images/insta.webp', height="30",className="mx-2")
                    ),href="https://www.instagram.com/alcaldiadeibague/", target="_blank")
                ],className="instagram")
                ,
                html.Div([
                    dbc.NavLink((
                    html.Img(src='/assets/images/alcaldia.png', height="40")
                    ),href="https://ibague.gov.co/portal/index.php", target="_blank")
                ],className="web")

        ],className="info")
        ,
        html.Form([
                html.Div(
                    [
                    
                        html.H3("Deja tu comentario: "),
                        
                    ],
                        className="correo",
                    )

                , html.Div(
                    [
                        dcc.Textarea(
                            id='textarea-example',
                            value='',
                            style={'width': '100%', 'height': 200},
                        )
                    ],
                        className="Observacion",
                    ) ,
                    html.Button([ "Enviar"

                                    ],type="submit",className="btn btn-light btn-outline-primary button1")
                    ],className="formulario")

        ],className="contenedor6")