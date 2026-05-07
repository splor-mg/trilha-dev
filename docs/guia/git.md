---
title: Git
---

# Git

[← Voltar ao guia](../)

---

## Inicialização

```bash
git init                 # Inicializa um repositório Git
git clone URL            # Clona um repositório remoto
```

## Stage seletivo

```bash
git add arquivo.txt      # Adiciona apenas um arquivo
git add pasta/           # Adiciona uma pasta inteira
```

## Verificação e Histórico

```bash
git status          # Mostra o estado dos arquivos

git log             # Exibe o histórico de commits
git log --oneline   # Histórico resumido
git log --graph     # Histórico visual das branches

git diff            # Mostra alterações não commitadas
git diff --staged   # Mostra alterações no stage
```

## Versionamento

```bash
git add .                 # Adiciona alterações
git commit -m "mensagem"  # Registra alterações
```

## Desfazer alterações

```bash
git restore arquivo.txt           # Desfaz alterações no arquivo
git restore --staged arquivo.txt  # Remove arquivo do stage
```

## Branches

```bash
git branch                    # Lista branches locais
git branch -a                 # Lista branches locais e remotas
git branch -d branch          # Remove branch local
git checkout -b nova-branch   # Cria uma nova branch
git checkout nome-branch      # Troca de branch
```

## Sincronização

```bash
git pull origin main            # Atualiza com a branch principal
git pull --rebase origin main   # Atualiza evitando commits extras

git push origin minha-branch    # Envia alterações para o repositório remoto

git fetch                       # Busca atualizações do repositório remoto sem aplicar alterações
git fetch origin                # Busca atualizações do repositório remoto chamado origin
git fetch upstream              # Busca atualizações do repositório original (upstream)
git fetch --all                 # Busca atualizações de todos os repositórios remotos configurados
git checkout main               # Vai para a branch main local
git merge upstream/main         # Aplica as atualizações na sua main
```

!!! info "Diferença entre `fetch` e `pull`"
    O comando **`git fetch`** apenas baixa as atualizações do ==repositório remoto==. Já o comando **`git pull`** baixa e aplica automaticamente as alterações na ==branch atual==.

!!! tip "Dica"
    O **`git fetch`** é mais seguro para verificar mudanças antes de atualizar sua branch local.

## Reorganização de histório

```bash
git rebase main   # Reorganiza commits sobre a main
```

## Configuração inicial

```bash
git config --global user.name "Seu Nome"        # Define o nome do autor dos commits (usado em todos os repositórios na máquina)
git config --global user.email "seu@email.com"  # Define o e-mail do autor dos commits (associado ao GitHub ou outro serviço)
```

## Recuperação temporária

```bash
git stash           # Guarda alterações temporariamente
git stash pop       # Recupera alterações salvas
```

## Tags

```bash
git tag             # Lista tags
git tag v1.0        # Cria uma tag
```

## Remotos e Inspeção

```bash
git remote -v            # Lista repositórios remotos

git show                 # Mostra detalhes do último commit
git blame arquivo.py     # Mostra autoria por linha
```

## Fork no repositório

```bash
# Após criar o fork no GitHub (botão "Fork")

git clone git@github.com:SEU-USUARIO/exercicios-python.git   # Clona seu fork
cd exercicios-python                                         # Acessa a pasta do projeto

git remote add upstream git@github.com:splor-mg/exercicios-python.git   # Conecta com o repositório original
git remote -v                                                           # Verifica os remotes configurados

git fetch upstream        # Busca atualizações do repositório original
git checkout main         # Vai para a branch main
git merge upstream/main   # Atualiza sua main com as mudanças do upstream
```

!!! tip "Dica"
    No GitHub, verifique se o repositório aparece como:
    **`forked from splor-mg/exercicios-python`**

!!! warning "Atenção"
    O comando **`git merge upstream/main`** pode gerar conflitos caso você tenha alterações locais.


## Fluxo comum

```bash
git status
git add .
git commit -m "mensagem"
git push origin minha-branch
```
