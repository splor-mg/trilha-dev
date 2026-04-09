---
comments: true
---
# Aula 021: Tuplas

## 🎥 Vídeo 21

Nesta aula, vamos aprender sobre tuplas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IZrUBCoNFec?si=S6aBn4umt6aFUB2I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender sobre tuplas.

#### **O que são tuplas?**

Tuplas são estruturas semelhantes às listas, porém são **imutáveis**, ou seja, não podem ser alteradas após a sua criação.

#### **Criando uma _lista_ e uma _tupla_**

**Lista:**

``` py
numeros = [1, 2, 5, 1]
```

**Tupla:**

``` py
numeros = (1, 2, 5, 1)
```

A diferença está na sintaxe:

- listas usam **colchetes []**
- tuplas usam **parênteses ()**

#### **Quando usar _tuplas_**

Tuplas são úteis quando queremos garantir que os dados não sejam modificados ao longo do programa.

#### **Usando _count()_**

Retorna quantas vezes um valor aparece na tupla:

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
print(numeros.count(5))
```

Resultado:

``` py
1
```

#### **Usando _index()_**

Retorna a posição da primeira ocorrência:

``` py
print(numeros.index(5))
```

Resultado:

``` py
2
```

Lembrando:

``` py
- índice 0 → 1
- índice 1 → 2
- índice 2 → 5
```

Outro exemplo:

``` py
print(numeros.index(1))
```

Resultado:

``` py
0
```

#### **Imutabilidade das _tuplas_**

Tuplas não podem ser alteradas.

Exemplo inválido:

``` py
numeros.append(10)
```

Isso gera erro, pois tuplas não possuem esse método.

#### **Acessando elementos**

Podemos acessar valores pelo índice:

``` py
print(numeros[1])
```

Resultado:

``` py
2
```

#### **Tentativa de alteração**

Não é possível modificar valores:

``` py
numeros[0] = 6
```

Isso também gera erro.

#### **Conclusão**

Ao final desta aula, você aprendeu:

- O que são tuplas?
- Diferença entre _lista_ e _tupla_
- Como criar tuplas
- Métodos disponíveis:
    - count
    - index
- Como acessar elementos
- O conceito de imutabilidade

Tuplas são importantes quando precisamos garantir que os dados permaneçam constantes durante a execução do programa.