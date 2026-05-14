---
comments: true
---
# Aula 025: Parâmetros

## 🎥 Vídeo 25

Nesta aula, vamos aprender sobre parâmetros de funções.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rQg1j9U8nHI?si=3t4qin6bB5y_JoyJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Funções com parâmetros**

As funções em Python também podem receber informações externas para trabalhar com diferentes valores. Essas informações são chamadas de **parâmetros**.

#### **Problema sem parâmetros**

Imagine uma função que sempre exibe o mesmo nome:

``` py
def saudacao():
    print("Olá, Ana!")
```

Resultado:

``` py
Olá, Ana!
```

Nesse caso, a função fica limitada a apenas um nome.

#### **Utilizando parâmetros**

Os parâmetros permitem deixar a função mais dinâmica.

``` py
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Para executar:

``` py
saudacao("Maria")
```

Resultado:

``` py
Olá, Maria!
```

Outro exemplo:

``` py
saudacao("Carlos")
```

Resultado:

``` py
Olá, Carlos!
```

#### **Como funcionam os parâmetros**

Quando chamamos a função:

``` py
saudacao("Maria")
```

O Python faz:

``` py
nome = "Maria"
```

Ou seja, o valor passado na execução é armazenado dentro da variável da função.

#### **Criando funções mais reutilizáveis**

Com parâmetros, a mesma função pode ser usada várias vezes com valores diferentes:

``` py
saudacao("Ana")
saudacao("João")
saudacao("Fernanda")
```

#### **Funções com mais de um parâmetro**

Também podemos utilizar vários parâmetros:

``` py
def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")
```

Executando:

``` py
apresentar("Lucas", 25)
```

Resultado:

``` py
Lucas tem 25 anos.
```

#### **A ordem dos parâmetros importa**

Os valores são enviados conforme a posição definida na função.

``` py
apresentar("Lucas", 25)
```

Nesse caso:

``` py
nome = "Lucas"
idade = 25
```

#### **Erros comuns com parâmetros**

Quantidade incorreta de valores:

``` py
apresentar("Lucas")
```

Isso gera erro, pois a função espera dois parâmetros.

#### **Aplicação prática**

Ao criar parâmetros:

- Utilize nomes claros
- Evite abreviações desnecessárias
- Pense na reutilização da função

Exemplo:

``` py
def calcular_media(nota1, nota2):
    pass
```

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são parâmetros?;
- Como passar valores para funções;
- Como reutilizar funções com diferentes dados;
- Como utilizar múltiplos parâmetros;
- Que a ordem dos parâmetros importa;
- Boas práticas na criação de funções.

Os parâmetros tornam as funções mais flexíveis, reutilizáveis e poderosas.
