📚 API de Doação de Livros
Esta é uma API simples feita com Flask e SQLite que permite cadastrar e listar livros doados.

▶️ Como rodar o projeto
Clone o repositório:
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:
pip install -r requirements.txt
Inicie o servidor:
python app.py
A API estará disponível em http://localhost:5000

🔗 Endpoints
➕ POST /doar
Cadastra um novo livro.

Requisição (JSON):

{
  "titulo": "Dom Casmurro",
  "categoria": "Romance",
  "autor": "Machado de Assis",
  "image_url": "https://link-da-imagem.com"
}
Resposta (201):

{
  "mensagem": "Livro cadastrado com sucesso!"
}
📚 GET /livros
Retorna todos os livros cadastrados.

Resposta (200):

[
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "categoria": "Romance",
    "autor": "Machado de Assis",
    "image_url": "https://link-da-imagem.com"
  }
]
❌ DELETE /livros/id
Deletar um Livro.

Resposta (200):

{
    "menssagem": "Livro excluido com sucesso!"
}
🧰 Tecnologias utilizadas
Python 3
Flask
SQLite
Flask-CORS
