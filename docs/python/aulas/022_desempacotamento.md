---
comments: true
---
# Aula 022: Desempacotamento ou _unpacking_

## 🎥 Vídeo 22

Nesta aula, vamos aprender sobre desempacotamento.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RBqp2J8Z-Zw?si=MYUpc2ven55cVufh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é unpacking?**

O _unpacking_ permite pegar valores de um objeto **iterável** (como _listas_ e _tuplas_) e atribuí-los diretamente a variáveis.

#### **Exemplo com _tupla_**

``` py
coordenadas = (1, 2, 3)
```

Forma menos eficiente:

``` py
coordenadas[0] * coordenadas[1] * coordenadas[2]
```

Outra forma:

``` py
x = coordenadas[0]
y = coordenadas[1]
z = coordenadas[2]
```

Uso das variáveis:

``` py
x * y * z
```

#### **Utilizando _unpacking_**

``` py
x, y, z = coordenadas
```

O Python faz automaticamente:

``` py
- x recebe 1
- y recebe 2
- z recebe 3
```

Testando:

``` py
print(y)
```

Resultado:

``` py
2
```

Outro teste:

``` py
print(z)
```

Resultado:

``` py
3
```

#### **Funciona com _listas_**

``` py
coordenadas = [1, 2, 3]
x, y, z = coordenadas
```

#### **Outros tipos de dados**

``` py
dados = ("Abel", 25, True)
nome, idade, ativo = dados
```

### **Checklist**

Ao final desta aula, você aprendeu:

- O que é _unpacking_?
- Como extrair valores de _listas_ e _tuplas_
- Como atribuir múltiplos valores em uma única linha
- Como melhorar a legibilidade do código

O _unpacking_ é um recurso simples, mas muito útil para escrever códigos mais limpos e organizados.
