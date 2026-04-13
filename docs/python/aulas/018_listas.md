---
comments: true
---
# Aula 018: Listas

## 🎥 Vídeo 18

Nesta aula, vamos aprender mais sobre listas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qfEoyKp6iaE?si=ZsHuYs0H6KxkfyNB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Criando uma lista**

_Listas_ são criadas utilizando colchetes **[ ]**:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes)
```

Ao imprimir, os elementos aparecem no terminal junto com os **colchetes**.
É importante lembrar de usar _aspas_, pois os valores são _strings_.

#### **Acessando elementos por índice**

Cada item da _lista_ possui uma posição **(índice)**, começando em **0**:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[0]) # Imprime Adriana
print(nomes[4]) # Imprime Maria
```

Se tentar acessar um **índice** que não existe, ocorre erro:

``` py
Traceback (most recent call last):
  File "/workspaces/curso-python/aulas/018/app.py", line 2, in <module>
    print(nomes[5])
                ^^^
IndexError: list index out of range
```

#### **Índices negativos**

Também é possível acessar elementos a partir do final da _lista_:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[-1]) # Imprime Maria
print(nomes[-2]) # Imprime Ana
```

Isso é útil quando não sabemos o tamanho da _lista_.

#### **Fatiamento de _listas_ (slicing)**

O **slicing** permite acessar partes da _lista_:

```py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[2:]) # ["Fernanda", "Ana", "Maria"]
print(nomes[2:4]) # ["Fernanda", "Ana"]
print(nomes[:3]) # ["Adriana", "Júlia", "Fernanda"]
```

Regras:

- O início é **inclusivo**
- O fim é **exclusivo**
- Se não informar o **início**, começa do índice **0**
- Se não informar o **fim**, vai até o **final**

O **slicing** não altera a lista original.

#### **Alterando valores**

Para modificar um elemento basta atribuir um novo valor ao **índice**:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
nomes[0] = "Adriane"
print(nomes)
```

Neste caso, o primeiro item será atualizado.

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como criar _listas_
- Como acessar elementos por **índice**
- Como utilizar **índices negativos**
- Como aplicar **slicing**
- Como alterar valores na _lista_

_Listas_ são estruturas fundamentais para trabalhar com coleções de dados em Python.
