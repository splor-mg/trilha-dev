## 🎨 Aula Extra: Estilizando seu site com Material for MkDocs

### Introdução: O que é o Material for MkDocs

> "Agora que temos um site funcionando, que tal deixá-lo com a nossa cara? É hora de aprender como personalizar o visual com o **Material for MkDocs**."

- **Material for MkDocs** é um tema moderno e personalizável.
- Oferece visual profissional, responsivo e acessível.
- Usado por grandes projetos e empresas.

---

### Instalando o Material for MkDocs

No terminal:

_bash_
poetry add mkdocs-material


### Ativando o tema no seu projeto

1. No arquivo mkdocs.yml:

theme:
  name: material

2. Salve e execute:

`mkdocs serve`

3. Abra no navegador: http://127.0.0.1:8000

### Customizando cores e fontes

Exemplo de configuração no mkdocs.yml:

site_name: Meu Portfólio
theme:
  name: material
  palette:
    primary: teal
    accent: orange
  font:
    text: Roboto
    code: Roboto Mono

Você pode escolher outras cores na documentação oficial

### Adicionando uma seção de Blog

- No mkdocs.yml:

nav:
  - Início: index.md
  - Blog:
      - Primeiro Post: blog/post1.md

- No terminal:

`mkdir blog`
`touch blog/post1.md`

No arquivo blog/post1.md, adicione seu conteúdo Markdown.

## Outras personalizações possíveis

- Logo e favicon personalizados
- Dark mode automático
- Ícones e emojis
- Busca integrada

### Conclusão

"Com o Material for MkDocs, seu site ganha vida com poucas configurações. Explore a documentação e torne seu portfólio único!"

📌 Dica: guarde o link da documentação para consultar sempre que quiser ajustar algo:https://squidfunk.github.io/mkdocs-material