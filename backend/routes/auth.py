#!/bin/python3
from flask import Blueprint, request, jsonify
import json

""""
Código de retorno HTTP e seus significados:
https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status
"""

# React irá me retornar os dados de e-mail e senha no formato JSON


# Crie um objeto Blueprint chamado auth, associado ao módulo atual
auth_bp = Blueprint('auth', __name__)
 

usuarios = "data/usuarios.json"
@auth_bp.route('/login', methods=['POST'])
def login():
    

    ###############################
    #     VERIFICAÇÃO NO LOGIN    #
    ###############################

    # pegar dados
    dados = request.get_json()


    # pega os dados digitados
    email = dados.get("email")
    senha = dados.get("senha")


    # campos preenchidos?
    if not email or not senha:
        return jsonify({
            "erro": "Email e/ou senha não preenchidos"
        })
    
    # abre nosso "BD" de usuários
    with open(usuarios, "r") as file:
        usuarios_json = json.load(file) # transforma nosso JSON em uma lista python

    ###############################
    #       SUCESSO NO LOGIN      #
    ###############################
    for usuario in usuarios_json:
        if usuario["email"] == email and usuario["senha"] == senha:
            return jsonify({
                "sucesso": "Login realizado",
                "usuario": { # naõ podemos passar o objeto "usuario" direto, por conta que irá retornar a senha também
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "email": usuario["email"]
                }
            }), 200

    return jsonify({
        "erro": "Credenciais inválidas"
    }), 409

@auth_bp.route('/register', methods=['POST'])
def register():
    dados = request.get_json()

    nome = dados.get("nome") # Identificação 
    email = dados.get("email")
    senha = dados.get("senha")

    ###############################
    #   VERIFICAÇÃO NO CADASTRO   #
    ###############################

    # campos preenchidos?
    if not email or not senha:
        return jsonify({
            "erro": "Email e senha obrigatórios para cadastro"
        })

    # abre nosso "BD" de usuários
    with open(usuarios, "r") as file:
        usuarios_json = json.load(file) # transforma nosso JSON em uma lista python


    # verificação de usuário já cadastrado
    for usuario in usuarios_json:
        if(usuario["email"] == email):
            return jsonify({
                "erro": f"E-mail {usuario["email"]} já cadastrado"
                }), 409 

    ###############################
    #    SUCESSO NO CADASTRO   #
    ###############################
    
    # cria um novo usuário pra ser adicionado na nossa lista de usuários
    novo_id = len(usuarios) + 1
    novo_usuario = {
        "id": novo_id,
        "nome": nome,
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
        "mensagem": f"Usuário {novo_usuario["nome"]} adicionado com sucesso!"
    }), 200 