---
comments: true
---
# Aula 008: Métodos de strings

## 🎥 Vídeo 8

Nesta aula, vamos aprender mais sobre as strings e sobre funções específicas que podem ser usadas com elas, chamadas de métodos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/t507HYz7L_s?si=ij96he6HbB-uU7lb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender algumas funções e métodos úteis para trabalhar com strings em Python.

#### **Criando uma string**

Vamos começar criando uma variável:

``` py
curso = "Python é legal"
```

#### **Função len()**

A função **len()** retorna o tamanho de um valor.

Exemplo:

```py
print(len(curso))
```

Primeiro o Python calcula o valor de **len(curso)** e depois imprime o resultado.
Essa função é generalista e pode ser utilizada com outros tipos de dados - como listas.
Também é útil para validação de dados, como verificar o tamanho de um CPF ou de uma data.

#### **Métodos de strings**

Métodos são funções específicas de um tipo de dado.

A sintaxe utiliza ponto (.):

``` py
curso.upper()
```

##### **upper()**

Converte todos os caracteres para maiúsculas:

``` py
print(curso.upper())
```

##### **lower()**

Converte todos os caracteres para minúsculas:

``` py
print(curso.lower())
```

Esses métodos não alteram a variável original, apenas retornam um novo valor.

#### **Método find()**

O método **find()** retorna o índice de um caractere ou palavra:

``` py
print(curso.find("o"))
print(curso.find("P"))
print(curso.find("p"))
print(curso.find("legal"))
```

Observações:

- A contagem começa do zero
- Se não encontrar, retorna -1
- É sensível a maiúsculas e minúsculas

#### **Método replace()**

O método **replace()** substitui partes da string:

``` py
print(curso.replace("legal", "muito legal"))
```

A string original não é alterada.

#### **Operador in**

Permite verificar se um valor está contido na string:

``` py
print("Python" in curso)
```

O resultado será <span style="color: #cbdc39;"><em>True</em></span> ou <span style="color: #cbdc39;"><em>False</em></span>.

Também é sensível a maiúsculas e minúsculas.

#### **Resumo dos principais recursos**

- **len()** → retorna o tamanho
- **upper()** → converte para maiúsculas
- **lower()** → converte para minúsculas
- **find()** → retorna a posição de um valor
- **replace()** → substitui partes da string
- **in** → verifica existência

#### **Conclusão**

Ao final desta aula, você aprendeu:

- Como obter o tamanho de uma string
- Como transformar letras maiúsculas e minúsculas
- Como buscar valores dentro da string
- Como substituir partes do texto
- Como verificar se um valor está presente

Esses recursos são fundamentais para manipulação de textos em Python.