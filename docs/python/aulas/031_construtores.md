---
comments: true
---
# Aula 031: Construtores

## 🎥 Vídeo 31

Nesta aula, vamos aprender sobre construtores na criação de Classes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qv6RkijUglk?si=rzEx5tQKY_z3jHTH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são construtores em classes?**

Na aula anterior, vimos como criar classes, métodos e atributos em Python. Nesta, o foco é entender os **construtores**, que permitem definir automaticamente os atributos de um objeto no momento em que ele é criado.

#### **Relembrando uma classe simples**

Exemplo:

```py
class Aluno:

    def aprovar(self):
        print("Aprovado")

    def reprovar(self):
        print("Reprovado")
```

Essa classe possui dois métodos:

- `aprovar()`
- `reprovar()`

#### **Criando objetos da classe**

Podemos criar objetos assim:

```py
aluno_um = Aluno()
aluno_dois = Aluno()
```

Na aula anterior, os atributos eram adicionados manualmente:

```py
aluno_um.nome = "Maria"
aluno_um.idade = 10
```

Isso funciona, mas pode gerar repetição no código.

#### **O problema da criação manual de atributos**

Quando os atributos são adicionados manualmente:

```py
aluno_um.nome = "Maria"
aluno_um.idade = 10
```

Precisamos repetir esse processo para todos os objetos criados.

Além disso:

- Um objeto pode acabar sem atributos importantes;
- Não existe uma padronização garantida;
- O código fica mais repetitivo.

#### **O que é um construtor?**

O construtor é um método especial executado automaticamente quando um objeto é criado.

Em Python, o construtor é definido com:

```py
__init__
```

Esse método é chamado automaticamente ao iniciar um objeto da classe.

#### **Criando um construtor**

Exemplo:

```py
class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

Nesse exemplo:

- `__init__` é o construtor;
- `nome` e `idade` são parâmetros recebidos;
- `self.nome` e `self.idade` criam atributos no objeto.

#### **O que significa `self`?**

O `self` representa o próprio objeto que está sendo criado.

Exemplo:

```py
self.nome = nome
```

Isso significa:

- criar um atributo chamado `nome` no objeto;
- armazenar nele o valor recebido no parâmetro `nome`.

#### **Criando objetos com construtor**

Agora, ao criar um objeto, precisamos informar os valores exigidos pelo construtor:

```py
aluno_um = Aluno("Ana", 14)
```

Nesse caso:

- `"Ana"` será o nome;
- `14` será a idade.

#### **O que acontece se faltar um argumento?**

Se tentarmos criar o objeto sem os parâmetros:

```py
aluno_um = Aluno()
```

O Python gera erro:

```py
TypeError
```

Isso acontece porque o construtor exige:

- `nome`
- `idade`

#### **Acessando atributos do objeto**

Depois de criar o objeto:

```py
aluno_um = Aluno("Ana", 14)
```

Podemos acessar os atributos:

```py
print(aluno_um.nome)
print(aluno_um.idade)
```

Resultado:

```py
Ana
14
```

#### **Adicionando mais atributos**

Também podemos adicionar novos atributos no construtor.

Exemplo:

```py
class Aluno:

    def __init__(self, nome, idade, escola):
        self.nome = nome
        self.idade = idade
        self.escola = escola
```

Agora o objeto precisa receber:

- nome;
- idade;
- escola.

#### **Criando um objeto com vários atributos**

Exemplo:

```py
aluno_um = Aluno("Ana", 14, "Escola Um")
```

Acessando os valores:

```py
print(aluno_um.nome)
print(aluno_um.idade)
print(aluno_um.escola)
```

Resultado:

```py
Ana
14
Escola Um
```

#### **Alterando atributos depois da criação**

Os atributos podem ser modificados posteriormente.

Exemplo:

```py
aluno_um.idade = 15
```

Depois:

```py
print(aluno_um.idade)
```

Resultado:

```py
15
```

#### **Métodos continuam funcionando**

Mesmo usando construtores, os métodos da classe continuam disponíveis.

Exemplo:

```py
class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aprovar(self):
        print("Aprovado")
```

Executando:

```py
aluno_um = Aluno("Ana", 14)

aluno_um.aprovar()
```

Resultado:

```py
Aprovado
```

#### **Classe como “blueprint”**

Uma classe funciona como um modelo (blueprint) para criação de objetos.

Ela define:

- quais atributos os objetos terão;
- quais métodos poderão executar;
- como esses objetos serão organizados.

#### **Curiosidade sobre `self`**

A palavra `self` é apenas uma convenção.

Tecnicamente, outro nome poderia ser utilizado:

```py
def __init__(meu_objeto, nome):
    meu_objeto.nome = nome
```

Isso funciona normalmente. Porém, a convenção da comunidade Python é utilizar `self`.
Isso deixa o código mais padronizado e fácil de entender.

#### **Aplicação prática**

Os construtores ajudam a:

- padronizar objetos;
- evitar repetição;
- garantir atributos obrigatórios;
- organizar melhor o código;
- facilitar manutenção do sistema.

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que é um construtor?;
- Como utilizar `__init__`;
- O papel do `self`;
- Como criar atributos automaticamente;
- Como criar objetos com parâmetros;
- Como acessar atributos;
- Como alterar atributos;
- Como os métodos continuam funcionando;
- O conceito de classe como blueprint.

Os construtores são fundamentais na programação orientada a objetos, pois permitem criar objetos mais organizados, padronizados e reutilizáveis.