<h1 align="center">
  <br>
  BLX - Backend
  <br>
  <h3>A expansão é buscar o ínicio das coisas!</h3>
</h1>

## 💻 Sobre o BLX

Projeto criado na aula de desenvolvimento backend com python do professor Rogério Silva do IFPI, a ideia é ter uma espécie de OLX onde os moradores de um bairro e de uma comunidade vendem seus produtos.

## 🧪 Stacks - Front-End

- [FastAPI](http://fastapitutorial.com/)
- [sqlalchemy](https://docs.sqlalchemy.org)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [alembic](https://alembic.sqlalchemy.org/)

## 🚀 Instruções

```bash
# Clonar este repositório
$ git clone https://github.com/gusdecante/blx-backend.git


# Install dependencies
$ make create_env
$ make install packages

# Ativar o ambiente virtual
$ . ./env/bin/activate

# Desinstalar pacotes
$ make uninstall_packages

# Ativar o ambiente virtual
$ deactivate

# Comando para rodar o server
$ make run_server

# Comando para deletar pacotes
$ make delete_packages

# Comandos alembic, após entrar no ambiente virtual
# revisão e nome desta
$ alembic revision --autogenarate -m "nome da revisão"

# Fazer upgrade do head
$ alembic upgrade head

```
