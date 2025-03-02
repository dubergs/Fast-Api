Aplicación web desarrollada con FastAPI para gestionar información de películas.

--------------------------------------------------------------------------------
Instalación:
git clone https://github.com/dubergs/Fast-Api.git

cd Fast-Api

source venv/bin/activate  # En Windows: venv\Scripts\activate

pip install -r requirements.txt

-------------------------------------------------------------
Ejecución:
uvicorn main:app --reload  

Accede a la API en http://127.0.0.1:8000
Documentación en http://127.0.0.1:8000/docs

-------------------------------------------
Estructura:
main.py → Punto de entrada de la aplicación
DataBase/ → Configuración de la base de datos
Models/ → Definición de modelos SQLAlchemy
Routers/ → Endpoints de la API
user_jwt.py → Gestión de autenticación con JWT

----------------------------------------------
Contribución:
Haz un fork
Crea una rama (feature/nueva-funcionalidad)
Realiza cambios y haz commit
Envía un pull request
