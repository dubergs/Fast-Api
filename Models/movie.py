from DataBase.db import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    año = Column(Integer)
    genero = Column(String)
    pais = Column(String)
    idioma = Column(String)
    calificacion = Column(Float)