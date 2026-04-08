---
comments: true
---
# Aula 006: Strings

## 🎥 Vídeo 6

Nesta aula, nós vamos aprender mais sobre as strings e como manipulá-las.

<iframe width="560" height="315" src="https://www.youtube.com/embed/m6JKs9dlhco?si=hvgDyDcCKuj4w88o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprofundar o conhecimento sobre strings e aprender formas de manipulá-las em Python.

#### **O que são strings**

Strings são sequências de caracteres delimitadas por aspas simples (') ou duplas (").

Exemplo:

``` py
string = "Python é legal"
```

#### **Uso de aspas dentro de strings**

É possível utilizar aspas dentro de uma string, desde que sejam diferentes das aspas que delimitam o texto:

``` py
string = 'Python é uma linguagem "poderosa"'
```

Ou:

``` py
string = "Python é uma linguagem 'poderosa'"
```

É importante sempre abrir e fechar corretamente as aspas. Caso contrário, o Python não conseguirá interpretar a string e gerará erro.

#### **Acessando caracteres por índice**

Cada caractere de uma string possui uma posição (índice), iniciando em **0**.

Exemplo:

``` py
string = "Python é legal"
print(string[0]) # Imprime a letra P
print(string[2]) # Imprime a letra t
```

#### **Índices negativos**

Também é possível acessar caracteres a partir do final da string:

``` py
string = "Python é legal"
print(string[-1]) # Último caractere - letra l
print(string[-2]) # Penúltimo caractere - letra a
```

#### **Fatiamento de strings (slicing)**

O fatiamento (slicing) permite acessar partes da string utilizando intervalos:

``` py
string = "Python é legal"
print(string[2:-2]) # Imprime thon é leg
```

**Regras importantes:**

``` py
- O índice inicial é incluído
- O índice final é excluído
```

**Outros exemplos:**

``` py
texto = "Python é legal"
print(string[2:]) # Do índice 2 até o final - thon é legal
print(string[:4]) # Do início até o índice 3 - Pyth
```
Quando um dos valores é omitido, o Python assume automaticamente o início ou o fim da string.

#### **Repetição de strings**

Também é possível repetir uma string:

``` py
string = "Python é legal"
string2 = string[:]
print(string2)
```

#### **Boas práticas**

``` py
- Sempre verifique se as aspas estão corretamente fechadas
- Teste diferentes índices para entender o comportamento
- Pratique slicing para ganhar familiaridade
```

#### **Conclusão**

Ao final desta aula, você aprendeu:

- O que são strings e como defini-las
- Como utilizar aspas corretamente
- Como acessar caracteres por índice
- Como usar índices negativos
- Como extrair partes da string com slicing
- Como repetir strings

Esses conceitos são fundamentais para trabalhar com textos em Python e serão muito utilizados em programas mais avançados.