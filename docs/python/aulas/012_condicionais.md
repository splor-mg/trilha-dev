---
comments: true
---
# Aula 012: Uso de condicionais

## 🎥 Vídeo 12

Nesta aula, vamos aprender sobre como criar estruturas condicionais no nosso código, usando o `if`, `elif` e o `else`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/cMzIDqnPyS8?si=wcJYmGSWTMR-46Ny" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são condicionais?**

Condicionais permitem que o programa tome decisões com base em condições.
Ou seja, o código pode seguir caminhos diferentes dependendo se uma condição é _verdadeira_ ou _falsa_.

#### **Exemplo inicial**

Vamos criar uma variável _booleana_:

``` py
esta_quente = True
```

Agora, utilizamos a estrutura **if**:

``` py
if esta_quente:
  print("O dia está quente")
  print("Beba água")

print("Tenha um bom dia")
```

Comportamento:

- Se **esta_quente** for **True** as mensagens dentro do **if** serão exibidas;
- A mensagem _"Tenha um bom dia"_ será exibida sempre, pois está fora do bloco.

Se alterarmos:

``` py
esta_quente = False
```

Apenas _"Tenha um bom dia"_ será exibido.

#### **Utilizando elif**

Podemos adicionar outra condição:

``` py
esta_frio = True

if esta_quente:
  print("O dia está quente")
  print("Beba água")

elif esta_frio:
  print("O dia está frio")
  print("Use agasalho")

print("Tenha um bom dia")
```

O Python:

- Verifica primeiro o **if**;
- Se for _falso_, verifica o **elif**;
- Executa apenas o primeiro bloco _verdadeiro_.

#### **Utilizando else**

Para tratar o caso em que nenhuma condição é _verdadeira_:

``` py
if esta_quente:
  print("O dia está quente")
  print("Beba água")

elif esta_frio:
  print("O dia está frio")
  print("Use agasalho")

else:
  print("É um lindo dia")
print("Tenha um bom dia")
```

Nesse caso:

- Se nenhuma condição for _verdadeira_, o bloco **else** será executado.

#### **Estrutura geral**

A estrutura condicional em Python segue o padrão:

``` py
if condicao:
# código

elif outra_condicao:
# código

else:
# código
```

#### **Importância da indentação**

A indentação define quais linhas pertencem a cada bloco.

- Código _indentado_ → pertence à condição
- Código _sem indentação_ → executado independentemente

#### **Checklist**

Ao final desta aula, você aprendeu:

- Como utilizar **if**, **elif** e **else**
- Como o Python avalia condições
- Como controlar o fluxo do programa
- A importância da _indentação_

Estruturas condicionais são fundamentais para criar programas com lógica e tomada de decisão.
