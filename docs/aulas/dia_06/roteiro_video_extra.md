# Batalha de Commits: Resolvendo Conflitos no Git

## 1. Abertura – Contexto da Competição (1 min)
- Raiane apresenta a aula:
> "Hoje vamos aprender a lidar com algo inevitável quando trabalhamos em equipe: conflitos no Git. E, para deixar tudo mais divertido, vamos criar um conflito proposital — numa corrida contra o tempo!"
- Apresentar o Gabriel:
> "Aqui está o Gabriel, meu colega, pronto para tentar me derrotar!"
- Explicar rapidamente a dinâmica:
    - Ambos vão tentar editar a mesma linha no repositório Trilha Dev.
    - O primeiro que fizer o merge na main ganha a corrida.
    - O segundo, ao tentar mergear, vai encontrar um conflito.

2. Preparação para o Desafio (1 min)

- Mostrar o trecho do arquivo onde a frase será adicionada.
- Explicar:
>"Cada um vai colocar a frase 'O Gabriel é o vencedor do desafio' ou 'A Raiane é a vencedora do desafio', logo abaixo da área reservada no arquivo."
- Mostrar rapidamente que ambos estão trabalhando em branches diferentes.

## 3. A Corrida (1–2 min)
- Iniciar a contagem regressiva (pode ser com humor, tipo “3, 2, 1, Git!”).
- Gravar simultaneamente a tela dos dois OU gravar a tela do repositório ou do site.

## 4. Explicação do Conflito (2 min)
- Mostrar a mensagem de erro do GitHub ou do terminal.
- O que é um conflito: quando duas alterações afetam exatamente a mesma parte de um arquivo e o Git não consegue decidir sozinho qual manter.
- Ressaltar: conflitos não são “erros graves”, apenas exigem decisão humana.

## 5. Resolução do Conflito (3–4 min)
- Abrir o editor de código (ou a ferramenta de merge do GitHub).
- Mostrar:
    - Localizar os marcadores de conflito (<<<<<<<, =======, >>>>>>>).
    - Escolher qual conteúdo manter (ou mesclar as partes).
    - Apagar os marcadores.
    - Salvar o arquivo.
- Fazer git add e git commit para registrar a resolução.
- Fazer o git push para atualizar o pull request.
- Mostrar o merge sendo concluído.

6. Boas Práticas para Evitar Conflitos (1–2 min)
- Atualizar sua branch com frequência (git pull origin main).
- Dividir alterações grandes em commits menores.
- Comunicar-se com a equipe sobre arquivos críticos.

7. Encerramento (1 min)
- Mostrar o arquivo final com o nome do vencedor.
- Reforçar a mensagem:

> “Conflitos fazem parte do trabalho em equipe. Com calma e método, é fácil resolvê-los.”