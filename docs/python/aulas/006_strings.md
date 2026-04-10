---
comments: true
---
# Aula 006: Strings

## 🎥 Vídeo 6

Nesta aula, nós vamos aprender mais sobre as _strings_ e como manipulá-las.

<iframe width="560" height="315" src="https://www.youtube.com/embed/m6JKs9dlhco?si=hvgDyDcCKuj4w88o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são _strings_?**

_Strings_ são sequências de caracteres delimitadas por _aspas_ simples **( ' )** ou duplas **( " )**.

Exemplo:

``` py
string = "Python é legal"
```

#### **Uso de _aspas_ dentro de _strings_**

É possível utilizar _aspas_ dentro de uma _string_, desde que sejam diferentes das _aspas_ que delimitam o texto:

``` py
string = 'Python é uma linguagem "poderosa"'
```

Ou:

``` py
string = "Python é uma linguagem 'poderosa'"
```

É importante sempre abrir e fechar corretamente as _aspas_. Caso contrário, o Python não conseguirá interpretar a _string_ e gerará erro.

#### **Acessando caracteres por índice**

Cada caractere de uma _string_ possui uma posição **(índice)**, iniciando em **0**.

Exemplo:

``` py
string = "Python é legal"
print(string[0]) # Imprime a letra P
print(string[2]) # Imprime a letra t
```

#### **Índices negativos**

Também é possível acessar caracteres a partir do final da _string_:

``` py
string = "Python é legal"
print(string[-1]) # Último caractere - letra l
print(string[-2]) # Penúltimo caractere - letra a
```

#### **Fatiamento de _strings_ (slicing)**

O fatiamento **(slicing)** permite acessar partes da _string_ utilizando intervalos:

``` py
string = "Python é legal"
print(string[2:-2]) # Imprime thon é leg
```

**Regras importantes:**

- O índice inicial é **incluído**
- O índice final é **excluído**

**Outros exemplos:**

``` py
texto = "Python é legal"
print(string[2:]) # Do índice 2 até o final - thon é legal
print(string[:4]) # Do início até o índice 3 - Pyth
```
Quando um dos valores é omitido o Python assume automaticamente o início ou o fim da _string_.

#### **Repetição de _strings_**

Também é possível repetir uma _string_:

``` py
string = "Python é legal"
string2 = string[:]
print(string2)
```

#### **Boas práticas**

- Sempre verifique se as _aspas_ estão corretamente fechadas
- Teste diferentes **índices** para entender o comportamento
- Pratique **slicing** para ganhar familiaridade

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são _strings_ e como defini-las?
- Como utilizar _aspas_ corretamente
- Como acessar caracteres por **índice**
- Como usar **índices negativos**
- Como extrair partes da _string_ com **slicing**
- Como repetir _strings_

Esses conceitos são fundamentais para trabalhar com textos em Python e serão muito utilizados em programas mais avançados.
