---
comments: true
---
# Aula 014: Operadores de comparação

## 🎥 Vídeo 14

Nesta aula, vamos aprender sobre operadores para fazermos comparações.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3hxkR7hk-_8?si=7DkQXB8N-dJB8gCO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são operadores de comparação?**

Operadores de comparação permitem comparar valores e retornam um resultado _booleano_:

- **True**
- **False**

Esses operadores são muito utilizados em estruturas condicionais.

#### **Exemplo inicial**

Vamos criar uma variável:

``` py
temperatura = 30
```

Agora, podemos usar uma condição:

``` py
if temperatura > 30:
  print("O dia está quente")
```

Neste caso:

``` py
- 30 > 30 → False
- Nada será exibido
```

Se alterarmos:

``` py
temperatura = 31

- 31 > 30 → True
- A mensagem será exibida
```

#### **Principais operadores**

**Maior que (>)**

``` py
temperatura > 30
```

**Menor que (<)**

``` py
temperatura < 40
```

**Maior ou igual (>=)**

``` py
temperatura >= 30
```

**Menor ou igual (<=)**

``` py
temperatura <= 30
```

**Diferente (!=)**

``` py
temperatura != 30
```

**Igual (==)**

``` py
temperatura == 30
```

#### **Diferença entre ( = ) e ( == )**

É importante **NÃO** confundir:

- **Atribuição** de valor para uma variável **( = )**.

``` PY
temperatura = 30
```

- **Comparação** entre valores **( == )**.
``` PY
temperatura == 30
```

A comparação retorna:

- _True_ se os valores forem iguais
- _False_ caso contrário

#### **Aplicação prática**

Esses operadores permitem criar diferentes cenários - como:

- Temperatura acima de 30 → _dia quente_;
- Temperatura abaixo de 10 → _usar agasalho_;
- Temperatura em intervalo específico → _dia agradável_.

#### **Checklist**

Ao final desta aula você aprendeu:

- Como comparar valores em Python
- Os principais operadores de comparação
- A diferença entre atribuição e comparação
- Como utilizar esses operadores em condições

Esses conceitos são fundamentais para a construção de regras e decisões em programas.
