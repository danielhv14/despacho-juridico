# models/nota.py
# Modelo CRUD para tabla notas

from database.connection import ejecutar_consulta


def listar_por_caso(caso_id):
    """Retorna todas las notas de un caso específico."""
    query = """
    SELECT n.id, n.nota, n.creado_en,
           u.nombre AS autor
    FROM notas n
    LEFT JOIN usuarios u ON u.id = n.usuario_id
    WHERE n.caso_id = %s
    ORDER BY n.creado_en DESC
    """
    return ejecutar_consulta(query, (caso_id,), fetch=True)


def crear(caso_id, usuario_id, nota):
    """Crea una nueva nota para un caso."""
    query = """
    INSERT INTO notas (caso_id, usuario_id, nota)
    VALUES (%s, %s, %s)
    """
    return ejecutar_consulta(query, (caso_id, usuario_id, nota))


def eliminar(id):
    """Elimina una nota por su id."""
    query = "DELETE FROM notas WHERE id = %s"
    return ejecutar_consulta(query, (id,))