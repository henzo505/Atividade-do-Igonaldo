from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from app.models.usuario import Usuario

auth_bp=Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome=request.form.get("nome", "").strip()
        senha=request.form.get("senha", "")
        if not nome or not senha:
            flash("Preencha todos os campos.", "danger")
        else:
            usuario=Usuario.autenticar(nome, senha)
            if usuario:
                session.clear()
                session["user_id"]=usuario["id"]
                session["username"]=usuario["nome"]
                resp=make_response(redirect(url_for("main.home")))
                resp.set_cookie("ultimo_usuario", nome, max_age=30*24*60*60)
                return resp
            flash("Usuário ou senha incorretos.", "danger")
    return render_template("login.html", ultimo_usuario=request.cookies.get("ultimo_usuario", ""))

@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome=request.form.get("nome", "").strip()
        senha=request.form.get("senha", "")
        if len(nome)<3 or len(nome)>40 or len(senha)<4:
            flash("Nome deve ter 3 a 40 caracteres e senha ao menos 4.", "danger")
        elif Usuario.buscar_por_nome(nome):
            flash("Esse usuário já existe.", "warning")
        else:
            Usuario(nome, senha).salvar()
            flash("Cadastro realizado! Faça login.", "success")
            return redirect(url_for("auth.login"))
    return render_template("cadastro.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Você saiu do sistema.", "info")
    return redirect(url_for("auth.login"))
