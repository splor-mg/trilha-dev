---
comments: true
---
# Aula 013: Operadores lógicos

## 🎥 Vídeo 13

Nesta aula, vamos aprender sobre operadores lógicos na estrutura do nosso código, usando o `and`, `or` e o `not`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9ezYrH9J_E8?si=Svnn_V3OFrmH-0Km" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Nesta aula, você vai aprender a utilizar operadores lógicos para criar condições mais complexas em seus programas.

#### **Operadores lógicos**

Os principais operadores lógicos em Python são:

``` py
- and
- or
- not
```

Eles permitem combinar condições e estruturar regras dentro do código.

#### **Operador _and_**

O operador **_and_** exige que todas as condições sejam verdadeiras.

Exemplo:

``` py
tem_alta_renda = True
tem_bom_credito = True

if tem_alta_renda and tem_bom_credito:
  print("Elegível para empréstimo")
```

Neste caso:

- Ambas as condições precisam ser _True_;
- Se uma delas for _False_, nada será exibido.

#### **Operador _or_**

O operador **_or_** exige que pelo menos uma condição seja verdadeira.

Exemplo:

``` py
tem_alta_renda = True
tem_bom_credito = False

if tem_alta_renda or tem_bom_credito:
  print("Elegível para empréstimo")
```

Neste caso:

- Basta uma condição ser _True_;
- Se ambas forem _False_, nada será exibido

#### **Operador _not_**

O operador **_not_** inverte o valor lógico.

Exemplo:

``` py
tem_alta_renda = True
tem_historico_criminal = False

if tem_alta_renda and not tem_historico_criminal:
  print("Elegível para empréstimo")
```

Comportamento:

```py
- not False → True
- not True → False
```

Se _tem_historico_criminal_ for _True_, a condição não será satisfeita.

#### **Resumo**

- **_and_** → todas as condições devem ser verdadeiras;
- **_or_** → pelo menos uma condição deve ser verdadeira;
- **_not_** → inverte o valor lógico.

#### **Conclusão**

Ao final desta aula, você aprendeu:

- Como combinar condições com operadores lógicos
- Como utilizar _and_, _or_ e _not_
- Como estruturar regras mais complexas no código

Esses operadores são fundamentais para criar validações e regras de negócio em programas.
