# db.py
import psycopg2
import bcrypt

def conectar():
    return psycopg2.connect(
        host="simple-node-app.cbkk2cg4ulnw.us-east-2.rds.amazonaws.com",
        port=5432,
        user="postgres",
        password="postgres",
        dbname="template_cpepr"
    )

def verificar_login(email, password):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT password FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        hashed = resultado[0].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    else:
        return False
