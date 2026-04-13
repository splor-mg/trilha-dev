---
comments: true
---
# Aula 017: Loop Aninhados

## 🎥 Vídeo 17

Nesta aula, vamos aprender sobre _loops aninhados_ ou _nested loops_.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yixWM5RtWs?si=JugZGikmzdwcw3NG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são _loops aninhados_?**

_Loops aninhados_ acontecem quando um _loop_ está dentro de outro.
Essa estrutura é utilizada quando precisamos repetir uma ação múltiplas vezes dentro de outra repetição.

#### **Exemplo com coordenadas**

Vamos supor que queremos exibir coordenadas no formato:

``` py
- (0,0), (0,1), (0,2)
- (1,0), (1,1), (1,2)
- (2,0), (2,1), (2,2)
- (3,0), (3,1), (3,2)
```

Para isso, utilizamos dois _loops_:

``` py
for x in range(4): # 0 -3
    for y in range(3):
        print(f' ({x}, {y}) ')
```

#### **Funcionamento**

O Python executa da seguinte forma:

1.  Inicia o _loop externo_ **(x = 0)**;
2.  Executa completamente o _loop interno_ **(y = 0, 1, 2)**;
3.  Incrementa o **x (x = 1)**;
4.  Executa novamente o _loop interno_;
5.  Repete até finalizar o _loop externo_.

Ou seja, o _loop interno_ é executado completamente a cada iteração do _loop externo_.

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

- Para cada item da lista A
- Percorrer todos os itens da lista B
- Verificar se há correspondência

Esse tipo de estrutura é comum em validações e processamento de dados.

#### **Checklist**

Ao final desta aula você aprendeu:

- O que são _loops aninhados_?
- Como utilizar **for** dentro de **for**
- Como funciona a execução dos _loops_
- Aplicações práticas dessa estrutura

Esse conceito é importante para trabalhar com dados e resolver problemas mais complexos.
