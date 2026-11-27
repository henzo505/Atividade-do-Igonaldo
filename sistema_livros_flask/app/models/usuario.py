from werkzeug.security import generate_password_hash, check_password_hash
from app.db import DatabaseConnection

class Usuario:
    def __init__(self, nome, senha, id=None):
        self.id=id
        self.nome=nome.strip()
        self.senha=senha
    @classmethod
    def criar_tabela(cls):
        with DatabaseConnection() as db:
            db.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL)""")
    def salvar(self):
        with DatabaseConnection() as db:
            db.cursor.execute("INSERT INTO usuarios(nome, senha) VALUES (?, ?)",
                (self.nome, generate_password_hash(self.senha)))
            self.id=db.cursor.lastrowid
        return self.id
    @classmethod
    def buscar_por_nome(cls, nome):
        with DatabaseConnection() as db:
            db.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
            return db.cursor.fetchone()
    @classmethod
    def buscar_por_id(cls, user_id):
        with DatabaseConnection() as db:
            db.cursor.execute("SELECT id, nome FROM usuarios WHERE id = ?", (user_id,))
            return db.cursor.fetchone()
    @classmethod
    def autenticar(cls, nome, senha):
        user=cls.buscar_por_nome(nome)
        if user and check_password_hash(user["senha"], senha):
            return user
        return None
