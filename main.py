from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title='Aprendiendo FastAPI', 
    description='Una API en mis primeros pasos',
    version='0.0.1'
    )

class Movie(BaseModel):
    id: Optional[int] = None
    titulo: str
    año: int
    genero: str
    pais: str
    idioma: str
    calificacion: float
    
    
    
movies = [
    {
        "id": 1,
        "titulo": "El Padrino",
        "año": 1972,
        "genero": ["Crimen","Drama"],
        "pais": "Estados Unidos",
        "idioma": "Inglés",
        "calificacion": 9.2
    }
]


@app.get('/', tags=['Inicio'])

def read_root():
    return HTMLResponse('<h2>Hola mundo!</h2>')


@app.get('/movies', tags=['Peliculas'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['Peliculas'])
def get_movie(id: int):
    for i in movies:
        if i["id"] == id:
            return i
        return []
    
    
@app.get('/movies/', tags=['Peliculas'])
def get_movies_by_category(genero: str):
    return genero


@app.post('/movies', tags=['Peliculas'])
def create_movie(movie: Movie):
    movies.append(
        movie
    )
    return movies

print(movies)

@app.put('/movies/{id}', tags=['Peliculas'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item ['id'] == id:
             item['titulo'] = movie.titulo,
             item['año'] = movie.año,
             item['genero'] = movie.genero,
             item['pais'] = movie.pais,
             item['idioma'] = movie.idioma,
             item['calificacion'] = movie.calificacion
        return movies
    
@app.delete('/movies/{id}', tags=['Peliculas'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies