from functools import wraps
from flask import session, redirect, url_for, flash, g
from app.models.usuario import Usuario

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id=session.get("user_id")
        usuario=Usuario.buscar_por_id(user_id) if user_id else None
        if not usuario:
            session.clear()
            flash("Faça login para acessar esta página.", "warning")
            return redirect(url_for("auth.login"))
        g.usuario=usuario
        return func(*args, **kwargs)
    return wrapper
