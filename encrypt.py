# Función para hash de contraseñas
import bcrypt

# Función para encriptar contraseñas
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') # Estandar de la libreria

# Función para desencriptar contraseñas
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))  # Estandar de la libreria