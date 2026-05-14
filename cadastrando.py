from flask import Flask, request, jsonify

#Variável app -> Indicando que o sistema será via web
app = Flask(__name__)

#Lista que vai armazenar os usuarios
usuarios = []

# Endpoint inicia
# Quando acessar
@app.route("/")
def inicio():

    return "API Funcionando"

# Estamos usando o método POST - Criar dados
@app.route("/usuarios", methods=["POST"])
def cadastrar():

# request -> recebe dads enviados pelo cliente
# get -> Buscar | json -> formato do arquivo
    dados = request.get_json()
# Criará um usuário novo
# len(usuários) +1 gera o id automático
# Se a lista estiver vazia
# len = 0
# id = 1

    usuarios = {
        "id": len(usuarios)+1,
        "nome": dados["nome"]
    }


# Adicionar o usuário na lista
    usuarios.append(usuarios)

# Vai retornar o usuário criado
# jsonify -> Transforma resposta em python em JSON
# 201 = Criado com sucesso

    return jsonify(usuarios), 201

# Rodando o sitema
if __name__ == "__main__":
    app.run(debug=True)