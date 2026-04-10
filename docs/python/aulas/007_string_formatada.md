---
comments: true
---
# Aula 007: Formatação de strings

## 🎥 Vídeo 7

Nesta aula, nós vamos aprender mais sobre as strings e como formatá-las para um código mais prático e limpo.

<iframe width="560" height="315" src="https://www.youtube.com/embed/exabtQvKtzc?si=tY-VH8rjQLZncFo8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Contexto do problema**

Em muitos programas é necessário exibir mensagens personalizadas utilizando informações do usuário.

Exemplo de dados:

``` py
nome = "Ana"
sobrenome = "Silva"
```

O objetivo é exibir a seguinte mensagem:

``` py
Ana Silva é uma aluna nova.
```

#### **Concatenação de _strings_**

Uma forma de montar essa mensagem é utilizando concatenação com o operador **+**:

``` py
mensagem = nome + " " + sobrenome + " é uma aluna nova."
print(mensagem)
```

Neste caso, estamos unindo:

- o valor da variável **nome**
- um **espaço**
- o valor da variável **sobrenome**
- o restante da frase

#### **Formatação com _f-strings_**

Uma forma mais prática e legível de fazer isso é utilizando **_f-strings_**.
Com essa abordagem adicionamos a letra **f** antes da _string_ e utilizamos **{ }** para inserir variáveis diretamente:

``` py
mensagem = f"{nome} {sobrenome} é uma aluna nova."
print(mensagem)
```

O Python substitui automaticamente os valores das variáveis dentro das **chaves**.

#### **Reatribuição de variáveis**

Quando uma variável é redefinida o Python considera apenas o valor mais recente.

Exemplo:

``` py
mensagem = nome + " " + sobrenome + " é uma aluna nova."
mensagem2 = f"{nome} {sobrenome} é uma aluna nova."
print(mensagem2)
```

Neste caso, o valor exibido será o da variável utilizada no **print**.

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como concatenar _strings_ utilizando o operador **+**
- Como utilizar **_f-strings_** para formatação
- Como inserir variáveis dentro de _strings_
- Como funciona a reatribuição de variáveis

A formatação de strings é um recurso muito utilizado para tornar o código mais organizado e facilitar a construção de mensagens dinâmicas.
