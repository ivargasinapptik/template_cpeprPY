# main.py
import customtkinter as ctk
from tkinter import messagebox
from db import verificar_login
import sys  # al inicio del archivo

# Configuración general
ctk.set_appearance_mode("dark")  # Cambia a "light" si prefieres
ctk.set_default_color_theme("blue")

# Funciones
def abrir_ventana_base():
    ventana_base = ctk.CTkToplevel()
    ventana_base.title("Panel Principal")
    ventana_base.geometry("400x200")

    ctk.CTkLabel(ventana_base, text="¡Bienvenido al sistema del colegio!", font=("Arial", 16)).pack(pady=20)

    # Manejo del cierre de la ventana (dashboard)
    def cerrar_aplicacion():
        app.destroy()  # También puedes usar sys.exit()
    
    ventana_base.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)


def login():
    email = entry_email.get()
    password = entry_password.get()

    resultado = verificar_login(email, password)

    if resultado == "login_exitoso":
        messagebox.showinfo("Éxito", "Login exitoso")
        app.withdraw()
        abrir_ventana_base()
    elif resultado == "no_admin":
        messagebox.showerror("Acceso denegado", "No tiene permisos de administrador")
    elif resultado == "password_incorrecto":
        messagebox.showerror("Error", "Contraseña incorrecta")
    elif resultado == "email_invalido":
        messagebox.showerror("Error", "El correo no está registrado")

# Interfaz
app = ctk.CTk()
app.title("Login - Colegio")
app.geometry("350x250")

ctk.CTkLabel(app, text="Email", font=("Arial", 14)).pack(pady=(20, 5))
entry_email = ctk.CTkEntry(app, width=250)
entry_email.pack()

ctk.CTkLabel(app, text="Contraseña", font=("Arial", 14)).pack(pady=(15, 5))
entry_password = ctk.CTkEntry(app, width=250, show="*")
entry_password.pack()

ctk.CTkButton(app, text="Iniciar sesión", command=login).pack(pady=30)

app.mainloop()
