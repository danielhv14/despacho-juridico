# models/usuario.py
# Modelo CRUD para tabla usuarios

from database.connection import ejecutar_consulta


def existen_usuarios():
    """Verifica si ya existe al menos un usuario registrado."""
    query = "SELECT COUNT(*) AS total FROM usuarios"
    resultado = ejecutar_consulta(query, fetch=True)
    return resultado[0]["total"] > 0


def crear(data):
    """Crea un nuevo usuario en la base de datos."""
    query = """
    INSERT INTO usuarios
    (nombre, usuario, contrasena, rol,
     pregunta_seguridad, respuesta_seguridad)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["nombre"],
        data["usuario"],
        data["contrasena"],
        data.get("rol", "admin"),
        data.get("pregunta_seguridad", ""),
        data.get("respuesta_seguridad", ""),
    ))


def verificar_login(usuario, contrasena):
    """Verifica las credenciales de login y retorna el usuario si son correctas."""
    query = """
    SELECT * FROM usuarios
    WHERE usuario = %s AND contrasena = %s AND activo = 1
    """
    resultado = ejecutar_consulta(query, (usuario, contrasena), fetch=True)
    return resultado[0] if resultado else None


def obtener_por_usuario(usuario):
    """Retorna un usuario por su nombre de usuario."""
    query = "SELECT * FROM usuarios WHERE usuario = %s AND activo = 1"
    resultado = ejecutar_consulta(query, (usuario,), fetch=True)
    return resultado[0] if resultado else None


def verificar_respuesta_seguridad(usuario, respuesta):
    """Verifica si la respuesta de seguridad coincide con el usuario."""
    query = """
    SELECT * FROM usuarios
    WHERE usuario = %s AND respuesta_seguridad = %s AND activo = 1
    """
    resultado = ejecutar_consulta(query, (usuario, respuesta), fetch=True)
    return resultado[0] if resultado else None


def cambiar_contrasena(usuario, nueva_contrasena):
    """Cambia la contraseña de un usuario."""
    query = "UPDATE usuarios SET contrasena = %s WHERE usuario = %s"
    return ejecutar_consulta(query, (nueva_contrasena, usuario))


def listar():
    """Retorna todos los usuarios activos."""
    query = """
    SELECT id, nombre, usuario, rol, activo, creado_en
    FROM usuarios
    WHERE activo = 1
    ORDER BY nombre ASC
    """
    return ejecutar_consulta(query, fetch=True)


def eliminar(id):
    """Marca un usuario como inactivo en lugar de eliminarlo."""
    query = "UPDATE usuarios SET activo = 0 WHERE id = %s"
    return ejecutar_consulta(query, (id,))