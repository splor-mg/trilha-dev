# DIA 3: Escrevendo e publicando

🎥 Vídeo 7 – Documentação é tudo

Objetivo: Mostrar importância da documentação.

Eu estou muito empogada para essa aula, que está bastante densa e a gente vai colocar a mão na massa e já sair daqui com o nosso site iniciado. Nessa aula, que ficou um pouco mais densa, eu vou no final fazer todo mundo cometer um pequeno crime, mas eu juro que vai ficar tudo bem. 

1. Importância de ler a documentação (2-3 min)

    "Uma das habilidades mais importantes no mundo digital é saber ler e interpretar a documentação das ferramentas. Ela é o manual oficial de instruções — atualizada, confiável e completa."

- Evita erros comuns
- Economiza tempo
- Ajuda na autonomia e resolução de problemas

2. O que é o MkDocs (breve retomada) (1-2 min)

    “MkDocs é um gerador de sites estáticos feito especialmente para documentações. Ele transforma arquivos Markdown em um site bonito e organizado — tudo a partir de comandos simples no terminal. Ideal para quem quer criar manuais, guias ou qualquer tipo de documentação técnica (ou administrativa!) de forma rápida e moderna."

3. Navegando na documentação oficial (3-4 min)

- Acesse [mkdocs](https://www.mkdocs.org)
- Mostre as seções principais: Instalação, Uso Básico, Deploy
    "Com dois comandos simples, temos o projeto criado. E tudo isso está explicado com exemplos no site oficial."

4. Então vamos começar o nosso projeto e colocar a mão na massa? 

- Primeiro nós vamos abrir o nosso ambiente de desenvolvimento que nós já preparamos nas aulas passadas.
- Agora nós vamos seguir o que a documentação do MKDOCS
  "MkDocs requires a recent version of Python and the Python package manager, pip, to be installed on your system." 

O python a gente já sabe que já está instalado no nosso ambiente de desenvolvimento, nós terminamos a última aula usando ele para printar na tela " Olá, mundo!". E agora, e esse tal de gerenciador de pacotes?  

5. O que é um gerenciador de pacotes (2-3 min)

Um gerenciador de pacotes é como uma loja de aplicativos para programadores. Ele instala, atualiza e remove ferramentas e bibliotecas automaticamente. No caso, o mkdocks estfalando para a gente usar o pip que é o padrão do python, mas não existe só ele e eu vou te apresentar um segundo, que é o Poetry! 

5. pip x poetry (2-3 min)

|__PIP__ | __POETRY__|
| -------------------- | --------------------- |
| Padrão do Python | Ferramenta mais moderna |
| Instala pacotes diretamente | Cria ambientes virtuais e gerencia dependências de forma isolada |
| Simples e direto | Mais controle e organização |

"Neste curso, vamos usar o poetr por ser mais moderno e porque é o que usamos em outros projetos aqui na splor, isso pode facilitar quando você começar a contribuir neles.

6. Poetry

Ok, se vamos usar o Poetry, vamos até a documentação dele descobrir como usar.

- [Poetry](https://python-poetry.org/)

    - Verifica se tem o `pipx`
    ```
    pipx --version
    ```
    - Instala o `poetry` com o  `pipx`
    ```
    pipx install poetry
    ```
    - (Em um projeto já existente) Inicia o Poetry 
    ```
    poetry init
    ```
- Finalmente, vamos estão instalar o mkdocs!  
    
    - Instala o `Mkdocs` usando o `poetry`
    ```
    poetry  add mkdocs

    ```
    Cria o site 
    ```
    poetry run mkdocs new .
    ``` 
- Mostrar o que o comando criou: 

    - Um arquivo de configuração: mkdocs.yml, 
    - Uma pasta onde ficará a sua documentação, nesse momento tem apenas um documento que é a pagina inicial do nosso site: index.md.

- O MkDocs vem com uma funcionalidade embutida de um servidor de desenvolvimento, que permite você visualizar sua documentação enquanto você trabalha. Vamos ver como isso funciona? 
    Liga o servidor 
    ```
    poetry run mkdocs serve
    ``` 
    Desliga o servidor 
    ```
    ctrl + C 
    ```

7. Salvando o trabalho feito 

Agora chegou a hora do crime que eu comentei, eu vou pedir todo mundo para salvar de um jeito que não é o ideal e vc vai entender porque é um crime, nas próximas aulas. Mas, como eu não quero deixar ninguém confuso demais nós vamos fazer juntos as ações necessárias para salvar o trabalho, usando a interface gráfica do Codespaces.

📌 Gancho: Resumo e chamada para a prática (1 min)

"Agora você entende onde buscar informação oficial, como instalar o MkDocs, tá na hora de a gente começar a edita do nosso jeito. No próximo vídeo, vamos aprender como escrever com MkDocs. Para isso você tem uma tarefa: elabore o texto que você deseja que esteja na página inicial do seu site antes de iniciar próxima aula. Te vejo lá!

Atividade: Anotar o que deseja escrever sobre si mesmo.


🎥 Vídeo 8 – Aprendendo Markdown

Objetivo: Ensinar sintaxe básica do Markdown.

Roteiro:

Títulos, negrito, êtisco, listas, links, imagens.

Mostrar visualização.

🎥 Vídeo 9 – Editar página e comitar

Objetivo: Aplicar Markdown na página inicial e salvar alterações.

Roteiro:

Abrir arquivo da homepage (docs/index.md).

Escrever apresentação pessoal.

Explicar git add, git commit, git push.

Gancho: "Mas esses comandos são do Markdown? Não! Vamos entender."

Checklist Dia 3: