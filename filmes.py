from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista que funcionará como nosso banco de dados temporário
filmes = [
    {
        "id": 1,
        "nome": "Interestelar",
        "categorias": ["Ficção Científica", "Drama"],
        "duracao": 169,
        "idade": 12,
        "classificacao": "Não recomendado para menores de 12 anos",
        "avaliacao": 9.0
    }
]


# ==========================================
# GET - Buscar todos os filmes
# ==========================================

@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(filmes), 200


# ==========================================
# GET - Buscar um filme pelo ID
# ==========================================

@app.route("/filmes/<int:id>", methods=["GET"])
def buscar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            return jsonify(filme), 200

    return jsonify({
        "erro": "Filme não encontrado"
    }), 404


# ==========================================
# POST - Cadastrar um novo filme
# ==========================================

@app.route("/filmes", methods=["POST"])
def cadastrar_filme():

    dados = request.get_json()

    novo_filme = {
        "id": len(filmes) + 1,
        "nome": dados["nome"],
        "categorias": dados["categorias"],
        "duracao": dados["duracao"],
        "idade": dados["idade"],
        "classificacao": dados["classificacao"],
        "avaliacao": dados["avaliacao"]
    }

    filmes.append(novo_filme)

    return jsonify({
        "mensagem": "Filme cadastrado com sucesso!",
        "filme": novo_filme
    }), 201


# ==========================================
# PUT - Atualizar um filme
# ==========================================

@app.route("/filmes/<int:id>", methods=["PUT"])
def atualizar_filme(id):

    dados = request.get_json()

    for filme in filmes:
        if filme["id"] == id:

            filme["nome"] = dados["nome"]
            filme["categorias"] = dados["categorias"]
            filme["duracao"] = dados["duracao"]
            filme["idade"] = dados["idade"]
            filme["classificacao"] = dados["classificacao"]
            filme["avaliacao"] = dados["avaliacao"]

            return jsonify({
                "mensagem": "Filme atualizado com sucesso!",
                "filme": filme
            }), 200

    return jsonify({
        "erro": "Filme não encontrado"
    }), 404


# ==========================================
# DELETE - Remover um filme
# ==========================================

@app.route("/filmes/<int:id>", methods=["DELETE"])
def deletar_filme(id):

    for filme in filmes:
        if filme["id"] == id:

            filmes.remove(filme)

            return jsonify({
                "mensagem": "Filme removido com sucesso!",
                "filme": filme
            }), 200

    return jsonify({
        "erro": "Filme não encontrado"
    }), 404


# ==========================================
# Iniciar o servidor
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)