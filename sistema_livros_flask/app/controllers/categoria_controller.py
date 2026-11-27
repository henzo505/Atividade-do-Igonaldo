from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.categoria import Categoria
from app.utils.auth_middleware import login_required
categoria_bp=Blueprint("categorias", __name__)
@categoria_bp.route("/", methods=["GET","POST"])
@login_required
def listar():
    if request.method=="POST":
        nome=request.form.get("nome","").strip(); descricao=request.form.get("descricao","").strip()
        if not nome or len(nome)>60 or len(descricao)>200:
            flash("Informe nome (até 60 caracteres) e descrição (até 200).", "danger")
        else:
            Categoria(session["user_id"], nome, descricao).salvar()
            flash("Categoria cadastrada.", "success")
            return redirect(url_for("categorias.listar"))
    return render_template("categorias.html", categorias=Categoria.listar(session["user_id"], request.args.get("q","")), busca=request.args.get("q",""))
@categoria_bp.route("/<int:id>/editar", methods=["GET","POST"])
@login_required
def editar(id):
    cat=next((c for c in Categoria.listar(session["user_id"]) if c["id"]==id),None)
    if not cat:
        flash("Categoria não encontrada.", "warning"); return redirect(url_for("categorias.listar"))
    if request.method=="POST":
        nome=request.form.get("nome","").strip(); descricao=request.form.get("descricao","").strip()
        if nome:
            Categoria.atualizar(id, session["user_id"], nome, descricao)
            flash("Categoria atualizada.", "success"); return redirect(url_for("categorias.listar"))
        flash("Nome obrigatório.", "danger")
    return render_template("editar_categoria.html", categoria=cat)
@categoria_bp.route("/<int:id>/excluir", methods=["POST"])
@login_required
def excluir(id):
    if Categoria.excluir(id, session["user_id"]): flash("Categoria excluída.", "success")
    else: flash("Categoria não encontrada.", "warning")
    return redirect(url_for("categorias.listar"))
