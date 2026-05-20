from flask import Flask, json, jsonify, request

# Objeto app
app = Flask(__name__)

# Decorator pra rota padrão 
@app.route("/")
def main():
    return "<p> Bem vindo a página inicial! <p>"

# Apenas POST, pois no react moderno nem existe GET /login
# React renderiza a tela, então nosso flask vira somente API 
@app.route("/login", methods=["POST"])
def login():

    # recebe a resposta em JSON
    dados = request.json

    # recebe o atributo inserido
    email = dados['email']
    password = dados['password']

    # validação
    if(valid_login(email, password)):
        return log_the_user(email)


# Decorator pra rota 'robots.txt'
@app.route("/robots.txt")
def robot():
    return 'key.txt'

#######################
#       FUNÇÕES
#######################
def valid_login(email, password):
    # faça a leitura do nosso "Banco de dados"
    with open("/data/usuarios.json", "r") as arquivo:
        users = json.load(arquivo)
    for usuario in users:
        if(usuario['email'] == email and usuario['password'] == password):
            pass 
        
def log_the_user(username):
    pass # conta do usuário 
if __name__ == '__main__':
    app.run(debug=False)