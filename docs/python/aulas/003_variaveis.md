---
comments: true
---
# Aula 003: Variáveis

## 🎥 Vídeo 3

Neste vídeo, vamos aprender o que é uma variável e alguns tipos de dados.

<iframe width="560" height="315" src="https://www.youtube.com/embed/58vPFbpKqto?si=CDQfTTJQV4yRUeXF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são variáveis?**

Uma variável é um espaço na memória do computador utilizado para armazenar um valor. Ela funciona como um identificador **(nome)** associado a um dado. Esse nome permite acessar e reutilizar a informação ao longo do programa.

Exemplo:

``` py
nota = 5
```

Neste caso, o valor **5** está armazenado na variável chamada **nota**.

#### **Utilizando variáveis**

Para exibir o valor de uma variável utilizamos a função **print()**:

``` py
print(nota)
```

É importante não utilizar aspas ao passar o nome da variável. Caso contrário, o Python interpretará como texto, e não como uma referência ao valor armazenado.

#### **Atualização de valores**

O valor de uma variável pode ser alterado ao longo do programa:

``` py
nota = 5
nota = 8.5
print(nota)
```

Como o Python executa o código de cima para baixo, o valor final exibido será **8.5**.

#### **Tipos de dados**

As variáveis podem armazenar diferentes tipos de dados:

- **Inteiro (int)**: números sem casas decimais
- **Float (float)**: números com casas decimais (utilizando ponto)
- **String (str)**: textos entre _aspas_
- **Booleano (bool)**: valores lógicos (_True_ ou _False_)

Exemplos:

``` py
nota = 8
media = 7.5
nome = "Abel"
estudando = True
```

#### **Boas práticas na criação de variáveis**

Para manter o código organizado e legível:

- Utilize nomes descritivos (ex: **nota_final**, **nome_aluno**)
- Escreva em letras **minúsculas**
- Separe palavras com _underscore_ **( _ )**.


Evite nomes genéricos como **x** ou **y**, pois dificultam o entendimento do código.

#### **Case sensitive**

O Python diferencia letras **maiúsculas** de **minúsculas**. Isso significa que:

- <span style="color: #cbdc39;"><em>True</em></span> é válido.
- <span style="color: #cbdc39;"><em>true</em></span> é inválido.

Algumas palavras são reservadas pela linguagem e devem ser utilizadas exatamente como definidas.

#### **Checklist**

Ao final desta aula você aprendeu:

- O que são variáveis e para que servem
- Como armazenar e acessar valores
- Como atualizar informações
- Os principais tipos de dados do Python
- Boas práticas de nomeação

Esses conceitos são fundamentais para construir programas mais estruturados e dinâmicos.
