---
title: Poetry e MkDocs
---

# :simple-python: Poetry e MkDocs

[← Voltar ao guia](../)

---

## **Poetry**

Gerenciador de dependências e ambientes virtuais usado na Trilha Dev.

Instala o Poetry (feito uma única vez):
```bash
pipx install poetry
```

Instala as dependências listadas no `pyproject.toml`:
```bash
poetry install
```

!!! tip "Dica"
    Sempre rode `poetry install` ao clonar um repositório pela primeira vez.

Adiciona uma nova dependência ao projeto:
```bash
poetry add nome-do-pacote
```

Remove uma dependência:
```bash
poetry remove nome-do-pacote
```

Ativa o ambiente virtual do projeto:
```bash
poetry shell
```

---

## **MkDocs com Poetry**

Inicia o servidor local com preview em tempo real:
```bash
poetry run mkdocs serve
```

!!! info "Servidor local"
    Após rodar o comando, acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador.

Gera o site estático na pasta `site/`:
```bash
poetry run mkdocs build
```
