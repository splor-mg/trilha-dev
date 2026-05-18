---
title: Gerenciadores de Pacotes e Ambiente Virtual
---

# :simple-python: Gerenciadores de Pacotes e Ambiente Virtual

[← Voltar ao guia](../)

---

## **Poetry**

Instala o Poetry (feito uma única vez):
```bash
pipx install poetry
```

Instala as dependências do projeto listadas no `pyproject.toml`:
```bash
poetry install
```

!!! tip "Dica"
    Execute `poetry install` sempre que clonar um repositório pela primeira vez.

Adiciona um pacote ao projeto:
```bash
poetry add <nome-do-pacote>
```

Remove um pacote do projeto:
```bash
poetry remove <nome-do-pacote>
```

Ativa o ambiente virtual do projeto:
```bash
poetry shell
```

## **Pip**

Instala um pacote:
```bash
pip install <nome-do-pacote>
```

Remove um pacote:
```bash
pip uninstall <nome-do-pacote>
```

Lista os pacotes instalados:
```bash
pip list
```

!!! info "Pip ou Poetry?"
    Nos projetos da Trilha Dev, prefira sempre o **Poetry**. Use o `pip` apenas quando estiver fora de um projeto com `pyproject.toml`.

## **Pipx**

Instala uma ferramenta globalmente:
```bash
pipx install <nome-da-ferramenta>
```

Atualiza uma ferramenta instalada:
```bash
pipx upgrade <nome-da-ferramenta>
```

Lista as ferramentas instaladas:
```bash
pipx list
```

!!! example "Exemplo do Trilha Dev"
    ```bash
    pipx install poetry
    ```

## **Venv**

Cria um ambiente virtual na pasta `.venv`:
```bash
python -m venv .venv
```

Ativa o ambiente virtual (Linux/WSL):
```bash
source .venv/bin/activate
```

Desativa o ambiente virtual:
```bash
deactivate
```

!!! info "Por que usar ambiente virtual?"
    Isola as dependências do projeto, evitando conflitos entre versões de pacotes de projetos diferentes.


