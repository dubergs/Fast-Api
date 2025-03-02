import jwt

def createToken(data: dict):
    token: str = jwt.encode(payload=data, key='misecret', algorithm='HS256')
    return token

def validarToken(token: str) -> dict:
    try:
        data = jwt.decode(token, 'misecret', algorithms=['HS256'])
        return data
    except:
        return 'Token invalido'