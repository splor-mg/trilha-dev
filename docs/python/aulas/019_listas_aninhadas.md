---
comments: true
---
# Aula 019: Listas Aninhados

## 🎥 Vídeo 19

Nesta aula, vamos aprender sobre listas aninhadas ou _nested lists_.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DCxH99NJbeI?si=zG74cPT82CKKr3Zr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são _listas aninhadas_?**

_Listas aninhadas_ são estruturas em que cada elemento de uma lista também pode ser outra lista.
Esse formato é semelhante ao conceito de **matriz**, muito utilizado em matemática e em análise de dados.

#### **Exemplo de matriz**

``` py
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Nesse caso, temos uma _lista_ com três _listas internas_.

#### **Acessando elementos**

Para acessar os elementos utilizamos **índices**:

``` py
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0]) # Imprime [1, 2, 3]
print(matriz[0][1]) # Imprime 2
print(matriz[2][2]) # Imprime 9
```

- O primeiro **índice** acessa a _lista_
- O segundo **índice** acessa o elemento dentro da _lista_

#### **Alterando valores**

Também é possível modificar elementos da matriz:

``` py
matriz[2][2] = 20
print(matriz[2][2])
```

Neste caso, o valor **9** é substituído por **20**.

#### **Percorrendo a matriz**

Podemos percorrer todos os elementos utilizando _loops aninhados_:

``` py
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for item in linha:
        print(item)
```

#### **Funcionamento**

- O primeiro _loop_ percorre cada linha da matriz
- O segundo _loop_ percorre cada item dentro da linha
- Cada elemento é exibido individualmente

Resultado esperado:

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
```

#### **Aplicação prática**

Esse tipo de estrutura é muito comum quando trabalhamos com dados organizados em tabelas, planilhas ou matrizes.
Saber acessar e percorrer esses dados é essencial para manipulação e análise.

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são _listas aninhadas_?
- Como acessar elementos usando múltiplos **índices**
- Como alterar valores
- Como percorrer a estrutura com _loops aninhados_

Esse conceito é bastante utilizado em cenários mais avançados de programação.
