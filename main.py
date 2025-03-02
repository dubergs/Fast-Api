from fastapi import FastAPI, Body, Path, Query, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional
from pydantic import Field
from user_jwt import createToken, validarToken
from fastapi.security import HTTPBearer

app = FastAPI(
    title='Aprendiendo FastAPI', 
    description='Una API en mis primeros pasos',
    version='0.0.1'
    )

class User(BaseModel):
    email: str
    password: str

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validarToken(auth.credentials)
        if data['email'] != 'duber@gmail.com':
            raise HTTPException(status_code=403, detail='Token invalido❌!')

class Movie(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(default='Titulo de la pelicula', min_length=8, max_length=30)
    año: int = Field(default=2023)
    genero: str = Field(default='Genero de la pelicula')
    pais: str = Field(default='Pais de la pelicula')
    idioma: str = Field(default='Idioma de la pelicula')
    calificacion: float = Field(ge=1, le=10)

        
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

@app.post('/login', tags=['Login'])
def login(user: User):
    if user.email == 'duber@gmail.com' and user.password == '123':
        token: str = createToken(user.dict())
        print(f'Token: {token}')
        return JSONResponse(content={'message': 'Usuario Autenticado✅!', 'token': token})

@app.get('/', tags=['Inicio'])

def read_root():
    return HTMLResponse('<h2>Hola mundo!</h2>')


@app.get('/movies', tags=['Peliculas'], dependencies=[Depends(BearerJWT())])
def get_movies():
    return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=['Peliculas'])
def get_movie(id: int = Path(ge=1, le=100)):
    for i in movies:
        if i["id"] == id:
            return i
        return []
    
    
@app.get('/movies/', tags=['Peliculas'])
def get_movies_by_category(genero: str = Query(min_length=4)):
    return genero


@app.post('/movies', tags=['Peliculas'])
def create_movie(movie: Movie):
    movies.append(movie)
    print(movies)
    return JSONResponse(content={'message': 'Pelicula creada con exito👌!', 'Pelicula': [movie.model_dump() for m in movies]})


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
        return JSONResponse(content={'message': 'Pelicula actulizada con exito✅!', 'Pelicula': [movie.model_dump() for m in movies]})
    
@app.delete('/movies/{id}', tags=['Peliculas'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(content={'message': 'Pelicula eliminada con exito✅!'})