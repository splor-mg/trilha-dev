---
comments: true
---
# Aula 005: Conversão de dados _(casting)_

## 🎥 Vídeo 5

Nesta aula, nós vamos aprender como podemos transformar um tipo de dado.
A conversão de tipo em Python é feita usando novas funções que aprenderemos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JBxs9pzNn4E?si=FrVoN5HIOs-saB6X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- `int()` - constrói um número inteiro a partir de um decimal - `flot`-, removendo todas as casas decimais ou de uma `string`, desde que a `string` represente um número inteiro.
- `float()` - constrói um número decimal - `flot`- a partir de um inteiro ou de uma `string`, desde que a `string` represente um número decimal ou um inteiro.
- `str()` - constrói uma `string` a partir de uma ampla variedade de tipos de dados, incluindo `strings`, `inteiros` e decimais - `flot`-.
- `bool()` - constrói um booleano a partir de um inteiro, `float` ou `string`.


Nesta aula, você vai aprender como converter tipos de dados em Python, permitindo realizar operações corretamente.

#### **Proposta do programa**

O objetivo é criar um programa que:

``` py
- Solicite o ano de nascimento do usuário
- Calcule a idade com base no ano atual
- Exiba o resultado no terminal
```

#### **Coletando o dado do usuário**

Primeiro, utilizamos a função **input()** para receber o ano de nascimento:

``` py
ano_nascimento = input("Ano de nascimento: ")
```

Esse valor será armazenado na variável **ano_nascimento**.

#### **Realizando o cálculo**

Em seguida, calculamos a idade:

``` py
idade = 2026 - ano_nascimento
```

#### **Entendendo o erro**

Ao executar esse código, ocorre um erro.

Isso acontece porque:

``` py
- 2026 é um número inteiro (int)
- ano_nascimento é uma string (str)
```

A função **input()** sempre retorna uma string, mesmo que o valor digitado seja numérico.

O Python não permite realizar operações matemáticas entre diferentes tipos, como inteiro e string.

#### **Conversão de tipos (casting)**

Para resolver o problema, é necessário converter o valor recebido para inteiro utilizando a função **int()**:

``` py
ano_nascimento = int(input("Ano de nascimento: "))
idade = 2026 - ano_nascimento
```

Agora, o cálculo pode ser realizado corretamente.

#### **Exibindo o resultado**

``` py
print(idade)
```

#### **Outras funções de conversão**

O Python possui outras funções para conversão de tipos:

``` py
- int() → converte para inteiro
- float() → converte para número decimal
- str() → converte para texto
- bool() → converte para valor booleano
```

Essas funções são chamadas de funções **built-in** (nativas da linguagem).

#### **Verificando tipos com type()**

A função **type()** permite identificar o tipo de um valor:

``` py
print(type(ano_nascimento))
print(type(idade))
```

Isso é útil para entender como os dados estão sendo interpretados pelo Python.

#### **Fluxo do programa**

Ao executar:

``` py
1.  O usuário informa o ano de nascimento
2.  O valor é convertido para inteiro
3.  A idade é calculada
4.  O resultado é exibido
```

#### **Conclusão**

Ao final desta aula, você aprendeu:

- Que a função **input()** retorna uma string
- Por que ocorre erro ao misturar tipos diferentes
- Como converter dados utilizando casting
- Como verificar tipos com **type()**
- A importância de garantir o tipo correto para cada operação

Esses conceitos são fundamentais para evitar erros e trabalhar corretamente com dados em Python.