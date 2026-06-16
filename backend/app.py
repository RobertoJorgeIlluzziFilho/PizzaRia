#!/bin/python3

# Mostrando a existências dos BluesPrints
from flask import Flask
from routes.auth import auth_bp
from routes.pedidos import pedidos_bp
from routes.user import user_bp

# Inicializa nosso objeto princial flask
app = Flask(__name__)

# Registrando as rotas pro app
app.register_blueprint(auth_bp)
app.register_blueprint(pedidos_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True) # n esquecer de desativar na aplicação real
