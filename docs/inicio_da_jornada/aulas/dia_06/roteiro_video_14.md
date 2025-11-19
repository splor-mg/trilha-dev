# "Branch e Pull Request: colaborando com segurança"
## 1. Introdução
Na aula passada, criamos uma issue para sugerir uma nova seção no nosso site. Agora vamos transformar essa ideia em realidade — mas sem bagunçar o projeto principal. Como? Usando branches e pull requests.

## 2. Conceito de branch (ramo)
Pense na branch como uma cópia da sua linha principal de desenvolvimento, onde você pode testar e desenvolver novas ideias sem interferir no que já está funcionando.

A branch principal costuma se chamar `main.`

Quando queremos fazer uma nova funcionalidade, criamos uma nova branch, ex: `post-aprendizados.`

Assim, podemos trabalhar de forma isolada e segura.

📌 Vantagens:

- Permite testar sem afetar o site em produção.

- Facilita o trabalho em equipe: cada pessoa trabalha em sua própria branch.

## 3. Conceito de pull request (PR)
Depois que finalizamos o trabalho numa branch, precisamos integrar essa mudança ao projeto principal. A maneira mais organizada e segura de fazer isso é com um pull request.

O PR serve para revisar o que foi feito, comentar, pedir sugestões e, por fim, juntar (fazer o merge) com a branch principal.

O nome pull vem da ideia de “puxar” aquela alteração para dentro da main.

📌 Boa prática: Sempre associe o PR com a issue que deu origem à tarefa.

## 4. Criando a branch a partir da issue
No terminal:

```
git checkout -b post-aprendizados
checkout -b cria e muda para uma nova branch chamada post-aprendizados.
```

💡 Dica: escolha nomes curtos e descritivos para as branches.

## 5. Fazendo as alterações no projeto
- Criar o post sugerido na issue:

```
mkdir blog
touch blog/aprendizados.md
Adicionar conteúdo ao aprendizados.md (ex: principais aprendizados do curso).
```
- Atualizar o mkdocs.yml para incluir o novo post:

```
nav:
  - Início: index.md
  - Blog:
    - Aprendizados da semana: blog/aprendizados.md
```

## 6. Comitar e enviar a branch
```
git add .
git commit -m "Criação do post com aprendizados da semana"
git push origin post-aprendizados
```

## 7. Criando o pull request no GitHub
Passo a passo:

- Vá até o repositório no GitHub

- Clique no banner amarelo que aparece ("Compare & pull request") ou vá na aba "Pull Requests" e clique em "New pull request"

- Selecione:

Base: `main`
Compare: `post-aprendizados`

- Preencha:

Título
Descrição com referência à issue (ex: Closes #1)
Clique em "Create pull request"

Pronto! Agora temos uma sugestão de alteração registrada, que pode ser revisada e aprovada antes de ser incluída no site.

## 8. Conclusão
Hoje você aprendeu a criar um novo ramo (branch), a fazer uma alteração de forma isolada, e a propor essa alteração com um pull request. Esse é o fluxo mais comum em projetos reais!

## 9. Gancho para a próxima aula
Na próxima aula, vamos entender o que acontece depois que um pull request é aprovado: como fazer o merge e manter o projeto principal sempre atualizado.