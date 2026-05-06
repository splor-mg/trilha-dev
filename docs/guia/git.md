---
title: Git
---

# Git

[← Voltar ao guia](../)

---

## Verificação

```bash
git status          # Mostra o estado dos arquivos
git log             # Exibe o histórico de commits
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
git checkout -b nova-branch   # Cria uma nova branch
git checkout nome-branch      # Troca de branch
```

## Sincronização

```bash
git pull origin main            # Atualiza com a branch principal
git pull --rebase origin main   # Atualiza evitando commits extras
git push origin minha-branch    # Envia alterações para o repositório remoto
```

## Configuração inicial

```bash
git config --global user.name "Seu Nome"        # Define o nome do autor dos commits (usado em todos os repositórios na máquina)
git config --global user.email "seu@email.com"  # Define o e-mail do autor dos commits (associado ao GitHub ou outro serviço)
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
