from flask import Flask, jsonify, abort

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell"},
    {"id": 4, "titulo": "Capitães da Areia", "autor": "Jorge Amado"},
]


@app.route("/livros")
def listar_livros():
    return jsonify(livros)

@app.route("/livros/<int:livro_id>")
def detalhar_livro(livro_id):
    for livro in livros:
        if livro["id"] == livro_id:
            return jsonify(livro)
    abort(404, description="Livro não encontrado")


@app.errorhandler(404)
def erro_404(e):
    return jsonify({"erro": "Recurso não encontrado", "detalhe": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)
