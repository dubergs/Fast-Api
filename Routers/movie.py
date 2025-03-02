from fastapi import Path, Query, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from pydantic import Field
from user_jwt import validarToken
from fastapi.security import HTTPBearer
from DataBase.db import Session
from Models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from Models.movie import Movie

routerMovie = APIRouter()


#Clase para validar el token
class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validarToken(auth.credentials)
        if data['email'] != 'duber@gmail.com':
            raise HTTPException(status_code=403, detail='Token invalido❌!')


#Modelo de pelicula
class Movie(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(default='Titulo de la pelicula', min_length=8, max_length=30)
    año: int = Field(default=2023)
    genero: str = Field(default='Genero de la pelicula')
    pais: str = Field(default='Pais de la pelicula')
    idioma: str = Field(default='Idioma de la pelicula')
    calificacion: float = Field(ge=1, le=10)


#Obtener lista de peliculas
@routerMovie.get('/movies', tags=['Peliculas'], dependencies=[Depends(BearerJWT())])
def get_movies():
    db = Session()
    data = db.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(data))


#Obtener pelicula por id
@routerMovie.get('/movies/{id}', tags=['Peliculas'])
def get_movie(id: int = Path(ge=1, le=100)):
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': '❌Pelicula no encontrada!'})
    return JSONResponse(content=jsonable_encoder(data))
    
    
#Obtener peliculas por genero
@routerMovie.get('/movies/', tags=['Peliculas'])
def get_movies_by_category(genero: str = Query(min_length=4)):
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.genero == genero).all()
    if not data:
        return JSONResponse(status_code=404, content={'message': '❌No contamos con esta categoria!'})
    return JSONResponse(content=jsonable_encoder(data))


#Crear pelicula
@routerMovie.post('/movies', tags=['Peliculas'])
def create_movie(movie: Movie):
    db = Session()
    newMovie = MovieModel(**movie.dict())
    db.add(newMovie)
    db.commit()
    return JSONResponse(content={'message': 'Pelicula creada con exito👌!'})


#Actualizar pelicula
@routerMovie.put('/movies/{id}', tags=['Peliculas'])
def update_movie(id: int, movie: Movie):
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': '❌Pelicula no encontrada!'})
    data.titulo = movie.titulo
    data.año = movie.año
    data.genero = movie.genero
    data.pais = movie.pais
    data.idioma = movie.idioma
    data.calificacion = movie.calificacion
    db.commit()
    return JSONResponse(content={'message': '✅Pelicula actulizada con exito!', 'Pelicula': [movie.model_dump() for m in movies]})

  
#Eliminar pelicula  
@routerMovie.delete('/movies/{id}', tags=['Peliculas'])
def delete_movie(id: int):
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': '❌Pelicula no encontrada!'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message': '✅Pelicula eliminada con exito!', 'Pelicula': jsonable_encoder(data)})