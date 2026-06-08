---
title: Git
---

# :simple-git: Git

[← Voltar ao guia](../guia/index.md)

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

## **Fluxo de Trabalho Completo**

!!! tip "Ordem recomendada"
    `status` → `add` → `commit` → `push`

### 1. Atualizar o Projeto Local

Antes de iniciar qualquer tarefa você deve ir para a branch `main`

```bash
git switch main
```

Verificar estado do repositório

```bash
git status
```

Resultado esperado:

```text
On branch dev
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### 2. Criar Nova Branch

Sempre criar branches a partir da `main` atualizada.

Exemplo de feature:

```bash
git switch -c feat/login-social
```

### 3. Desenvolver a Funcionalidade

Durante o desenvolvimento:

- realizar commits pequenos;
- testar frequentemente;
- evitar mudanças muito grandes.

Verificar alterações. Certifique-se que não foram alterados documentos que não estavam dentro do seu escopo de trabalho.

```bash
git status
```

Adicionar arquivos — adicionar tudo:

```bash
git add .
```

Adicionar arquivo específico:

```bash
git add src/auth/login.py
```

Criar commit:

```bash
git commit -m "Implementa funcionalidade de login"
```

### 4. Enviar Branch para o GitHub

```bash
git push origin feat/login-social
```

### 5. Abrir Pull Request

Após o push, acessar o GitHub, abrir Pull Request e selecionar:

Base `main` > Compare `feat/login-social`


??? example "Fluxo de Trabalho Completo"

    ```mermaid
     flowchart TB
        A(["`**Início**`"]) --> B["`**git switch main**`"]
        B --> S["`**git status**`"]
        S --> C["`**git switch -c<br>feat/nova-feature**`"]
        C --> D["`**Desenvolver<br>commits pequenos · testar**`"]
        D --> E1["`**git add .<br>(todos os arquivos)**`"]
        D --> E2["`**git add caminho/arquivo.py<br>(um arquivo específico)**`"]
        E1 --> F["`**git commit -m 'mensagem'**`"]
        E2 --> F
        F --> G["`**git push origin<br>feat/nova-feature**`"]
        G --> H["`**Abrir Pull Request no GitHub<br>Base: main · Compare: feat/nova-feature**`"]
        H --> I(["`**Fim**`"])

        A:::terminal
        B:::git
        S:::git
        C:::git
        D:::etapa
        E1:::git
        E2:::git
        F:::git
        G:::git
        H:::etapa
        I:::terminal
    ```

## **Histórico e inspeção**

Exibe o histórico de commits:
```bash
git log
```

Histórico resumido, uma linha por commit:
```bash
git log --oneline
```

Mostra alterações ainda não adicionadas ao stage (alterações entre commits, entre um commit e a árvore de trabalho, etc):
```bash
git diff
```

Mostra alterações já no stage:
```bash
git diff --staged
```

---

## **Desfazer alterações**

Descarta as alterações feitas em um arquivo e restaura a versão do último commit:
```bash
git restore <nome-do-arquivo.txt>
```

Remove o arquivo do stage sem descartar as alterações:
```bash
git restore --staged <nome-do-arquivo.txt>
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

Cria uma nova branch e muda automaticamente para ela:
```bash
git checkout -b <nome-da-branch>
```

Troca para outra branch:
```bash
git checkout <nome-da-branch>
```

Remove uma branch local que já foi mergeada:
```bash
git branch -d <nome-da-branch>
```

Busca atualizações do repositório remoto, incluindo novas branches, sem alterar sua branch atual:
```bash
git fetch
```
---

## **Sincronização com remoto**

Baixa e aplica as alterações da branch remota:
```bash
git pull origin main
```

Envia sua branch para o repositório remoto:
```bash
git push origin <minha-branch>
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

Fluxo para manter um fork atualizado com o repositório original.

Após criar o fork no GitHub (botão **Fork**), clone o seu fork:
```bash
git clone git@github.com:SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

Entre na pasta do projeto:
```bash
cd <NOME-DO-REPOSITORIO>
```

Conecta o repositório original como upstream:
```bash
git remote add upstream git@github.com:USUARIO-ORIGINAL/NOME-DO-REPOSITORIO.git
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

Aplica as atualizações do repositório original na sua main:
```bash
git merge upstream/main
```

!!! tip "Como verificar"
    No GitHub, o repositório deve aparecer como **`forked from USUARIO-ORIGINAL/NOME-DO-REPOSITORIO`**.

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
