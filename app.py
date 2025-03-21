from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para inicializar o banco de dados
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                imagem_url TEXT NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        print("Banco de dados inicializado com sucesso!")

# Inicializa o banco de dados
init_db()

# Página inicial
@app.route('/')
def home_page():
    return '<h2>Doe um livro e espalhe conhecimento.</h2>'

# Rota para cadastrar um novo livro
@app.route('/doar', methods=['POST'])
def doar():
    dados = request.get_json()
    titulo = dados.get('titulo')
    categoria = dados.get('categoria')
    autor = dados.get('autor')
    imagem_url = dados.get('imagem_url')

    if not all([titulo, categoria, autor, imagem_url]):
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, categoria, autor, imagem_url)
            VALUES (?, ?, ?, ?)
        """, (titulo, categoria, autor, imagem_url))
        conn.commit()
        cursor.close()

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# Rota para listar todos os livros cadastrados
@app.route('/livros', methods=['GET'])
def listar_livros():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        cursor.close()

    livros_formatados = [
        {"id": livro[0], "titulo": livro[1], "categoria": livro[2], "autor": livro[3], "imagem_url": livro[4]}
        for livro in livros
    ]

    return jsonify(livros_formatados), 200

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
