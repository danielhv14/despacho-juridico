# models/abogado.py
# Modelo CRUD para tabla abogados

from database.connection import ejecutar_consulta


def listar(busqueda=""):
    """Retorna todos los abogados activos."""
    query = """
    SELECT id, nombre, cedula, matricula,
           especialidad, email, telefono
    FROM abogados
    WHERE activo = 1
    AND (nombre LIKE %s OR cedula LIKE %s)
    ORDER BY nombre ASC
    """
    like = f"%{busqueda}%"
    return ejecutar_consulta(query, (like, like), fetch=True)


def obtener(id):
    """Retorna un abogado por su id."""
    query = "SELECT * FROM abogados WHERE id = %s"
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea un nuevo abogado en la base de datos."""
    query = """
    INSERT INTO abogados
    (nombre, cedula, matricula, especialidad, email, telefono)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["nombre"],
        data["cedula"],
        data.get("matricula", ""),
        data.get("especialidad", ""),
        data.get("email", ""),
        data.get("telefono", ""),
    ))


def actualizar(id, data):
    """Actualiza un abogado existente."""
    query = """
    UPDATE abogados
    SET nombre = %s,
        cedula = %s,
        matricula = %s,
        especialidad = %s,
        email = %s,
        telefono = %s
    WHERE id = %s
    """
    return ejecutar_consulta(query, (
        data["nombre"],
        data["cedula"],
        data.get("matricula", ""),
        data.get("especialidad", ""),
        data.get("email", ""),
        data.get("telefono", ""),
        id,
    ))