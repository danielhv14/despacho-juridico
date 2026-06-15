# database/connection.py
# Módulo de conexión a MySQL

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host":     "localhost",
    "port":     3306,
    "user":     "root",
    "password": "",
    "database": "despacho_juridico",
    "charset":  "utf8mb4",
}

def get_connection():
    """Crea y retorna una conexión a MySQL."""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except Error as e:
        raise ConnectionError(f"No se pudo conectar a MySQL: {e}")

def test_conexion():
    """Prueba si la conexión a MySQL funciona."""
    try:
        conexion = get_connection()
        conexion.close()
        return True
    except:
        return False

def ejecutar_consulta(query, params=None, fetch=False):
    """
    Ejecuta una consulta SQL.
    - fetch=False → INSERT, UPDATE, DELETE
    - fetch=True  → SELECT
    """
    conexion = get_connection()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        conexion.commit()
        return cursor.lastrowid if cursor.lastrowid else cursor.rowcount
    except Error as e:
        conexion.rollback()
        raise RuntimeError(f"Error en consulta: {e}")
    finally:
        cursor.close()
        conexion.close()