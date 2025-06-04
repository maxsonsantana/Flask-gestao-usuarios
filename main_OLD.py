from flask import Flask, url_for, render_template

#Inicialicação precisa estar no início do arquivo
app = Flask(__name__) # Create a Flask application instance

#rotas
@app.route('/')
def home():
    #return f"<a href='{ url_for('sobre')}'>Sobre</a>"
    titulo = "Página Inicial"
    usuarios = [{
        'nome': 'João',
        'ativo': True
    }, {   
        'nome': 'Maria',
        'ativo': False
    }, {
        'nome': 'José',
        'ativo': True
    }]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)#primeiro parâmetro é o nome do template(variavel de contexto), os outros são variáveis que serão passadas para o template

@app.route('/sobre')
def sobre():
    return "<h1>Sobre a Aplicação</h1><p>Esta é uma aplicação de exemplo para gestão de usuários.</p>"

#Execução tem que estar no final do arquivo
app.run(debug=True) # Run the application in debug mode(this will reload the server on code changes)



