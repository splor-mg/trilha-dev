---
title: Git
---

# :simple-git: Git

[← Voltar ao guia](../)

---

## **Configuração inicial**

Execute uma única vez ao configurar o ambiente:

Define o nome do autor dos commits:
```bash
git config --global user.name "Seu Nome"
```

Define o e-mail do autor dos commits:
```bash
git config --global user.email "seu@email.com"
```

---

## **Inicialização**

Inicializa um repositório local:
```bash
git init
```

Clona um repositório remoto:
```bash
git clone URL
```

---

## **Fluxo básico de trabalho**

!!! tip "Ordem recomendada"
    `status` → `add` → `commit` → `push`

Mostra o estado dos arquivos:
```bash
git status
```

Adiciona todas as alterações ao stage:
```bash
git add .
```

Adiciona um arquivo específico ao stage:
```bash
git add <nome-do-arquivo.txt>
```

Registra as alterações com uma mensagem:
```bash
git commit -m <"mensagem do commit">
```

Envia as alterações para o repositório remoto:
```bash
git push origin minha-branch
```

---

## **Histórico e inspeção**

Exibe o histórico de commits:
```bash
git log
```

Histórico resumido, uma linha por commit:
```bash
git log --oneline
```

Mostra alterações ainda não adicionadas ao stage:
```bash
git diff
```

Mostra alterações já no stage:
```bash
git diff --staged
```

---

## **Desfazer alterações**

Descarta alterações no arquivo (volta ao último commit):
```bash
git restore arquivo.txt
```

Remove o arquivo do stage sem descartar as alterações:
```bash
git restore --staged arquivo.txt
```

!!! warning "Atenção"
    O `git restore` descarta mudanças não commitadas. Use com cuidado.

---

## **Branches**

Lista as branches locais:
```bash
git branch
```

Lista branches locais e remotas:
```bash
git branch -a
```

Cria uma nova branch e já entra nela:
```bash
git checkout -b nova-branch
```

Troca para outra branch:
```bash
git checkout nome-da-branch
```

Remove uma branch local (somente se já mergeada):
```bash
git branch -d nome-da-branch
```

---

## **Sincronização com remoto**

Baixa e aplica as alterações da branch remota:
```bash
git pull origin main
```

Envia sua branch para o repositório remoto:
```bash
git push origin minha-branch
```

Baixa atualizações sem aplicar na branch atual:
```bash
git fetch origin
```

!!! info "Diferença entre `fetch` e `pull`"
    **`git fetch`** apenas baixa as atualizações do repositório remoto, sem alterar sua branch local. **`git pull`** baixa e aplica automaticamente.

    O `fetch` é mais seguro para inspecionar o que mudou antes de integrar.

---

## **Fork e upstream**

Fluxo usado no repositório de exercícios da Trilha Dev.

Após criar o fork no GitHub (botão **Fork**), clone o seu fork:
```bash
git clone git@github.com:SEU-USUARIO/exercicios-python.git
```

Entre na pasta do projeto:
```bash
cd exercicios-python
```

Conecta com o repositório original:
```bash
git remote add upstream git@github.com:splor-mg/exercicios-python.git
```

Confirma os remotes configurados:
```bash
git remote -v
```

Busca atualizações do repositório original:
```bash
git fetch upstream
```

Vai para a branch main local:
```bash
git checkout main
```

Aplica as atualizações na sua main:
```bash
git merge upstream/main
```

!!! tip "Como verificar"
    No GitHub, o repositório deve aparecer como **`forked from splor-mg/exercicios-python`**.

---

## **Guardar trabalho temporariamente**

Útil quando precisar trocar de branch sem commitar:

Guarda as alterações atuais temporariamente:
```bash
git stash
```

Recupera as alterações guardadas:
```bash
git stash pop
```
