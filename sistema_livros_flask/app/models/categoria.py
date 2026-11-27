from app.db import DatabaseConnection

class Categoria:
    def __init__(self, usuario_id, nome, descricao="", id=None):
        self.id=id
        self.usuario_id=usuario_id
        self.nome=nome.strip()
        self.descricao=descricao.strip()
    @classmethod
    def criar_tabela(cls):
        with DatabaseConnection() as db:
            db.cursor.execute("""CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                descricao TEXT,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE)""")
    def salvar(self):
        with DatabaseConnection() as db:
            db.cursor.execute("INSERT INTO categorias(usuario_id, nome, descricao) VALUES (?, ?, ?)",
                (self.usuario_id, self.nome, self.descricao))
            self.id=db.cursor.lastrowid
        return self.id
    @classmethod
    def listar(cls, usuario_id, busca=""):
        with DatabaseConnection() as db:
            db.cursor.execute("""SELECT id, nome, descricao FROM categorias
                WHERE usuario_id = ? AND nome LIKE ? ORDER BY nome""",
                (usuario_id, f"%{busca}%"))
            return db.cursor.fetchall()
    @classmethod
    def atualizar(cls, categoria_id, usuario_id, nome, descricao):
        with DatabaseConnection() as db:
            db.cursor.execute("UPDATE categorias SET nome = ?, descricao = ? WHERE id = ? AND usuario_id = ?",
                (nome.strip(), descricao.strip(), categoria_id, usuario_id))
            return db.cursor.rowcount
    @classmethod
    def excluir(cls, categoria_id, usuario_id):
        with DatabaseConnection() as db:
            db.cursor.execute("DELETE FROM categorias WHERE id = ? AND usuario_id = ?", (categoria_id, usuario_id))
            return db.cursor.rowcount
