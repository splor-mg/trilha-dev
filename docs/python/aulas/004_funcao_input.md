---
comments: true
---
# Aula 004: Função input

## 🎥 Vídeo 4

Nesta aula, nós vamos aprender como podemos receber informações digitadas pelo usuário através do terminal com a função **`input`**.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sgebdUm6ZIc?si=IFXXNmpJR6zKq_iE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Entrada e saída de dados**

Até agora foi utilizada a função **print()** para exibir informações na tela.

Com a função **input()**, passa a ser possível receber dados digitados pelo usuário, permitindo uma interação mais completa.

#### **Utilizando a função input()**

A função **input()** exibe uma mensagem e aguarda o usuário digitar uma resposta.

Exemplo:

``` py
nome = input("Qual o seu nome? ")
```

O valor digitado será armazenado na variável **nome**.
O espaço ao final da mensagem serve para melhorar a visualização, evitando que o texto digitado fique colado na pergunta.

#### **Exibindo uma mensagem personalizada**

Após receber o valor é possível utilizá-lo em outras partes do programa:

``` py
print("Olá, " + nome)
```

Neste caso, a mensagem exibida será personalizada com o nome informado pelo usuário.

#### **Concatenação de strings**

A operação utilizada para juntar textos é chamada de **concatenação**.
Ela ocorre quando utilizamos o operador **+** para unir:

- Um texto fixo _(string)_
- Um valor armazenado em variável (também _string_)

O resultado é uma nova _string_ combinando os dois elementos.

#### **Fluxo de execução**

Ao executar o programa:

1.  O Python solicita o nome do usuário;
2.  Aguarda a digitação;
3.  Armazena o valor na variável;
4.  Exibe a mensagem personalizada.

Esse processo segue a ordem de execução do código (de cima para baixo).

#### **Checklist**

Ao final desta aula você aprendeu:

- Como utilizar a função **input()**
- Como receber dados do usuário
- Como armazenar essas informações em variáveis
- Como combinar textos com concatenação
- Como criar interações simples no terminal

Esse é um passo importante para desenvolver programas mais dinâmicos e interativos.
