---
comments: true
---
# Aula 028: Exceções com o `try` e `except`

## 🎥 Vídeo 28

Nesta aula, vamos aprender  como tratar erros.

<iframe width="560" height="315" src="https://www.youtube.com/embed/p-kacbRGXHY?si=ONJ9ay0H8pYb-vUP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Tratando erros em Python**

Durante a execução de um programa, erros podem acontecer. Alguns desses erros são previsíveis e podem ser tratados para evitar que o programa pare de funcionar.

Para isso, o Python oferece a estrutura `try` e `except`.

#### **Exemplo: recebendo a idade do usuário**

``` py
idade = int(input("Idade: "))

print(idade)
```

Nesse exemplo:

- `input()` recebe um valor digitado pelo usuário
- `int()` converte o valor para inteiro
- `print()` exibe o resultado

#### **Funcionando corretamente**

Se o usuário digitar:

``` py
20
```

Resultado:

``` py
20
```

#### **Quando acontece um erro**

Se o usuário digitar:

``` py
abc
```

O Python gera um erro:

``` py
ValueError
```

Isso acontece porque:

- `int()` só consegue converter números inteiros
- `"abc"` não pode ser convertido para inteiro

Sem tratamento, o programa é interrompido.

#### **Lendo mensagens de erro**

As mensagens de erro normalmente informam:

- O arquivo onde ocorreu o erro
- A linha do código
- O tipo do erro
- A causa do problema

Exemplo:

``` py
ValueError: invalid literal for int()
```

#### **Utilizando `try` e `except`**

Podemos tratar esse erro utilizando:

``` py
try:
    idade = int(input("Idade: "))
    print(idade)

except ValueError:
    print("Idade inválida")
```

#### **Como funciona**

O Python:

1. Tenta executar o bloco `try`
2. Se ocorrer o erro informado no `except`
3. Executa o tratamento definido

#### **Fluxo correto**

Se o usuário digitar:

``` py
20
```

Resultado:

``` py
20
```

#### **Fluxo com erro**

Se o usuário digitar:

``` py
abc
```

Resultado:

``` py
Idade inválida
```

O programa continua funcionando normalmente.

#### **Estrutura do `try` e `except`**

``` py
try:
    # código que pode gerar erro

except TipoDoErro:
    # tratamento do erro
```

#### **Indentação é obrigatória**

Assim como em funções e condicionais, os blocos precisam estar identados:

``` py
try:
    print("Tentando executar")

except ValueError:
    print("Erro encontrado")
```

#### **Tratando mais de um erro**

Podemos tratar vários erros diferentes.

Exemplo:

``` py
try:
    idade = int(input("Idade: "))

    salario = 10000

    print(salario / idade)

except ValueError:
    print("Idade inválida")

except ZeroDivisionError:
    print("A idade não pode ser zero")
```

#### **Erro de divisão por zero**

Se o usuário informar:

``` py
0
```

O Python gera:

``` py
ZeroDivisionError
```

Porque não é possível dividir um número por zero.

#### **Tratando a divisão por zero**

Com o `except`, conseguimos evitar que o programa pare:

``` py
except ZeroDivisionError:
    print("A idade não pode ser zero")
```

Resultado:

``` py
A idade não pode ser zero
```

#### **Por que tratar erros?**

O tratamento de erros permite:

- Evitar que o programa pare inesperadamente
- Melhorar a experiência do usuário
- Criar sistemas mais estáveis
- Exibir mensagens mais amigáveis

#### **Exemplos comuns no dia a dia**

Tratamento de erros é muito usado em:

- Login de usuários
- Cadastro de contas
- Validação de e-mails
- Formulários
- Sistemas bancários
- APIs

#### **Aplicação prática**

Ao tratar erros:

- Leia sempre a mensagem do erro
- Trate apenas erros previsíveis
- Mostre mensagens claras para o usuário
- Evite deixar o programa encerrar inesperadamente

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são erros previsíveis
- Como utilizar `try`
- Como utilizar `except`
- Como tratar `ValueError`
- Como tratar `ZeroDivisionError`
- Como impedir que o programa pare ao encontrar erros

O tratamento de erros é essencial para criar programas mais seguros, confiáveis e fáceis de utilizar.