---
comments: true
---
# Aula 008: Métodos de strings

## 🎥 Vídeo 8

Nesta aula, vamos aprender mais sobre as strings e sobre funções específicas que podem ser usadas com elas, chamadas de métodos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/t507HYz7L_s?si=ij96he6HbB-uU7lb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

#### **Métodos de _strings_**

Métodos são funções específicas de um tipo de dado.

A sintaxe utiliza ponto **( . )**:

``` py
curso.upper()
```

##### **Usando upper()**

Converte todos os caracteres para **maiúsculas**:

``` py
print(curso.upper())
```

##### **Usando lower()**

Converte todos os caracteres para **minúsculas**:

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

O método **replace()** substitui partes da _string_:

``` py
print(curso.replace("legal", "muito legal"))
```

A _string_ original não é alterada.

#### **Operador in**

Permite verificar se um valor está contido na _string_:

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
- **replace()** → substitui partes da _string_
- **in** → verifica existência

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como obter o tamanho de uma _string_
- Como transformar letras maiúsculas e minúsculas
- Como buscar valores dentro da _string_
- Como substituir partes do texto
- Como verificar se um valor está presente

Esses recursos são fundamentais para manipulação de textos em Python.
