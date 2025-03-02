from fastapi import APIRouter
from pydantic import BaseModel
from user_jwt import createToken
from fastapi.responses import JSONResponse

#Instancia de APIRouter
router_users = APIRouter()


#Modelo de usuario
class User(BaseModel):
    email: str
    password: str


#Ruta de login
@router_users.post('/login', tags=['Login'])
def login(user: User):
    if user.email == 'duber@gmail.com' and user.password == '123':
        token: str = createToken(user.dict())
        print(f'Token: {token}')
        return JSONResponse(content={'message': 'Usuario Autenticado✅!', 'token': token})

