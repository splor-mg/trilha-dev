---
comments: true
---
# **Como fazer os exercícios do curso**

O trilha-dev: Python conta com um [repositório de exercícios](https://github.com/splor-mg/exercicios-python) próprios para que você aproveite ao máximo os seus aprendizados. Nele você encontará exercícios para explorar diversas competências e em níveis de dificuldade.

Nos vídeos abaixo, eu vou te mostrar tudo o que você precisa saber para começar a fazer os exercícios da trilha, mesmo que você nunca tenha programado antes.
Além disso, se você tiver dúvida sobre o que for apresentado nesses vídeos, visite (ou revisite) o Trilha Dev: Início da Jornada.

## Como fazer o setup do repositório de exercícios

Neste primeiro vídeo, vamos fazer o setup do projeto seguindo as orientações do README.md do repositório.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ftAtqfZ4GW8?si=6XjFfzSqeVCa2CuS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Como fazer os exercícios e rodar testes

Neste segundo vídeo, vamos entender a estrutura do repositório e fazer o passo a passo de como resolver os exercícios com a ajuda dos testes automatizados.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Up50Nytue9s?si=7enSjmhWpQiUut5P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Como o repositório está organizado

```
exercicio-01/
│
├── README.md
├── main.py
└── tests/
```

- `README.md`: Aqui está o enunciado do exercício, ou seja, é o que você precisa resolver.
- `main.py`: Aqui é onde você vai escrever sua resposta.
- `tests/`: Aqui estão os testes automáticos que vão verificar se sua solução está correta.”

### Para resolver os exercícios

- Navegue até um exercício que você deseja resolver.
- Encontre o arquivo `main.py` e substitua o _placeholder_ `pass` pela sua resolução.


### Usando o pytest para verificar sua resposta

- Certifique-se de que você está na pasta na qual deseja rodar o teste.
- Rode o comando

```
task test
```
- Analise o resultado

```
. → passou
F → falhou
```
##💡 Lembre-se

Errar faz parte — use o erro como guia. Você não precisa saber tudo para começar. Comece com o básico, tente resolver, veja o que o teste diz e ajuste.
O mais importante é praticar!
