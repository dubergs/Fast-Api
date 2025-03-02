from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from DataBase.db import engine, Base
from Models.movie import Movie as MovieModel
from Routers.movie import routerMovie
from Routers.users import router_users


#Documentacion del proyecto
app = FastAPI(
    title='Aprendiendo FastAPI', 
    description='Una API en mis primeros pasos',
    version='0.0.1'
    )


#Rutas de la API
app.include_router(routerMovie)
app.include_router(router_users)


#Creacion de la base de datos
Base.metadata.create_all(bind=engine)


#Ruta de inicio
@app.get('/', tags=['Inicio'])
def read_root():
    return HTMLResponse('<h2>Hola mundo!</h2>')
