from flask import Flask, redirect, url_for, session, request
from controllers.auth_controller import auth_bp
from models.database import init_db

app = Flask(__name__, template_folder="views")
app.config["SECRET_KEY"] = "troque-esta-chave-em-um-projeto-real"

# Blueprint responsável pelas rotas de login e logout
app.register_blueprint(auth_bp)

# Middleware simples: protege as páginas que exigem login
@app.before_request
def verificar_login():
    rotas_publicas = ["auth.login", "static"]
    if request.endpoint is None:
        return None
    if request.endpoint in rotas_publicas:
        return None
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    return None

@app.route("/")
def inicio():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    from flask import render_template
    return render_template("home.html", usuario=session["usuario"])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
