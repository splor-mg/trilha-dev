---
comments: true
---
# Aula 009: Operadores Aritméticos

## 🎥 Vídeo 9

Nesta aula, vamos aprender sobre as operações matemáticas que podemos fazer com `inteiros` e `floats`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SRVupPRpKWM?si=U2hpNO61qvCHX9RM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Tipos numéricos**

No Python existem dois tipos principais de números:

- **int**: números inteiros (ex: 10)
- **float**: números decimais (ex: 10.5)

Números decimais utilizam ponto ( **.** ) em vez de **vírgula**.

#### **Operações básicas**

As operações aritméticas seguem a lógica da matemática:

``` py
x = 10 + 3
```

Outros operadores:

``` py
- Subtração: -
- Multiplicação: *
```

#### **Divisão**

Existem duas formas de divisão:

``` py
x = 10 / 3
print(x)
```
Usando uma **/** retorna um número do tipo **float** (com números decimais).

``` py
x = 10 // 3
```
Usando duas **//** retorna um número inteiro (ou seja, arredonda o resultado de números decimais).

#### **Outros operadores:**

**Módulo ( % )**

Retorna o resto da divisão:

``` py
x = 10 % 3

Resultado: 1
```

**Exponenciação ( \*\* )**

Representa potência:

``` py
x = 10 ** 3

Resultado: 1000
```

#### **Atribuição com operadores**

Também é possível realizar operações de forma mais compacta.

Forma tradicional:

``` py
x = 10
x = x + 3
print(x)
```

Forma simplificada:

``` py
x = 10
x += 3
print(x)
```

Ambas produzem o mesmo resultado.

#### **Vantagens da forma simplificada**

- Código mais limpo
- Escrita mais rápida
- Muito utilizada no dia a dia

#### **Checklist**

Ao final desta aula, você aprendeu:

- Os principais operadores aritméticos
- A diferença entre divisão comum e divisão inteira
- Como utilizar módulo e exponenciação
- Como simplificar operações com atribuição

Esses conceitos são fundamentais para trabalhar com cálculos em Python.
