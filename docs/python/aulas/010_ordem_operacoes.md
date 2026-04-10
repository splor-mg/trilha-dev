---
comments: true
---
# Aula 010: Ordem de precedência de operações matemáticas.

## 🎥 Vídeo 10

Nesta aula, vamos aprender sobre a ordem na qual as operações aritméticas são executadas, lembrando conceitos matemáticos importantes para a previsibilidade dos resultados de tais operações.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UytgXC8f6To?si=KIjAX6UYicpqqfQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Exemplo inicial**

Considere a seguinte expressão:

``` py
x = 10 + 3 * 2
print(x)
```

Antes de executar é importante entender qual operação será realizada primeiro.

#### **Regra de precedência**

A multiplicação tem precedência sobre a adição. Portanto:

``` py
- Primeiro: 3 * 2 = 6
- Depois: 10 + 6 = 16
```

Ao executar o código, o resultado será:

``` py
16
```

#### **Ordem de precedência completa**

A ordem das operações em Python segue a regra matemática:

1.  Exponenciação: **\*\***
2.  Multiplicação e divisão: **\***, **/**, **//**, **%**
3.  Adição e subtração: **+**, **-**

O Python executa as operações respeitando essa hierarquia.

#### **Uso de parênteses**

Os parênteses podem alterar a ordem de execução, pois têm prioridade máxima.

Exemplo:

``` py
x = (10 + 3) * 2 ** 2
print(x)
```

Ordem de execução:

- Primeiro: (10 + 3) = 13 - **(Parênteses)**
- Depois: 2 ** 2 = 4 - **(Expoente)**
- Por fim: 13 * 4 = 52 - **(Multiplicação)**

Resultado:
``` py
52
```

#### **Importância dos parênteses**

O uso de **parênteses** permite:

- Controlar a ordem das operações
- Evitar ambiguidades
- Garantir resultados corretos

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como funciona a precedência de operações
- A ordem padrão de execução no Python
- O papel da exponenciação na hierarquia
- Como usar parênteses para alterar a ordem

Esses conceitos são essenciais para evitar erros em cálculos e garantir que o programa produza os resultados esperados.

#### 💡 **Dica**

Existe o mnemônico **PEMDAS** para lembrar a ordem das operações matemáticas, essencial para resolver expressões numéricas corretamente: Parênteses, Expoentes, Multiplicação e Divisão (da esquerda para a direita), Adição e Subtração (da esquerda para a direita). Seguir essa sequência garante que todos cheguem ao mesmo resultado, evitando erros de prioridade.
