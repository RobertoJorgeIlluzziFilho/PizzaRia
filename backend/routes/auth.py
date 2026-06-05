#!/bin/python3
from flask import Blueprint, request, jsonify
import json


# React irá me retornar os dados de e-mail e senha no formato JSON


# Crie um objeto Blueprint chamado auth, associado ao módulo atual
auth_bp = Blueprint('auth', __name__)
 

usuarios = "data/usuarios.json"
@auth_bp.route('/login', methods=['POST'])
def login():
    
    # pegar dados
    dados = request.get_json()


    # pega os dados digitados
    email = dados["email"]
    senha = dados["senha"]


    # campos preenchidos?
    if not email or not senha:
        return jsonify({
            "erro": "Email e/ou senha não preenchidos"
        })
    
    # abre nosso "BD" de usuários
    with open(usuarios, "r") as file:
        usuarios_json = json.load(file) # transforma nosso JSON em uma lista python

    for usuario in usuarios_json:
        if usuario["email"] == email and usuario["senha"] == senha:
            return jsonify({
                "sucesso": "Login realizado"
            }), 200

    return jsonify({
        "erro": "Credenciais inválidas"
    })

@auth_bp.route('/register', methods=['POST'])
def register():
    dados = request.get_json()

    email = dados["email"]
    senha = dados["senha"]

    # campos preenchidos?
    if not email or not senha:
        return jsonify({
            "erro": "Email e senha obrigatórios para cadastro"
        })

    # abre nosso "BD" de usuários
    with open(usuarios, "r") as file:
        usuarios_json = json.load(file) # transforma nosso JSON em uma lista python

    # cria um novo usuário pra ser adicionado na nossa lista de usuários
    novo_usuario = {
        "email": email,
        "senha": senha
    }

    # adicionar usuário no arquivo
    usuarios_json.append(novo_usuario)

    # salvar no arquivo
    with open(usuarios, "w") as file:
        # dump(): Converte de volta para lista python -> json puro
        json.dump(usuarios_json, file)

    return jsonify({
        "mensagem": "Usuário adicionado com sucesso!"
    }), 200