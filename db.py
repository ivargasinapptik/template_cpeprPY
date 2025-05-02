# db.py
import psycopg2
import bcrypt
from dotenv import load_dotenv
import os

# Carga variables desde el archivo .env
load_dotenv()

def conectar():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def verificar_login(email, password):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT password, rol FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        return "email_invalido"

    hashed_password, rol = resultado
    hashed_password = hashed_password.encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return "password_incorrecto"

    if rol != "admin":
        return "no_admin"

    return "login_exitoso"
