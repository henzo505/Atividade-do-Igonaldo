# Sistema de Livros — Projeto Final Flask

Aplicação web para gerenciamento de biblioteca pessoal. Feita com Flask, Jinja2 e SQLite3, sem ORM.

## Executar
1. `python -m venv venv`
2. Ativar ambiente virtual.
3. `pip install -r requirements.txt`
4. `python iniciar_bd.py`
5. `python run.py`
6. Acesse http://127.0.0.1:5000/login

## Usuários de teste
- `henzo` / `1234`
- `teste` / `senha123`

Senhas armazenadas com hash Werkzeug.

## Entidades
- Usuários
- Livros
- Categorias

## Funcionalidades
Cadastro/login/logout, cookie de último usuário, gerenciamento de livros e categorias (cadastro, listagem, edição, exclusão, busca), validação, flash messages, middleware de login, 404 personalizado, SQL parametrizado e filtro por usuário.

## Estrutura
`app/models`: classes e SQL; `app/controllers`: Blueprints/rotas; `app/views`: Jinja2 com herança; `app/utils`: middleware; `app/db.py`: DatabaseConnection; `iniciar_bd.py`: criação das tabelas e usuários iniciais.
