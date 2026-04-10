---
comments: true
---
# Aula 016: Estruturas de repetição

## 🎥 Vídeo 16

Nesta aula, vamos aprender sobre estruturas de repetição com o `for` loop.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qSI67mwNueY?si=dNX7oCfqg23cVBnp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é o for?**

O **for** é utilizado para percorrer elementos de uma sequência.
Pode ser entendido como: **“para cada item”** dentro de uma coleção.

#### **Exemplo com _string_**

``` py
for item in "Python":
    print(item)
```

Neste caso:

- A -string_ **"Python"** é uma sequência de caracteres
- A variável item representa cada letra
- O _loop_ percorre todos os caracteres

Resultado:

``` py
P
y
t
h
o
n
```

#### **Diferença em relação ao while**

- O **while** depende de uma **condição**
- O **for** percorre uma sequência com **fim definido**

#### **Exemplo com _lista_**

Listas são definidas com **colchetes**:

``` py
for item in ["banana", "maçã", "abacate"]:
    print(item)
```

Resultado:

``` py
banana
maçã
abacate
```

Também funciona com números:

``` py
for item in [1, 5, 9]:
    print(item)
```

#### **Função range()**

A função **range()** gera uma sequência de números.

``` py
for item in range(10):
    print(item)
```

Resultado:

``` py
0
1
2
3
4
5
6
7
8
9
```

**_Obs.: O valor final não é incluído._**

#### **Definindo início e fim**

``` py
for item in range(1, 11):
    print(item)
```

Resultado:

``` py
1
2
3
4
5
6
7
8
9
10
```

#### **Utilizando o passo (step)**

``` py
for item in range(1, 11, 2):
    print(item)
```

Resultado:

``` py
1
3
5
7
9
```

#### **Resumo**

- **for** percorre elementos de uma sequência
- A variável de _loop_ (ex: item) representa cada elemento
- **in** indica a coleção a ser percorrida
- A coleção pode ser:
    - _string_
    - _lista_
    - _range_

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como utilizar o **for**
- Como percorrer _strings_ e _listas_
- Como gerar sequências com _range()_
- Como controlar **início**, **fim** e **passo**

O **for** é uma das estruturas mais utilizadas para repetição em Python.
