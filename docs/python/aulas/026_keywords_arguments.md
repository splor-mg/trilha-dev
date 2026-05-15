---
comments: true
---
# Aula 026: Parâmetros

## 🎥 Vídeo 26

Nesta aula, vamos aprender sobre argumentos chaves de funções.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DcblJZ2erHY?si=FRxCtJJqbifYn4wJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são argumentos em funções?**

Na aula anterior, aprendemos sobre parâmetros em funções. Agora vamos entender os **argumentos**, que são os valores enviados para esses parâmetros no momento da execução da função.

#### **Parâmetros e argumentos**

Exemplo:

``` py
def apresentar(nome, sobrenome):
    print(nome, sobrenome)
```

Nesse caso:

- `nome` e `sobrenome` são os **parâmetros**

Ao executar:

``` py
apresentar("Maria", "Abreu")
```

- `"Maria"` e `"Abreu"` são os **argumentos**

#### **Argumentos posicionais**

Por padrão, os argumentos seguem a ordem definida nos parâmetros.

Exemplo:

``` py
apresentar("Maria", "Abreu")
```

O Python interpreta assim:

``` py
nome = "Maria"
sobrenome = "Abreu"
```

#### **A ordem importa**

Se invertermos os valores:

``` py
apresentar("Abreu", "Maria")
```

Resultado:

``` py
Abreu Maria
```

Nesse caso:

``` py
nome = "Abreu"
sobrenome = "Maria"
```

Ou seja, a ordem altera o resultado.

#### **Erro ao faltar argumentos**

Se não enviarmos todos os argumentos necessários:

``` py
apresentar("Maria")
```

O Python gera erro, porque a função espera dois argumentos.

#### **Argumentos com palavras-chave (_keyword arguments_)**

Também podemos informar explicitamente qual valor pertence a cada parâmetro.

``` py
apresentar(
    nome="Maria",
    sobrenome="Abreu"
)
```

#### **A ordem deixa de importar**

Quando utilizamos palavras-chave, a posição não é mais obrigatória.

``` py
apresentar(
    sobrenome="Abreu",
    nome="Maria"
)
```

Resultado:

``` py
Maria Abreu
```

O Python entende corretamente qual valor pertence a cada parâmetro.

#### **Quando utilizar argumentos com palavras-chave?**

Esse formato é útil principalmente quando:

- A função possui muitos parâmetros
- Os valores não são tão claros
- Queremos melhorar a legibilidade do código

#### **Exemplo prático**

Imagine uma função de compras online:

``` py
def calcular_custo(
    total_compra,
    valor_entrega,
    desconto
):
    pass
```

Sem palavras-chave:

``` py
calcular_custo(100, 15, 10)
```

Pode ser difícil entender o que cada número representa.

Com palavras-chave:

``` py
calcular_custo(
    total_compra=100,
    valor_entrega=15,
    desconto=10
)
```

O código fica muito mais legível.

#### **Misturando argumentos posicionais e palavras-chave**

Uma função pode utilizar os dois formatos.

Mas existe uma regra importante:

- Argumentos posicionais devem vir primeiro

Exemplo correto:

``` py
funcao(10, nome="Maria")
```

Exemplo incorreto:

``` py
funcao(nome="Maria", 10)
```

Isso gera erro no Python.

#### **Aplicação prática**

Ao trabalhar com argumentos:

- Utilize palavras-chave em funções complexas
- Prefira legibilidade
- Use nomes claros nos parâmetros
- Evite funções confusas

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são argumentos?;
- A diferença entre parâmetros e argumentos;
- O que são argumentos posicionais;
- Como funcionam os _keyword arguments_;
- Quando utilizar palavras-chave;
- Como melhorar a legibilidade do código;
- A regra sobre ordem dos argumentos.

Os argumentos com palavras-chave ajudam a criar códigos mais claros, organizados e fáceis de manter.