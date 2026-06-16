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


def actualizar(id, data):
    """Actualiza un cliente existente."""
    query = """
    UPDATE clientes
    SET tipo = %s,
        nombre = %s,
        identificacion = %s,
        email = %s,
        telefono = %s,
        direccion = %s,
        ciudad = %s,
        estado_civil = %s,
        ocupacion = %s,
        observaciones = %s
    WHERE id = %s
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
        id,
    ))


def eliminar(id):
    """Marca un cliente como inactivo en lugar de eliminarlo."""
    query = "UPDATE clientes SET activo = 0 WHERE id = %s"
    return ejecutar_consulta(query, (id,))