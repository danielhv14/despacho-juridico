# models/documento.py
# Modelo CRUD para tabla documentos

from database.connection import ejecutar_consulta


def listar_por_caso(caso_id):
    """Retorna todos los documentos de un caso específico."""
    query = """
    SELECT id, nombre, tipo, ruta_archivo,
           descripcion, subido_en
    FROM documentos
    WHERE caso_id = %s
    ORDER BY subido_en DESC
    """
    return ejecutar_consulta(query, (caso_id,), fetch=True)


def obtener(id):
    """Retorna un documento por su id."""
    query = "SELECT * FROM documentos WHERE id = %s"
    resultado = ejecutar_consulta(query, (id,), fetch=True)
    return resultado[0] if resultado else None


def crear(data):
    """Crea un nuevo documento en la base de datos."""
    query = """
    INSERT INTO documentos
    (caso_id, nombre, tipo, ruta_archivo,
     descripcion, subido_por)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    return ejecutar_consulta(query, (
        data["caso_id"],
        data["nombre"],
        data.get("tipo", ""),
        data.get("ruta_archivo", ""),
        data.get("descripcion", ""),
        data.get("subido_por", None),
    ))


def eliminar(id):
    """Elimina un documento por su id."""
    query = "DELETE FROM documentos WHERE id = %s"
    return ejecutar_consulta(query, (id,))