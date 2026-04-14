---
comments: true
---
# Aula 002: Como o um programa Python é executado

## 🎥 Vídeo 2

Neste vídeo, vamos aprender como um código python é executado e outros conceitos interessantes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0xAelPwq0Iw?si=iPepTSlngfnu3gMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Preparação do ambiente**

Com o ambiente já aberto:

- Acesse a pasta **aulas**
- Crie uma subpasta para esta aula (ex: **002**)
- Dentro dela, utilize o arquivo **app.py**
- No terminal, navegue até a pasta da aula utilizando o comando:

``` py
cd aulas/002
```

O comando **cd** permite navegar entre diretórios no sistema.

#### **Ordem de execução do Python**

O Python lê o código como nós: de cima para baixo e da esquerda para a direita.

Porém, existe um "pulo do gato" nas atribuições (o sinal de `=`). Quando o interpretador encontra um sinal de `=`, ele faz uma pausa - primeiro ele resolve toda a expressão que está à direita para, só depois, guardar o resultado na variável que ficou à esquerda. É por isso que, embora a leitura comece na esquerda, o cálculo final parece acontecer de trás para frente.

#### **Exemplo prático com múltiplos prints**

Utilizando a função **print()**, é possível exibir diferentes linhas no terminal:

``` py
print('O----')
print(' ////')
```

Ao executar o programa, cada **print()** será exibido em uma nova linha, respeitando a ordem em que foi escrito.

#### **Interpretador Python**

O interpretador é o responsável por:

- Ler o código escrito
- Traduzir para uma linguagem que o computador entende
- Executar as instruções
- Retornar o resultado no terminal

Compreender esse processo ajuda a prever o comportamento do programa.

#### **Introdução às _strings_**

Uma _string_ é qualquer sequência de caracteres dentro de aspas.

Exemplos:

``` py
print('Olá')
print('Texto qualquer')
print(' ')
```

Tudo que está entre aspas será interpretado como texto.

#### **Expressões e operadores**

O Python também avalia expressões antes de exibir o resultado.

Exemplo:

``` py
print(' * ' * 10)
```

Nesse caso:

- **' * '** é uma _string_
- **\*** é o operador de multiplicação
- **10** é o número de repetições

O resultado será a repetição da _string_ dez vezes na tela.

#### **O que é uma expressão?**

Uma **expressão** é qualquer instrução que produz um valor.

Antes de exibir o resultado, o Python:

1.  Avalia a expressão;
2.  Calcula o valor;
3.  Retorna o resultado.

Esse conceito é essencial para operações matemáticas e manipulação de dados.

#### **Checklist**

Ao final desta aula você aprendeu:

- Como o Python executa um programa
- A ordem de leitura do código
- O papel do interpretador
- O conceito de _string_
- Como funcionam expressões e operadores básicos

Esses fundamentos são importantes para começar a construir programas com lógica e previsibilidade.
