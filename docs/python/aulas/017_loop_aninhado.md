---
comments: true
---
# Aula 017: Loop Aninhados

## 🎥 Vídeo 17

Nesta aula, vamos aprender sobre loops aninhados ou _nested loops_.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yixWM5RtWs?si=JugZGikmzdwcw3NG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender sobre loops aninhados, ou seja, quando utilizamos um loop dentro de outro.

#### **O que são _loops aninhados_**

_Loops aninhados_ acontecem quando um loop está dentro de outro.

Essa estrutura é utilizada quando precisamos repetir uma ação múltiplas vezes dentro de outra repetição.

#### **Exemplo com coordenadas**

Vamos supor que queremos exibir coordenadas no formato:

``` py
- (0,0), (0,1), (0,2)
- (1,0), (1,1), (1,2)
- (2,0), (2,1), (2,2)
- (3,0), (3,1), (3,2)
```

Para isso, utilizamos dois loops:

``` py
for x in range(4): # 0 -3
    for y in range(3):
        print(f' ({x}, {y}) ')
```

#### **Funcionamento**

O Python executa da seguinte forma:

``` py
1.  Inicia o loop externo (x = 0)
2.  Executa completamente o loop interno (y = 0, 1, 2)
3.  Incrementa o x (x = 1)
4.  Executa novamente o loop interno
5.  Repete até finalizar o loop externo
```

Ou seja, o loop interno é executado completamente a cada iteração do loop externo.

#### **Visualizando a execução**

Resultado esperado:

``` py
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
```

#### **Aplicação prática**

_Loops aninhados_ são muito utilizados para comparar dados.

Exemplo:

``` py
- Lista A: "banana", "maçã", "pera"
- Lista B: "maçã", "uva", "abacaxi"
```

A lógica seria:

``` py
- Para cada item da lista A
- Percorrer todos os itens da lista B
- Verificar se há correspondência
```

Esse tipo de estrutura é comum em validações e processamento de dados.

#### **Conclusão**

Ao final desta aula você aprendeu:

- O que são _loops aninhados_
- Como utilizar **_for_** dentro de **_for_**
- Como funciona a execução dos loops
- Aplicações práticas dessa estrutura

Esse conceito é importante para trabalhar com dados e resolver problemas mais complexos.