# Trilha Dev: Início de Jornada

Repositório dedicado à construção e disponibilização do curso Trilha Dev: Início de Jornada, que tem como objetivo passar o básico para trabalhar em um projeto de desenvolvimento.
O projeto foi criado utilizando a ferramenta [MkDocs](https://www.mkdocs.org/) e  [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

# Setup

## Requisitos

Certifique-se de ter instalado:

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/)

## Configuração Inicial

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:

   ```sh
   git clone git@github.com:splor-mg/trilha-dev.git
   cd handbook
   ```

1. Instale as dependências do projeto com Poetry:

   ```sh
   poetry install
   ```

1. Inicie o servidor de desenvolvimento:

   ```sh
   poetry run mkdocs serve
   ```

O site estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

