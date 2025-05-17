from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login = Blueprint('login', __name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'Unida',
    'password': 'unida123',
    'database': 'jaguarete'             
}

def verificar_credenciales(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None
    accion = ''

    try:
        print("Verificar login")

        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        # Ejecutar la consulta SQL
        query = "SELECT username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))

        # Obtener el resultado
        result = cursor.fetchone()


    except Exception as e:
        print(f"Error al verificar credenciales: {e}")
        codRes = 'ERROR'
        menRes = 'Error interno en el servidor'
        accion = 'Error'


    return codRes, menRes, accion, usuario
