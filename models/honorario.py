# models/honorario.py
# Modelo CRUD para tabla honorarios

from database.connection import ejecutar_consulta


def listar(busqueda=""):
    """Retorna todos los honorarios con datos de caso y cliente."""
    query = """
    SELECT h.id, h.concepto, h.monto, h.fecha_emision,
           h.fecha_pago, h.estado,
           c.numero_caso,
           cl.nombre AS cliente_nombre
    FROM honorarios h
    JOIN casos c ON c.id = h.caso_id
    JOIN clientes cl ON cl.id = h.cliente_id
    WHERE cl.nombre LIKE %s
    ORDER BY h.fecha_emision DESC
    """
    like = f"%{busqueda}%"
    return ejecutar_consulta(query, (like,), fetch=True)


def obtener(id):
    """Retorna un honorario por su id."""
    query = "SELECT * FROM honorarios WHERE id = %s"
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea un nuevo honorario en la base de datos."""
    query = """
    INSERT INTO honorarios
    (caso_id, cliente_id, concepto, monto,
     fecha_emision, estado, metodo_pago, observaciones)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["caso_id"],
        data["cliente_id"],
        data["concepto"],
        data["monto"],
        data.get("fecha_emision", None),
        data.get("estado", "pendiente"),
        data.get("metodo_pago", ""),
        data.get("observaciones", ""),
    ))


def actualizar_estado(id, estado, fecha_pago=None):
    """Actualiza el estado de un honorario."""
    query = """
    UPDATE honorarios
    SET estado = %s,
        fecha_pago = %s
    WHERE id = %s
    """
    return ejecutar_consulta(query, (estado, fecha_pago, id))


def eliminar(id):
    """Elimina un honorario por su id."""
    query = "DELETE FROM honorarios WHERE id = %s"
    return ejecutar_consulta(query, (id,))