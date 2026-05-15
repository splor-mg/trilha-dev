---
comments: true
---
# Aula 035: Gerando valores aleatórios

## 🎥 Vídeo 35

Nesta aula, vamos aprender a usar o módulo `random`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QE7-pyUERwY?si=wcdavt20sm3nAyTA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### **O que são módulos `built-in`?**

Os módulos *built-in* são módulos que já vêm instalados junto com o Python. Isso significa que não precisamos criar esses módulos manualmente nem instalar bibliotecas externas para utilizá-los.

Esses módulos oferecem funções e classes prontas para diversas tarefas, como:

- geração de números aleatórios;
- manipulação de datas;
- operações matemáticas;
- envio de e-mails;
- conversão de dados;
- geração de senhas;
- entre muitas outras funcionalidades.

#### **Onde encontrar os módulos do Python?**

A documentação oficial do Python possui uma lista com todos os módulos disponíveis.

Pesquisando por:

```text
Python 3 module index
```

É possível acessar o índice completo dos módulos da linguagem.

É importante pesquisar pela versão correta do Python, pois os módulos disponíveis no Python 2 e no Python 3 possuem diferenças.

#### **Importando um módulo `built-in`**

Nesta aula foi utilizado o módulo `random`, responsável por gerar valores aleatórios.

Para importar um módulo built-in, basta utilizar o comando `import`:

```python
import random
```

Diferente dos módulos criados por nós, não é necessário possuir uma pasta ou arquivo chamado `random` no projeto, pois esse módulo já faz parte da instalação do Python.

#### **Gerando números aleatórios com `random.random()`**

A função `random.random()` gera números aleatórios entre `0` e `1`.

Exemplo:

```python
import random

for i in range(3):
    print(random.random())
```

#### **Possível saída**

```text
0.2451
0.8745
0.1923
```

Cada execução gera valores diferentes.

#### **Revisão do `for` com `range`**

Durante a aula foi reforçada a estrutura correta de um `for`:

```python
for i in range(3):
    print(i)
```

#### **Pontos importantes**

- utilizar `in`;
- utilizar `range()`;
- adicionar `:` no final da linha;
- identar o conteúdo do bloco.

#### **Gerando números inteiros aleatórios com `randint`**

A função `randint()` gera números inteiros dentro de um intervalo definido.

Exemplo

```python
import random

for i in range(3):
    print(random.randint(10, 20))
```

#### **Possível saída**

```text
20
18
17
```

Os números gerados estarão sempre entre `10` e `20`.

#### **Sorteando elementos de uma lista com `choice`**

A função `choice()` permite escolher aleatoriamente um item de um objeto iterável, como listas.

Exemplo

```python
import random

equipe = [
    "Ana",
    "Fernando",
    "Felipe",
    "Tadeu"
]

responsavel = random.choice(equipe)

print(responsavel)
```

#### **Possível saída**

```text
Felipe
```

A cada execução, um nome diferente pode ser selecionado.

#### **Aplicações práticas**

Com os conhecimentos aprendidos até aqui, já é possível desenvolver aplicações simples, como:

- jogos de bingo;
- sistemas de sorteio;
- rifas;
- conversores de temperatura;
- conversores de moeda;
- conversores de unidades;
- pequenos jogos;
- automações simples.

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são módulos built-in?;
- Onde encontrar a documentação oficial dos módulos do Python?;
- Como importar módulos com `import`;
- Como utilizar o módulo `random`;
- Como gerar números aleatórios;
- Como sortear valores de listas;
- Como reutilizar funcionalidades já existentes no Python.

## Desafio Bingo

### Orientações

<iframe width="560" height="315" src="https://www.youtube.com/embed/lQKgGHwWoE4?si=aHMXGgvx_P6h-hdZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Resolução

<iframe width="560" height="315" src="https://www.youtube.com/embed/n6jHge3-SMI?si=qCjpUkbn5rEmu8vX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>