---
comments: true
---
# Aula 011: Funções matemáticas.

## 🎥 Vídeo 11

Nesta aula, vamos aprender sobre alguma funções matemáticas e introduzir o módulo `math`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bicESc9nXEA?si=5cktC3kvRFFHJVwl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender algumas funções matemáticas disponíveis no Python, tanto funções embutidas quanto funções do módulo math.

#### **Utilizando a função round()**

Vamos começar com um exemplo:

``` py
x = 2.9
print(round(x))
```

A função **round()** é uma função embutida que realiza o arredondamento de valores.

Resultado esperado:

``` py
3
```

Alguns comportamentos importantes:

```py
- round(2.2) → retorna 2
- round(2.5) → retorna 2
```

Ou seja, o arredondamento segue regras específicas que podem ser exploradas com testes.

#### **Função abs()**

A função **abs()** retorna o valor absoluto de um número:

``` py
print(abs(-2.9))
```

Resultado:

``` py
2.9
```

Essa função sempre retorna um valor positivo.

#### **Utilizando o módulo math**

Para operações mais avançadas, o Python possui o módulo <span style="color: #cbdc39;"><strong>math</strong></span>.

Para utilizá-lo:

``` py
import math
```

#### **Função math.ceil()**

Arredonda o número para cima:

``` py
print(math.ceil(2.9))
```

Resultado:

``` py
3
```

#### **Função math.floor()**

Arredonda o número para baixo:

``` py
print(math.floor(2.9))
```

Resultado:

``` py
2
```

#### **Outras funções do módulo math**

O módulo <span style="color: #cbdc39;"><strong>math</strong></span> oferece diversas funções úteis, como:

- Cálculo de **π**
- Funções trigonométricas
- Outras operações matemáticas avançadas

Para conhecer todas as opções, é recomendado consultar a documentação oficial do Python.

#### **Conclusão**

Ao final desta aula, você aprendeu:

- Como utilizar a função **round()**
- Como obter o valor absoluto com **abs()**
- Como importar e usar o módulo **math**
- Como aplicar funções como **ceil()** e **floor()**

Essas ferramentas são úteis para realizar cálculos mais precisos e resolver problemas matemáticos em Python.
