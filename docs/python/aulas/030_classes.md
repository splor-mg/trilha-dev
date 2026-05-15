---
comments: true
---
# Aula 030: Classes

## 🎥 Vídeo 30

Nesta aula, vamos aprender sobre criação de Classes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nwKZWzNISpA?si=seFGuTbvqzi_S_nq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que são classes?**

Classes são estruturas utilizadas para criar novos tipos de objetos dentro do programa. Outras linguagens de programação também utilizam classes como base da programação orientada a objetos.

Em Python, vários tipos que já utilizamos são classes, como:

- `int`
- `bool`
- `list`
- `str`

#### **Métodos em objetos**

Objetos possuem métodos, que são funções específicas daquele tipo de dado.

Exemplo com listas:

```py
lista = [1, 2, 3]

lista.append(4)
```

Nesse caso:

- `append()` é um método da lista
- O método modifica o objeto `lista`

Outros métodos conhecidos:

```py
lista.pop()
lista.remove(2)
```

#### **Criando nossas próprias classes**

O Python permite criar nossas próprias classes e métodos.

Exemplo:

```py
class Aluno:
    pass
```

#### **Definindo uma classe**

Para criar uma classe, utilizamos:

```py
class NomeDaClasse:
```

Exemplo:

```py
class Aluno:
```

#### **Padrão de nomenclatura**

Classes normalmente utilizam:

- Primeira letra maiúscula
- Padrão `PascalCase`

Exemplos:

```py
class Aluno:
```

```py
class AlunoMatriculado:
```

Diferente das variáveis, normalmente não utilizamos `_` entre palavras no nome das classes.

#### **Criando métodos**

Métodos são funções definidas dentro da classe.

Exemplo:

```py
class Aluno:

    def aprovar(self):
        print("Aprovado")
```

#### **O parâmetro `self`**

Nos métodos, utilizamos o parâmetro `self`.

Exemplo:

```py
def aprovar(self):
```

Neste momento, basta entender que ele representa o próprio objeto que está utilizando o método.

#### **Criando mais métodos**

Também podemos criar outros comportamentos:

```py
class Aluno:

    def aprovar(self):
        print("Aprovado")

    def reprovar(self):
        print("Reprovado")
```

#### **Métodos representam comportamentos**

Os métodos definem ações e comportamentos dos objetos.

Exemplo:

- Aprovar aluno
- Reprovar aluno
- Alterar turma
- Atualizar cadastro

#### **Criando objetos**

Objetos são criados a partir das classes.

Exemplo:

```py
aluno_um = Aluno()
```

Nesse caso:

- `Aluno` é a classe
- `aluno_um` é um objeto da classe

Esse processo é chamado de instanciação.

#### **Utilizando métodos**

Depois de criar o objeto, podemos executar seus métodos:

```py
aluno_um.aprovar()
```

Resultado:

```py
Aprovado
```

#### **Métodos utilizam parênteses**

Como métodos são funções, precisamos utilizar parênteses:

```py
aluno_um.aprovar()
```

Sem os parênteses, o método não é executado.

#### **O que são atributos?**

Além de métodos, objetos também possuem atributos.

Os atributos representam dados do objeto.

Exemplo:

```py
aluno_um.nome = "Maria"
```

```py
aluno_um.idade = 10
```

Nesse caso:

- `nome` é um atributo
- `idade` é um atributo

#### **Métodos x atributos**

Os métodos representam:

- Comportamentos
- Ações

Os atributos representam:

- Dados
- Características do objeto

#### **Acessando atributos**

Podemos acessar atributos utilizando `.`:

```py
print(aluno_um.nome)
```

Resultado:

```py
Maria
```

#### **Criando múltiplos objetos**

Podemos criar vários objetos da mesma classe:

```py
aluno_um = Aluno()
aluno_dois = Aluno()
```

Cada objeto possui seus próprios atributos.

#### **Objetos possuem dados independentes**

Exemplo:

```py
aluno_um.nome = "Maria"
```

Isso não significa que `aluno_dois` também terá `nome`.

Se tentarmos acessar:

```py
print(aluno_dois.nome)
```

Resultado:

```py
AttributeError
```

Isso acontece porque o atributo não foi definido para esse objeto.

#### **Adicionando atributos em outro objeto**

Podemos adicionar atributos separadamente:

```py
aluno_dois.idade = 10
```

Depois disso:

```py
print(aluno_dois.idade)
```

Resultado:

```py
10
```

#### **Resumo da estrutura**

Exemplo completo:

```py
class Aluno:

    def aprovar(self):
        print("Aprovado")

    def reprovar(self):
        print("Reprovado")


aluno_um = Aluno()

aluno_um.nome = "Maria"
aluno_um.idade = 10

aluno_um.aprovar()

print(aluno_um.nome)
```

Resultado:

```py
Aprovado
Maria
```

#### **Por que utilizar classes?**

Classes ajudam a:

- Organizar o código
- Reutilizar comportamentos
- Modelar dados
- Criar sistemas mais complexos
- Facilitar manutenção

#### **Aplicação prática**

Classes são muito utilizadas para representar elementos do mundo real.

Exemplos:

- Usuários
- Produtos
- Alunos
- Contas bancárias
- Funcionários
- Pedidos

#### **Checklist**

Ao final desta aula, você aprendeu:

- O que são classes?;
- O que são objetos?;
- Como criar classes em Python;
- Como criar métodos;
- O que é o `self`?;
- Como instanciar objetos;
- O que são atributos?;
- Diferença entre métodos e atributos;
- Como acessar métodos e atributos com `.`.

As classes são fundamentais para a programação orientada a objetos e permitem criar sistemas mais organizados, reutilizáveis e próximos da realidade.