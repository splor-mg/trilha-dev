---
comments: true
---
# Aula 024: Funções

## 🎥 Vídeo 24

Nesta aula, vamos aprender sobre funções.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_VkF6lA4tZI?si=d_Fpul1zy7VGnx1l" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Conteúdo extra

??? tip "Será que você vai passar nesse desafio?"

    <iframe width="560" height="315" src="https://www.youtube.com/embed/gsKDsdJp2zk?si=CCnMpmoEXUnjWsBB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são funções?**

As funções em Python são blocos de código reutilizáveis que executam uma tarefa específica. Elas ajudam a organizar o código, evitar repetições e facilitar a manutenção do sistema.

#### **Por que utilizar funções?**

Imagine um sistema com vários módulos. Sempre que o usuário acessar um módulo, queremos exibir uma mensagem de boas-vindas.

Ao invés de repetir o mesmo código várias vezes, podemos criar uma função.

#### **Exemplo sem função**

``` py
print("Olá!")
print("Bem-vindo ao sistema!")

print("Olá!")
print("Bem-vindo ao sistema!")
```

Nesse caso, o código fica repetitivo.

#### **Criando uma função**

Para criar uma função, utilizamos a palavra reservada `def`.

``` py
def boas_vindas():
    print("Olá!")
    print("Bem-vindo ao sistema!")
```

#### **Estrutura da função**

Uma função possui:

- `def` → indica a criação da função
- Nome da função
- Parênteses `()`
- Dois pontos `:`
- Bloco de código indentado

#### **Aplicação prática**

Ao criar funções:

- Utilize letras minúsculas
- Use nomes descritivos
- Separe palavras com `_`

Exemplo:

``` py
def calcular_media():
    pass
```

Evite nomes sem significado:

``` py
def abobrinha():
    pass
```

#### **Executando a função**

Criar a função não significa executá-la.
Para executar, chamamos a função pelo nome:

``` py
boas_vindas()
```

Resultado:

``` py
Olá!
Bem-vindo ao sistema!
```

#### **Indentação nas funções**

Todo código pertencente à função deve ficar indentado.

Exemplo correto:

``` py
def boas_vindas():
    print("Olá!")
```

Exemplo incorreto:

``` py
def boas_vindas():
print("Olá!")
```

#### **Funções ajudam na reutilização**

Depois de criada, a função pode ser utilizada várias vezes no programa:

``` py
boas_vindas()
boas_vindas()
boas_vindas()
```

Isso evita repetição de código.

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são funções?;
- Para que servem as funções;
- Como criar uma função com `def`;
- Como nomear funções corretamente;
- Como executar uma função;
- A importância da indentação;
- Como reutilizar código com funções.

As funções são fundamentais em Python e ajudam a escrever códigos mais organizados, reutilizáveis e fáceis de manter.
