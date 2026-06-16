# models/cliente.py
# Modelo CRUD para tabla clientes

from database.connection import ejecutar_consulta


def listar(busqueda=""):
    """Retorna todos los clientes activos."""
    query = """
    SELECT  id, tipo, nombre, identificacion,
            email, telefono, ciudad
    FROM clientes
    WHERE activo = 1
    AND (nombre LIKE %s OR identificacion LIKE %s)
    ORDER BY nombre ASC
    """
    like = f"%{busqueda}%"
    return ejecutar_consulta(query, (like, like), fetch=True)


def obtener(id):
    """Retorna un cliente por su id."""
    query = "SELECT * FROM clientes WHERE id = %s"
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea un nuevo cliente en la base de datos."""
    query = """
    INSERT INTO clientes
    (tipo, nombre, identificacion, email,
    telefono, direccion, ciudad,
    estado_civil, ocupacion, observaciones)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["tipo"],
        data["nombre"],
        data["identificacion"],
        data.get("email", ""),
        data.get("telefono", ""),
        data.get("direccion", ""),
        data.get("ciudad", ""),
        data.get("estado_civil", ""),
        data.get("ocupacion", ""),
        data.get("observaciones", ""),
))

