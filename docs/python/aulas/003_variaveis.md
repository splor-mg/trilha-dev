---
comments: true
---
# Aula 003: Variáveis

## 🎥 Vídeo 3

Neste vídeo, vamos aprender o que é uma variável e alguns tipos de dados.

<iframe width="560" height="315" src="https://www.youtube.com/embed/58vPFbpKqto?si=CDQfTTJQV4yRUeXF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Nesta aula, você vai aprender o conceito de variáveis e como utilizá-las para armazenar informações em um programa Python.

#### **O que são variáveis**

Uma variável é um espaço na memória do computador utilizado para armazenar um valor. Ela funciona como um identificador _(nome)_ associado a um dado. Esse nome permite acessar e reutilizar a informação ao longo do programa.

Exemplo:

**nota = 5**

Nesse caso, o valor **5** está armazenado na variável chamada **nota**.

#### **Utilizando variáveis**

Para exibir o valor de uma variável, utilizamos a função **print()**:

<span style="color: #cbdc39;"><strong><em>print(nota)</em></strong></span>

É importante não utilizar aspas ao passar o nome da variável. Caso contrário, o Python interpretará como texto, e não como uma referência ao valor armazenado.

#### **Atualização de valores**

O valor de uma variável pode ser alterado ao longo do programa:

<span style="color: #cbdc39;"><strong><em>nota = 5</em></strong></span>

<span style="color: #cbdc39;"><strong><em>nota = 8.5</em></strong></span>

<span style="color: #cbdc39;"><strong><em>print(nota)</em></strong></span>

Como o Python executa o código de cima para baixo, o valor final exibido será **8.5**.

#### **Tipos de dados**

As variáveis podem armazenar diferentes tipos de dados:

- **Inteiro (int)**: números sem casas decimais
- **Float (float)**: números com casas decimais (utilizando ponto)
- **String (str)**: textos entre aspas
- **Booleano (bool)**: valores lógicos (**True** ou **False**)

Exemplos:

<span style="color: #cbdc39;"><strong><em>nota = 8**</em></strong></span>

<span style="color: #cbdc39;"><strong><em>media = 7.5**</em></strong></span>

<span style="color: #cbdc39;"><strong><em>nome = "Abel"**</em></strong></span>

<span style="color: #cbdc39;"><strong><em>estudando = True**</em></strong></span>

#### **Boas práticas na criação de variáveis**

Para manter o código organizado e legível:

- Utilize nomes descritivos **(ex: nota_final, nome_aluno)**
- Escreva em letras minúsculas
- Separe palavras com _underscore_ **(\_)**

Evite nomes genéricos como **x** ou **y**, pois dificultam o entendimento do código.

#### **Case sensitive**

O Python diferencia letras maiúsculas de minúsculas. Isso significa que:

- _True_ é válido
- _true_ é inválido

Algumas palavras são reservadas pela linguagem e devem ser utilizadas exatamente como definidas.

#### **Conclusão**

Ao final desta aula, você aprendeu:

- O que são variáveis e para que servem;
- Como armazenar e acessar valores;
- Como atualizar informações;
- Os principais tipos de dados do Python;
- Boas práticas de nomeação.

Esses conceitos são fundamentais para construir programas mais estruturados e dinâmicos.
