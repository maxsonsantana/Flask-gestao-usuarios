from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes =CLIENTES, pagina='Lista de Clientes')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    novo_usuario = {
        'id': len(CLIENTES) + 1,
        'nome': data.get('nome'),
        'email': data.get('email')
    }

    CLIENTES.append(novo_usuario)
    return render_template('lista_clientes.html', cliente=novo_usuario, pagina='Lista de Clientes')

@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    pass # Implementar a lógica para obter um cliente específico

@cliente_route.route('/new')
def formulario_cliente():
    return render_template('form_clientes.html', pagina='Formulario de Clientes')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('templates/detalhe_clientes.html', pagina='Detalhe de Clientes')

@cliente_route.route('/<int:cliente_id>/edit')
def editar_cliente(cliente_id):
    return render_template('templates/form_edit_clientes.html', pagina='Edicao de Clientes')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass # Implementar a lógica para atualizar um cliente específico

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass # Implementar a lógica para deletar um cliente específico