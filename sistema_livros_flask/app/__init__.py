import os
from flask import Flask, g
from app.controllers.auth_controller import auth_bp
from app.controllers.main_controller import main_bp
from app.controllers.livro_controller import livro_bp
from app.controllers.categoria_controller import categoria_bp

def create_app():
    app = Flask(__name__, template_folder="views")
    app.secret_key = os.environ.get("SECRET_KEY", "chave-didatica-trocar")
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(livro_bp, url_prefix="/livros")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")

    @app.errorhandler(404)
    def pagina_nao_encontrada(error):
        return "Página não encontrada (404).", 404

    return app
