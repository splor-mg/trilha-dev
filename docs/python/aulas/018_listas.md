---
comments: true
---
# Aula 018: Listas

## 🎥 Vídeo 18

Nesta aula, vamos aprender mais sobre listas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qfEoyKp6iaE?si=ZsHuYs0H6KxkfyNB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender mais sobre listas e como manipular seus elementos em Python.

#### **Criando uma lista**

Listas são criadas utilizando colchetes **[]**:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes)
```

Ao imprimir, os elementos aparecem no terminal junto com os **colchetes**.

É importante lembrar de usar aspas, pois os valores são strings.

#### **Acessando elementos por índice**

Cada item da lista possui uma posição **(índice)**, começando em **0**:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[0]) # Imprime Adriana
print(nomes[4]) # Imprime Maria
```

Se tentar acessar um índice que não existe ocorre erro:

<span style="color: #cbdc39;"><em><strong>index out of range</strong></em></span>

#### **Índices negativos**

Também é possível acessar elementos a partir do final da lista:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[-1]) # Imprime Maria
print(nomes[-2]) # Imprime Ana
```

Isso é útil quando não sabemos o tamanho da lista.

#### **Fatiamento de listas _(slicing)_**

O _slicing_ permite acessar partes da lista:

```py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
print(nomes[2:]) # ["Fernanda", "Ana", "Maria"]
print(nomes[2:4]) # ["Fernanda", "Ana"]
print(nomes[:3]) # ["Adriana", "Júlia", "Fernanda"]
```

Regras:

- O início é inclusivo
- O fim é exclusivo
- Se não informar o início, começa do índice 0
- Se não informar o fim, vai até o final

O _slicing_ não altera a lista original.

#### **Alterando valores**

Para modificar um elemento basta atribuir um novo valor ao índice:

``` py
nomes = ["Adriana", "Júlia", "Fernanda", "Ana", "Maria"]
nomes[0] = "Adriane"
print(nomes)
```

Neste caso, o primeiro item será atualizado.

#### **Conclusão**

Ao final desta aula, você aprendeu:

- Como criar listas
- Como acessar elementos por índice
- Como utilizar índices negativos
- Como aplicar _slicing_
- Como alterar valores na lista

Listas são estruturas fundamentais para trabalhar com coleções de dados em Python.