from app.db import DatabaseConnection

class Livro:
    def __init__(self, usuario_id, titulo, autor, id=None):
        self.id=id
        self.usuario_id=usuario_id
        self.titulo=titulo.strip()
        self.autor=autor.strip()
    @classmethod
    def criar_tabela(cls):
        with DatabaseConnection() as db:
            db.cursor.execute("""CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE)""")
    def salvar(self):
        with DatabaseConnection() as db:
            db.cursor.execute("INSERT INTO livros(usuario_id, titulo, autor) VALUES (?, ?, ?)",
                (self.usuario_id, self.titulo, self.autor))
            self.id=db.cursor.lastrowid
        return self.id
    @classmethod
    def listar(cls, usuario_id, busca=""):
        with DatabaseConnection() as db:
            db.cursor.execute("""SELECT id, titulo, autor FROM livros
                WHERE usuario_id = ? AND (titulo LIKE ? OR autor LIKE ?) ORDER BY titulo""",
                (usuario_id, f"%{busca}%", f"%{busca}%"))
            return db.cursor.fetchall()
    @classmethod
    def buscar(cls, livro_id, usuario_id):
        with DatabaseConnection() as db:
            db.cursor.execute("SELECT * FROM livros WHERE id = ? AND usuario_id = ?", (livro_id, usuario_id))
            return db.cursor.fetchone()
    @classmethod
    def atualizar(cls, livro_id, usuario_id, titulo, autor):
        with DatabaseConnection() as db:
            db.cursor.execute("UPDATE livros SET titulo = ?, autor = ? WHERE id = ? AND usuario_id = ?",
                (titulo.strip(), autor.strip(), livro_id, usuario_id))
            return db.cursor.rowcount
    @classmethod
    def excluir(cls, livro_id, usuario_id):
        with DatabaseConnection() as db:
            db.cursor.execute("DELETE FROM livros WHERE id = ? AND usuario_id = ?", (livro_id, usuario_id))
            return db.cursor.rowcount
