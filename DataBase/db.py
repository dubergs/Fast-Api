import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#Nombre del archivo SQLite que se utilizará como base de datos.
sqliteName = '../movies.sqlite'

#Obtiene el directorio base donde se encuentra el script actual.
base_dir = os.path.dirname(os.path.realpath(__file__))

#Construye la URL de la base de datos SQLite.
databaseUrl = f'sqlite:///{os.path.join(base_dir, sqliteName)}'

#Crea el motor de base de datos, que se encargará de gestionar la conexión con SQLite.
engine = create_engine(databaseUrl, echo=True)

#Session que permitirá interactuar con la base de datos.
Session = sessionmaker(bind=engine)

#Clase base para la creación de modelos con SQLAlchemy.
Base = declarative_base()
