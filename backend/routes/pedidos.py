#!/bin/python3

from flask import Blueprint,  jsonify

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/pedidos', methods=["GET"])
def listar_pedidos():
    return "pedidos sendo listados"
