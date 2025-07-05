from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamarServicioSet():
    json_data = request.get_json()
    ci = json_data.get('ci') if json_data else None
    codRes, menRes, accion = verificarCi(ci)
    
    response = {
        'codRes': codRes,
        'menRes': menRes,
        'accion': accion
    }
    return jsonify(response)

def verificarCi(ci):
    codRes = 'SIN ERROR'
    menRes = 'OK'
    accion = ''

    try:
        if not ci:
            codRes = 'ERROR'
            menRes = 'Debe enviar la cédula (ci)'
            accion = 'Falta parámetro'
        else:
            # Aquí puedes poner tu lógica real de verificación
            # Por ahora simula un fallo
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
            accion = 'Usuario o password incorrecto'
    except Exception as e:
        print("Error: " + str(e))
        codRes = 'ERROR'
        menRes = f'Msg: {str(e)}'
        accion = 'Error interno'

    return codRes, menRes, accion
