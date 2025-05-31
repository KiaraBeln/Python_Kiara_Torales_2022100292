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
        'accion': accion,
        'ci': ci
    }
    return jsonify(response)

def verificarCi(ci):
    try:
        if ci == '5574717':
            return 'Success', 'OK', 'SIN_ERROR'
        else:
            return 'ERROR', 'Error cliente', 'Cliente no esta '
    except Exception as e:
       print(f"Error credenciales: {e}")


