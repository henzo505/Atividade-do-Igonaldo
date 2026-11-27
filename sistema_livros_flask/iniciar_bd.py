from app.models.usuario import Usuario
from app.models.livro import Livro
from app.models.categoria import Categoria

def iniciar():
    Usuario.criar_tabela()
    Livro.criar_tabela()
    Categoria.criar_tabela()
    # Usuário de teste
    if not Usuario.buscar_por_nome("henzo"):
        Usuario("henzo", "1234").salvar()
    if not Usuario.buscar_por_nome("teste"):
        Usuario("teste", "senha123").salvar()
    # Dados iniciais de cada usuário são adicionados após cadastro, via páginas de gerenciamento.
    print("Banco inicializado.")

if __name__ == "__main__":
    iniciar()
