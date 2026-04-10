---
comments: true
---
# Aula 021: Tuplas

## 🎥 Vídeo 21

Nesta aula, vamos aprender sobre tuplas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IZrUBCoNFec?si=S6aBn4umt6aFUB2I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são _tuplas_?**

_Tuplas_ são estruturas semelhantes às _listas_, porém são **imutáveis**, ou seja, não podem ser alteradas após a sua criação.

#### **Criando uma _lista_ e uma _tupla_**

**_Lista_:**

``` py
numeros = [1, 2, 5, 1]
```

**_Tupla_:**

``` py
numeros = (1, 2, 5, 1)
```

A diferença está na **sintaxe**:

- _listas_ usam **colchetes [ ]**
- _tuplas_ usam **parênteses ( )**

#### **Quando usar _tuplas_**

_Tuplas_ são úteis quando queremos garantir que os dados não sejam modificados ao longo do programa.

#### **Usando count()**

Retorna quantas vezes um valor aparece na _tupla_:

``` py
numeros = (1, 2, 5, 1)
print(numeros.count(1))
```

Resultado:

``` py
2
```

Outro exemplo:

``` py
numeros = (1, 2, 5, 1)
print(numeros.count(5))
```

Resultado:

``` py
1
```

#### **Usando index()**

Retorna a posição da primeira ocorrência:

``` py
numeros = (1, 2, 5, 1)
print(numeros.index(5))
```

Resultado:

``` py
2
```

Lembrando:

**numeros = (1, 2, 5, 1)**
- índice 0 → **1**
- índice 1 → **2**
- índice 2 → **5**

Outro exemplo:

``` py
numeros = (1, 2, 5, 1)
print(numeros.index(1))
```

Resultado:

``` py
0
```

#### **Imutabilidade das _tuplas_**

_Tuplas_ não podem ser alteradas.

Exemplo **inválido**:

``` py
numeros = (1, 2, 5, 1)
numeros.append(10)
print(numeros)
```

Isso gera erro, pois _tuplas_ não possuem esse método.

#### **Acessando elementos**

Podemos acessar valores pelo **índice**:

``` py
numeros = (1, 2, 5, 1)
print(numeros[1])
```

Resultado:

``` py
2
```

#### **Tentativa de alteração**

Não é possível modificar valores:

``` py
numeros = (1, 2, 5, 1)
numeros[0] = 6
print(numeros[1])
```

Isso também gera erro.

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são _tuplas_?
- Diferença entre _lista_ e _tupla_
- Como criar _tuplas_
- Métodos disponíveis:
    - **count**
    - **index**
- Como acessar elementos
- O conceito de imutabilidade

_Tuplas_ são importantes quando precisamos garantir que os dados permaneçam constantes durante a execução do programa.
