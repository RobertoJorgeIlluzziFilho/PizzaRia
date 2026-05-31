#!/bin/python3
from flask import Blueprint, request, jsonify

# React irá me retornar os dados de e-mail e senha no formato JSON


# Crie um objeto Blueprint chamado auth, associado ao módulo atual
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return "Estou acessando a rota https://pizzaria/login"


print(__name__)
