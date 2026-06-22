# views/login.py
# Pantalla de inicio de sesión

try:
    import customtkinter as ctk
except ImportError:  # type: ignore[no-redef]
    import tkinter as ctk

from models import usuario
from config.settings import (
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_ACENTO,
    COLOR_FONDO,
    COLOR_BLANCO,
    COLOR_TEXTO,
    COLOR_ERROR,
    FUENTE_TITULO,
    FUENTE_NORMAL,
    APP_NOMBRE,
)


class VentanaLogin(ctk.CTk):
    """Ventana de inicio de sesión de la aplicación."""

    def __init__(self):
        super().__init__()
        self.title(APP_NOMBRE)
        self.geometry("420x520")
        self.configure(fg_color=COLOR_FONDO)
        self.resizable(False, False)

        # Logo / Título
        self.label_titulo = ctk.CTkLabel(
            self,
            text="⚖ Despacho Jurídico",
            font=FUENTE_TITULO,
            text_color=COLOR_PRIMARIO,
        )
        self.label_titulo.pack(pady=(50, 30))

        # Campo de usuario
        self.entry_usuario = ctk.CTkEntry(
            self,
            placeholder_text="Usuario",
            font=FUENTE_NORMAL,
            width=280,
            height=40,
        )
        self.entry_usuario.pack(pady=10)

        # Campo de contraseña
        self.entry_contrasena = ctk.CTkEntry(
            self,
            placeholder_text="Contraseña",
            font=FUENTE_NORMAL,
            width=280,
            height=40,
            show="*",
        )
        self.entry_contrasena.pack(pady=10)

        # Mensaje de error (vacío al inicio)
        self.label_error = ctk.CTkLabel(
            self,
            text="",
            font=FUENTE_NORMAL,
            text_color=COLOR_ERROR,
        )
        self.label_error.pack(pady=5)

        # Botón de ingresar
        self.btn_ingresar = ctk.CTkButton(
            self,
            text="Ingresar",
            font=FUENTE_NORMAL,
            fg_color=COLOR_PRIMARIO,
            hover_color=COLOR_SECUNDARIO,
            width=280,
            height=40,
            command=self.iniciar_sesion,
        )
        self.btn_ingresar.pack(pady=20)

    def iniciar_sesion(self):
        """Valida las credenciales e inicia sesión."""
        usuario_texto = self.entry_usuario.get()
        contrasena_texto = self.entry_contrasena.get()

        if not usuario_texto or not contrasena_texto:
            self.label_error.configure(text="Completa todos los campos")
            return

        datos_usuario = usuario.verificar_login(usuario_texto, contrasena_texto)

        if datos_usuario:
            self.label_error.configure(text="")
            print(f"Bienvenido {datos_usuario['nombre']}")
        else:
            self.label_error.configure(text="Usuario o contraseña incorrectos")