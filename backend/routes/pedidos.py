#!/bin/python3

from flask import Blueprint,  jsonify

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/pedidos', methods=["GET"])
def listar_pedidos():
    return "pedidos sendo listados"

# Vou precisar criar o pedido no usuário logado atualmente
@pedidos_bp.route('/pedidos', methods=["POST"])
def criar_pedidos():
    return
@pedidos_bp.route('/pedidos', methods=["DELETE"])
def remover_pedidos():
    return

