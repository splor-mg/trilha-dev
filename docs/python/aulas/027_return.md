---
comments: true
---
# Aula 027: Return

## 🎥 Vídeo 27

Nesta aula, vamos aprender sobre o uso do `return`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-IsixC9mE3k?si=ixTt3W1PkiHEAgBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é `return` em funções?**

As funções em Python podem executar cálculos e devolver resultados para o restante do código. Para isso, utilizamos a palavra reservada `return`.

#### **Criando uma função**

Exemplo:

``` py
def quadrado(numero):
    return numero * numero
```

Nesse caso:

- `quadrado` é o nome da função
- `numero` é o parâmetro
- `return` devolve o resultado do cálculo

#### **Executando a função**

Podemos chamar a função passando um argumento:

``` py
quadrado(3)
```

O Python faz:

``` py
3 * 3
```

Resultado:

``` py
9
```

#### **Exibindo o resultado na tela**

Para visualizar o valor retornado, podemos utilizar `print()`:

``` py
print(quadrado(3))
```

Resultado:

``` py
9
```

#### **O papel do `return`**

O `return` é responsável por devolver o resultado da função.

Exemplo:

``` py
def quadrado(numero):
    return numero * numero
```

Sem o `return`, a função executa o cálculo, mas o resultado não fica disponível para reutilização.

#### **Guardando o retorno em variáveis**

Também podemos armazenar o valor retornado em uma variável:

``` py
valor = quadrado(3)
```

Depois disso:

``` py
print(valor)
```

Resultado:

``` py
9
```

#### **Por que guardar o retorno?**

Guardar o retorno permite:

- Reutilizar o resultado
- Fazer novos cálculos
- Utilizar o valor em outras partes do código

Exemplo:

``` py
valor = quadrado(4)

print(valor + 10)
```

Resultado:

``` py
26
```

#### **Funções sem `return`**

Quando uma função não possui `return`, o Python devolve automaticamente `None`.

Exemplo:

``` py
def quadrado(numero):
    print(numero * numero)
```

Executando:

``` py
print(quadrado(3))
```

Resultado:

``` py
9
None
```

#### **Por que aparece `None`?**

O que acontece:

1. A função executa o `print(numero * numero)`
2. O número `9` é exibido na tela
3. Como não existe `return`, o Python devolve `None`

#### **O que é `None`?**

`None` representa ausência de valor no Python.

Ele é utilizado quando uma função não retorna nenhum resultado explicitamente.

#### **Aplicação prática**

Ao criar funções:

- Utilize `return` quando precisar devolver valores
- Prefira funções reutilizáveis
- Evite depender apenas de `print()`
- Guarde resultados em variáveis quando necessário

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que é `return`?;
- Como devolver valores em funções;
- Como utilizar o resultado retornado;
- Como armazenar retornos em variáveis;
- O que acontece em funções sem `return`;
- O significado de `None`.

O `return` é fundamental para criar funções reutilizáveis e tornar o código mais organizado e flexível.