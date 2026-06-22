# models/audiencia.py
# Modelo CRUD para tabla audiencias

from database.connection import ejecutar_consulta


def listar_por_caso(caso_id):
    """Retorna todas las audiencias de un caso específico."""
    query = """
    SELECT id, tipo, fecha_hora, lugar,
           descripcion, resultado, estado
    FROM audiencias
    WHERE caso_id = %s
    ORDER BY fecha_hora DESC
    """
    return ejecutar_consulta(query, (caso_id,), fetch=True)


def obtener(id):
    """Retorna una audiencia por su id."""
    query = "SELECT * FROM audiencias WHERE id = %s"
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea una nueva audiencia en la base de datos."""
    query = """
    INSERT INTO audiencias
    (caso_id, tipo, fecha_hora, lugar, descripcion, estado)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["caso_id"],
        data.get("tipo", ""),
        data["fecha_hora"],
        data.get("lugar", ""),
        data.get("descripcion", ""),
        data.get("estado", "pendiente"),
    ))


def actualizar(id, data):
    """Actualiza una audiencia existente."""
    query = """
    UPDATE audiencias
    SET tipo = %s,
        fecha_hora = %s,
        lugar = %s,
        descripcion = %s,
        resultado = %s,
        estado = %s
    WHERE id = %s
    """
    return ejecutar_consulta(query, (
        data.get("tipo", ""),
        data["fecha_hora"],
        data.get("lugar", ""),
        data.get("descripcion", ""),
        data.get("resultado", ""),
        data.get("estado", "pendiente"),
        id,
    ))


def eliminar(id):
    """Elimina una audiencia por su id."""
    query = "DELETE FROM audiencias WHERE id = %s"
    return ejecutar_consulta(query, (id,))

