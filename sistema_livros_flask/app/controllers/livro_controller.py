from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.livro import Livro
from app.utils.auth_middleware import login_required
livro_bp=Blueprint("livros", __name__)

@livro_bp.route("/", methods=["GET", "POST"])
@login_required
def listar():
    if request.method=="POST":
        titulo=request.form.get("titulo","").strip()
        autor=request.form.get("autor","").strip()
        if not titulo or not autor or len(titulo)>120 or len(autor)>80:
            flash("Informe título e autor (limites: 120 e 80 caracteres).", "danger")
        else:
            Livro(session["user_id"], titulo, autor).salvar()
            flash("Livro cadastrado!", "success")
            return redirect(url_for("livros.listar"))
    return render_template("livros.html", livros=Livro.listar(session["user_id"], request.args.get("q","")), busca=request.args.get("q",""))

@livro_bp.route("/<int:id>/editar", methods=["GET","POST"])
@login_required
def editar(id):
    livro=Livro.buscar(id, session["user_id"])
    if not livro:
        flash("Livro não encontrado.", "warning")
        return redirect(url_for("livros.listar"))
    if request.method=="POST":
        titulo=request.form.get("titulo","").strip(); autor=request.form.get("autor","").strip()
        if titulo and autor:
            Livro.atualizar(id, session["user_id"], titulo, autor)
            flash("Livro atualizado.", "success")
            return redirect(url_for("livros.listar"))
        flash("Preencha os campos.", "danger")
    return render_template("editar_livro.html", livro=livro)

@livro_bp.route("/<int:id>/excluir", methods=["POST"])
@login_required
def excluir(id):
    if Livro.excluir(id, session["user_id"]):
        flash("Livro excluído.", "success")
    else: flash("Livro não encontrado.", "warning")
    return redirect(url_for("livros.listar"))
