from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    json_data = request.get_json()
    user = json_data.get('user')
    password = json_data.get('password')
    codRes, menRes, accion = inicializarVariables(user, password)
    response = {
        'codRes': codRes,
        'menRes': menRes,
        'accion': accion
    }
    return jsonify(response)

def inicializarVariables(user, password):
    user_local = 'KiaraTorales'
    password_local = 'unida123'
    codRes = 'SIN ERROR'
    menRes = 'OK'
    accion = ''
    try:
        print("Verificar login")
        if password == password_local and user == user_local:
            print("Login correcto")
            accion = 'Success'
        else:
            print("Login incorrecto")
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
            accion = 'Usuario o password incorrecto'
    except Exception as e:
        print("Error " + str(e))
        codRes = 'ERROR'
        menRes = 'Msg : ' + str(e)
        accion = 'Error interno'
    return codRes, menRes, accion
