from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/usuario', methods=["POST"])
def criar_usuario():


    # get para ler os dados
    dados = request.get_json()

    # exibe os dados no formato json
    # flask trata o JSON como um dicionário (dict) -> estrutura semelhante

    # Flask transforma o dicionário em JSON antes de retornar
    return jsonify({
        "mensagem": f"Seja vem vindo(a) {dados["nome"]}",
        "dados_recebidos": dados
    })

    

if __name__ == '__main__':
    app.run(debug=True)



