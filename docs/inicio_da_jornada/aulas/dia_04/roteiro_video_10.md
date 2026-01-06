## 🎮 Roteiro para vídeo: "Comandos essenciais do terminal"

### 1. Introdução

"Agora que você já entende que o terminal é uma ponte para conversar com várias ferramentas, chegou a hora de aprender comandos básicos que usamos para navegar e organizar nossos arquivos — e vamos aplicar isso criando um post no seu blog com MkDocs."

---

### 2. Onde estamos? Comando `ls` + `pwd`

- ls        # Lista arquivos e pastas do diretório atual
- pwd       # Mostra o caminho completo do diretório atual

"Esses comandos te mostram onde você está e o que tem ao seu redor."

---

### 3. Criando pastas: mkdir
"Vamos criar uma pasta chamada posts, onde guardaremos os textos do nosso blog."

```
mkdir posts
cd posts
```
---

### 4. Criando arquivos: touch

Agora vamos criar um novo post dentro da pasta posts.

`touch 20250630_primeiro_post.md`

Editar o arquivo com a inclusão dos metadados.

```
---
date:
  created: 2025-06-30
draft: false
---

# Boas-vindas

Esse é o meu primeiro post no blog!
<!-- more -->

Aprendendo terminal, MkDocs e Markdown :)
```

### 5. Voltando e navegando: `cd ..`
Para voltar uma pasta, use `cd ..`. E para navegar direto para qualquer pasta, basta indicar o caminho."

```
cd ..     # volta para a pasta anterior
cd docs   # vai direto para a pasta 'docs' (onde estão as páginas do site)
```
---

### 6. Dica extra: limpando e reorganizando

Se quiser remover um arquivo ou pasta:


`rm [nome do arquivo]`


---
### 7. Salve e visualize seu site localmente:

`poetry run mkdocs serve`

Abra no navegador o endereço http://127.0.0.1:8000 para ver o post incluído.

---
### 8. Salve suas alterações:

"Depois de criar ou editar um post, não esqueça de salvar sua alteração no GitHub."

```
git status
git add docs/blog/2024-06-10-boas-vindas.md
git commit -m "Adiciona primeiro post do blog"
git push
```
---
### 9. Resumo e chamada para o próximo vídeo
"Hoje você aprendeu os comandos básicos para trabalhar com pastas e arquivos no terminal. E o melhor: aplicou isso diretamente no seu site!"

📌 Gancho:

"Agora que temos o terminal dominado, que tal aprender usar os comandos git clonee e entender como o sincronizar alterações com o GitHub."