# Api-floristeria
# Instalación y Uso de la API de Autenticación

Este proyecto es una API de autenticación utilizando FastAPI y SQLite.

## Requisitos Previos

Asegúrate de tener instalado:
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto:
   ```bash
   git clone https://github.com/torvi30/api-floristeria.git
   cd api-floristeria
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Para iniciar la API, ejecuta:
    ```bash
    uvicorn main:app --reload
    ```

## Ejecución del Servidor
Esto iniciará el servidor en `http://127.0.0.1:8000`

## Archivos Importantes
- `main.py`: Archivo principal donde se define la API.
- `requirements.txt`: Contiene las dependencias necesarias para ejecutar el proyecto.
- `database.db`: Archivo SQLite que almacena los datos de usuario.

## Documentación Automática
Puedes acceder a la documentación generada automáticamente en:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Notas Adicionales
- Se usa SQLite como base de datos, pero puedes cambiarlo en la configuración.
- Las contraseñas se almacenan cifradas con bcrypt para mayor seguridad.