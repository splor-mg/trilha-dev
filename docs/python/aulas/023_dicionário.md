---
comments: true
---
# Aula 023: Dicionários

## 🎥 Vídeo 23

Nesta aula, vamos aprender sobre dicionários.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YKmwvwyyP2k?si=XsMqOfKe9n0wXlP6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### **O que são dicionários?**

Os dicionários em Python são estruturas de dados utilizadas para armazenar informações em formato de **chave e valor**.

Esse formato facilita a organização, a pesquisa e a manipulação de dados.

#### **Exemplo de chave e valor**

Imagine um sistema escolar:

- `nome` → "Ana"
- `idade` → `10`
- `matriculada` → `True`

Nesse caso:

- `nome`, `idade` e `matriculada` são as **chaves**
- `"Ana"`, `10` e `True` são os **valores**

#### **Criando um dicionário**

``` py
aluno = {
    "nome": "Ana",
    "idade": 10,
    "matriculada": True
}
```

#### **Estrutura do dicionário**

Os dicionários utilizam:

- `{}` → para delimitar o dicionário
- `:` → para separar chave e valor
- `,` → para separar os pares de dados

#### **Tipos de dados nos valores**

Um dicionário pode armazenar diferentes tipos de dados:

``` py
aluno = {
    "nome": "Ana",
    "idade": 10,
    "matriculada": True
}
```

Nesse exemplo:

- `"Ana"` é uma _string_
- `10` é um inteiro
- `True` é um booleano

#### **As chaves devem ser únicas**

As chaves de um dicionário não podem se repetir.

Exemplo incorreto:

``` py
aluno = {
    "nome": "Ana",
    "nome": "Maria"
}
```

Isso pode causar problemas na organização dos dados.

#### **Acessando valores do dicionário**

Para acessar um valor, utilizamos a chave entre colchetes:

``` py
print(aluno["idade"])
```

Resultado:

``` py
10
```

#### **Alterando valores**

Também é possível modificar um valor existente:

``` py
aluno["idade"] = 12
```

Testando:

``` py
print(aluno["idade"])
```

Resultado:

``` py
12
```

#### **Adicionando novos dados**

Podemos incluir novos pares de chave e valor:

``` py
aluno["turma"] = "A25"
```

Testando:

``` py
print(aluno["turma"])
```

Resultado:

``` py
A25
```

#### **Utilizando o método `get()`**

Outra forma de acessar valores é utilizando o método `get()`:

``` py
print(aluno.get("idade"))
```

Resultado:

``` py
10
```

#### **Utilizando `get()` com novas chaves**

Também é possível acessar novos dados adicionados ao dicionário:

``` py
print(aluno.get("turma"))
```

Resultado:

``` py
A25
```

### **Checklist**

Ao final desta aula, você aprendeu:

- O que são dicionários?;
- Como criar um dicionário;
- Como utilizar pares de chave e valor;
- Como acessar valores dentro do dicionário;
- Como alterar informações;
- Como adicionar novos dados;
- Como utilizar o método `get()`.

Os dicionários são fundamentais em Python e muito utilizados para organizar dados de maneira estruturada e eficiente.
