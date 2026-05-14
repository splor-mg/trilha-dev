---
comments: true
---
# Aula 029: Comentários

## 🎥 Vídeo 29

Nesta aula, vamos aprender como fazer comentários no nosso código.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HSVRrif2d2k?si=lWvbo4s1IOiyCRax" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são comentários?**

Comentários são trechos do código que não são executados pelo Python.

Eles servem para:

- Fazer anotações
- Criar lembretes
- Explicar decisões do código
- Facilitar a leitura para outras pessoas

#### **Como criar comentários**

Em Python, comentários são iniciados com `#`.

Exemplo:

``` py
# Este é um comentário
```

Tudo o que estiver após `#` será ignorado pelo interpretador.

#### **Exemplo de comentário**

``` py
# Corrigir variável x depois
```

Também podemos utilizar comentários para criar lembretes durante o desenvolvimento.

#### **O interpretador ignora comentários**

Exemplo:

``` py
# Isso não será executado

print("Olá")
```

Resultado:

``` py
Olá
```

#### **Por que comentários são importantes?**

Comentários ajudam outras pessoas a entenderem:

- Decisões tomadas no código
- Regras importantes
- Informações temporárias
- Pontos que ainda precisam ser ajustados

#### **Quando usar comentários**

Comentários são úteis para:

- Explicar o motivo de uma decisão
- Criar lembretes
- Informar comportamentos importantes
- Facilitar manutenção futura

Exemplo:

``` py
# Utilizamos essa lógica para evitar divisão por zero
```

#### **O que evitar nos comentários?**

Não é recomendado usar comentários para descrever exatamente o que o código já mostra.

#### **Exemplo de comentário ruim**

``` py
# Informa que o céu é azul
print("O céu é azul")
```

Nesse caso, o comentário é desnecessário porque o código já é claro.

#### **Outro exemplo ruim**

``` py
def soma(numero1, numero2):
    # Soma numero1 e numero2
    return numero1 + numero2
```

O nome da função e o próprio código já explicam o comportamento.

#### **Por que evitar comentários redundantes?**

Comentários desnecessários:

- Poluem o código
- Tornam a leitura mais difícil
- Criam redundância
- Exigem manutenção extra

#### **Problema de manutenção**

Imagine este código:

``` py
# Informa que o céu é azul
print("O céu é azul")
```

Se o texto mudar:

``` py
print("O mar é azul")
```

O comentário também precisará ser alterado.

Isso aumenta o trabalho de manutenção.

#### **O código deve ser claro**

Um código bem escrito deve ser compreensível sem precisar de comentários explicando cada linha.

Por isso:

- Use nomes claros
- Organize bem o código
- Evite comentários repetitivos

Prefira comentários que expliquem:

- O motivo de algo existir
- Regras importantes
- Decisões específicas
- Contextos que não estão óbvios no código

#### **Exemplo de comentário útil**

``` py
# Mantemos esse cálculo separado para facilitar futuras alterações
valor_total = subtotal + taxa
```

#### **Aplicação prática**

Ao escrever comentários:

- Seja objetivo
- Evite excesso de comentários
- Não explique o óbvio
- Pense em quem vai ler o código depois

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são comentários?;
- Como criar comentários com `#`;
- Quando utilizar comentários;
- O que evitar nos comentários?;
- Como escrever comentários mais úteis;
- Boas práticas de legibilidade.

Comentários devem ajudar a tornar o código mais claro, e não mais confuso ou repetitivo.