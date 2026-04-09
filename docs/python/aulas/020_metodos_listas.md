---
comments: true
---
# Aula 020: Métodos de listas

## 🎥 Vídeo 20

Nesta aula, vamos aprender mais sobre as listas e sobre funções específicas que podem ser usadas com elas, chamadas de métodos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IADW1tvA0ew?si=feaBouw7dzqBWgvv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender sobre métodos de listas.

#### **O que são métodos?**

Métodos são funções específicas que utilizamos com determinados tipos de dados - como listas.
A sintaxe é diferente das funções tradicionais:

<span style="color: #cbdc39;"><strong>numeros.metodo()</strong></span>

Ou seja:

- usamos a variável
- seguida de ponto **(.)**
- nome do método

#### **Criando a lista**

``` py
numeros = [7, 5, 8, 2, 0]
```

#### **Usando _append()_**

Adiciona um item ao final da lista:

``` py
numeros.append(1)
print(numeros)
```

Resultado:

``` py
[7, 5, 8, 2, 0, 1\]
```

#### **Usando _insert()_**

Adiciona um item em uma posição específica:

``` py
numeros.insert(0, 1)
print(numeros)
```

Resultado:

``` py
[1, 7, 5, 8, 2, 0]
```

#### **Usando _remove()_**

Remove a primeira ocorrência de um valor:

``` py
numeros.remove(8)
print(numeros)
```

#### **Usando _clear()_**

Remove todos os elementos da lista:

``` py
numeros.clear()
print(numeros)
```

Resultado:

``` py
[]
```

#### **Usando _pop()_**

Remove o último elemento da lista:

``` py
numeros.pop()
print(numeros)
```

#### **Usando _index()_**

Retorna o índice da primeira ocorrência de um valor:

``` py
print(numeros.index(8))
```

<span style="color: #cbdc39;"><strong>Atenção:</strong></span> **se o valor não existir, ocorre erro.**

#### **Verificação com _in_**

Forma segura de verificar se um valor está na lista:

``` py
print(8 in numeros) # True
print(9 in numeros) # False
```

#### **Usando _count()_**

Conta quantas vezes um valor aparece:

``` py
print(numeros.count(8))
```

#### **Usando _sort()_**

Ordena a lista:

``` py
numeros.sort()
print(numeros)
```

<span style="color: #cbdc39;"><strong>Atenção:</strong></span> **altera a lista original.**

#### **Usando _reverse()_**

Inverte a ordem da lista:

``` py
numeros.reverse()
print(numeros)
```

#### **Usando _copy()_**

Cria uma cópia da lista:

``` py
numeros2 = numeros.copy()
print(numeros2)
```

Alterando a lista original:

``` py
numeros.append(1)
print(numeros)
print(numeros2)
```

A cópia não será alterada.

#### **Observação importante**

Cuidado com nomes de variáveis:

``` py
numeros2 # correto
numero2 # errado
```

Erro comum:

``` py
NameError: variável não definida
```

#### **Conclusão**

Ao final desta aula, você aprendeu:

- O que são métodos de listas?
- Como utilizar a sintaxe com ponto **(.)**
- Principais métodos:
    - append
    - insert
    - remove
    - clear
    - pop
    - index
    - count
    - sort
    - reverse
    - copy
- Como verificar valores com _in_

A prática é essencial para entender o comportamento de cada método.