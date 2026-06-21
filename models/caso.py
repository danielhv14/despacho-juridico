# models/caso.py
# Modelo CRUD para tabla casos

from database.connection import ejecutar_consulta


def listar(busqueda="", estado=None):
    """Retorna todos los casos con datos de cliente y abogado."""
    query = """
    SELECT c.id, c.numero_caso, c.tipo_caso, c.estado,
           c.prioridad, c.fecha_apertura,
           cl.nombre AS cliente_nombre,
           ab.nombre AS abogado_nombre
    FROM casos c
    JOIN clientes cl ON cl.id = c.cliente_id
    JOIN abogados ab ON ab.id = c.abogado_id
    WHERE c.numero_caso LIKE %s
    ORDER BY c.fecha_apertura DESC
    """
    like = f"%{busqueda}%"
    return ejecutar_consulta(query, (like,), fetch=True)


def obtener(id):
    """Retorna un caso por su id con datos completos."""
    query = """
    SELECT c.*,
           cl.nombre AS cliente_nombre,
           ab.nombre AS abogado_nombre
    FROM casos c
    JOIN clientes cl ON cl.id = c.cliente_id
    JOIN abogados ab ON ab.id = c.abogado_id
    WHERE c.id = %s
    """
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea un nuevo caso en la base de datos."""
    query = """
    INSERT INTO casos
    (numero_caso, cliente_id, abogado_id, tipo_caso,
     materia, descripcion, juzgado, numero_proceso,
     estado, prioridad, fecha_apertura, monto_estimado,
     observaciones)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["numero_caso"],
        data["cliente_id"],
        data["abogado_id"],
        data["tipo_caso"],
        data.get("materia", ""),
        data.get("descripcion", ""),
        data.get("juzgado", ""),
        data.get("numero_proceso", ""),
        data.get("estado", "abierto"),
        data.get("prioridad", "media"),
        data.get("fecha_apertura", None),
        data.get("monto_estimado", 0),
        data.get("observaciones", ""),
    ))


def actualizar(id, data):
    """Actualiza un caso existente."""
    query = """
    UPDATE casos
    SET numero_caso = %s,
        cliente_id = %s,
        abogado_id = %s,
        tipo_caso = %s,
        materia = %s,
        descripcion = %s,
        juzgado = %s,
        numero_proceso = %s,
        estado = %s,
        prioridad = %s,
        fecha_apertura = %s,
        monto_estimado = %s,
        observaciones = %s
    WHERE id = %s
    """
    return ejecutar_consulta(query, (
        data["numero_caso"],
        data["cliente_id"],
        data["abogado_id"],
        data["tipo_caso"],
        data.get("materia", ""),
        data.get("descripcion", ""),
        data.get("juzgado", ""),
        data.get("numero_proceso", ""),
        data.get("estado", "abierto"),
        data.get("prioridad", "media"),
        data.get("fecha_apertura", None),
        data.get("monto_estimado", 0),
        data.get("observaciones", ""),
        id,
    ))


def eliminar(id):
    """Elimina un caso por su id."""
    query = "DELETE FROM casos WHERE id = %s"
    return ejecutar_consulta(query, (id,))
