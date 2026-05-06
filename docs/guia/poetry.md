---
title: Poetry e MkDocs
---

# Poetry e MkDocs

[← Voltar ao guia](../)

---

## Poetry

```bash
pipx install poetry   # Instala o Poetry
poetry install        # Instala dependências do projeto

poetry add mkdocs     # Adiciona MkDocs ao projeto
poetry add pacote     # Adiciona dependência
poetry remove pacote  # Remove dependência

poetry shell          # Ativa ambiente virtual

poetry run mkdocs serve   # Inicia servidor local
poetry run mkdocs build   # Gera site estático
```

## MkDocs

```bash
mkdocs new projeto    # Cria novo projeto (fora do poetry)
```
