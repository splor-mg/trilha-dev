---
title: Gerenciadores de Pacotes e Ambiente Virtual
---

# :material-package-variant:{ .lg .middle } Gerenciadores de Pacotes e Ambiente Virtual

[← Voltar ao guia](../)

---

## **[Poetry](https://python-poetry.org/docs/)**

!!! info "Pré-requisito"
    Este comando utiliza o **pipx** para instalar o Poetry. Verifique se ele está instalado na sua máquina:

```bash
pipx --version
```

!!! tip "Dica"
    Caso não tenha o pipx, veja a seção [Pipx](#pipx) deste guia. Existem também [outras formas de instalar o Poetry](https://python-poetry.org/docs/#installation) conforme a documentação oficial.

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

Atualiza as dependências para as versões mais recentes permitidas pelo `pyproject.toml`:
```bash
poetry update
```

Atualiza o `poetry.lock` sem instalar nada (útil após editar o `pyproject.toml` manualmente):
```bash
poetry lock
```

Executa um comando dentro do ambiente virtual sem precisar ativá-lo:
```bash
poetry run <comando>
```

Ativa o ambiente virtual do projeto:

=== "Linux / macOS (bash/zsh)"
```bash
eval $(poetry env activate)
```

=== "macOS (fish)"
```fish
eval (poetry env activate)
```

=== "Windows (PowerShell)"
```powershell
Invoke-Expression (poetry env activate)
```

=== "Windows (CMD)"
```bat
poetry env activate
```
!!! warning "Atenção"
    No CMD, copie e cole manualmente o caminho retornado pelo comando acima e execute-o diretamente.


Desativa o ambiente virtual do projeto:
```bash
deactivate
```

---

## **[Pip](https://pip.pypa.io/en/stable/)**

Instala um pacote:
```bash
pip install <nome-do-pacote>
```

Instala uma versão específica de um pacote:
```bash
pip install <nome-do-pacote>==<versão>
```

Atualiza um pacote:
```bash
pip install --upgrade <nome-do-pacote>
```

Remove um pacote:
```bash
pip uninstall <nome-do-pacote>
```

Lista os pacotes instalados:
```bash
pip list
```

Exibe detalhes de um pacote instalado:
```bash
pip show <nome-do-pacote>
```

Instala dependências a partir de um arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

Gera um `requirements.txt` com os pacotes instalados no ambiente atual:
```bash
pip freeze > requirements.txt
```

!!! info "Pip ou Poetry?"
    Nos projetos do Trilha Dev, prefira sempre o **Poetry**. Use o `pip` apenas quando estiver fora de um projeto com `pyproject.toml`.

---

## **[Pipx](https://pipx.pypa.io/stable/)**

Instala uma ferramenta globalmente:
```bash
pipx install <nome-da-ferramenta>
```

Atualiza uma ferramenta instalada:
```bash
pipx upgrade <nome-da-ferramenta>
```

Atualiza todas as ferramentas instaladas:
```bash
pipx upgrade-all
```

Remove uma ferramenta instalada:
```bash
pipx uninstall <nome-da-ferramenta>
```

Lista as ferramentas instaladas:
```bash
pipx list
```

!!! example "Exemplo do Trilha Dev"
    pipx install poetry


---

## **[Venv](https://docs.python.org/3/library/venv.html)**

Cria um ambiente virtual na pasta `.venv`:
```bash
python -m venv .venv
```

!!! info "Informação"
    O nome `.venv` é apenas uma convenção. Você pode usar qualquer nome ao criar o ambiente virtual, por exemplo:
```bash
python -m venv .<meu-ambiente>
```
    Lembre-se de substituir `.venv` pelo nome escolhido nos comandos de ativação.


Ativa o ambiente virtual:

=== "Linux / macOS (bash/zsh)"
```bash
source .venv/bin/activate
```

=== "Windows (PowerShell)"
```powershell
.venv\Scripts\Activate.ps1
```

=== "Windows (CMD)"
```bat
.venv\Scripts\activate.bat
```

Instala as dependências após ativar o ambiente:
```bash
pip install -r requirements.txt
```

Desativa o ambiente virtual:
```bash
deactivate
```

!!! info "Por que usar ambiente virtual?"
    Isola as dependências do projeto, evitando conflitos entre versões de pacotes de projetos diferentes.
