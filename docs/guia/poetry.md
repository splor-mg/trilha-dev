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
poetry add <nome-do-pacote>
```

Remove uma dependência:
```bash
poetry remove <nome-do-pacote>
```

Ativa o ambiente virtual do projeto:
```bash
poetry env activate
```
!!! warning "Atenção"
    Esse comando apenas mostra o comando de ativação do ambiente virtual.

!!! info "Linux/macOS"
    No Linux/macOS (bash/zsh), normalmente você executa assim:
    `eval $(poetry env activate)`

---

## **MkDocs**

Inicia o servidor local com preview em tempo real:
```bash
mkdocs serve
```

!!! info "Servidor local"
    Após rodar o comando, acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador.


Gera o site estático na pasta `site/`:
```bash
mkdocs build
```
