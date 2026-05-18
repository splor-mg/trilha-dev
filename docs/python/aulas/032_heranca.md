---
comments: true
---
# Aula 032: Herança

## 🎥 Vídeo 32

Nesta aula, vamos aprender sobre herança na criação de Classes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IQRBa3pPsjY?si=QC01h9YTRS9NTehO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é herança?**

Herança é um mecanismo da programação orientada a objetos que permite que uma classe herde atributos e métodos de outra classe. Isso evita repetição de código e facilita a reutilização de comportamentos comuns entre diferentes classes.

#### **Criando uma classe simples**

Primeiro, foi criada uma classe chamada `Cachorro` com um método `passear`.

```python
class Cachorro:
    def passear(self):
        print("Passear")
```

#### **Repetição de código**

Depois, foi criada uma classe `Gato` com exatamente o mesmo método.

```python
class Gato:
    def passear(self):
        print("Passear")
```

Nesse caso, o código ficou repetido.
Se esse método tivesse dezenas ou centenas de linhas, seria trabalhoso manter tudo duplicado.

#### **Princípio DRY**

A aula apresenta o princípio **DRY**:

> **Don't Repeat Yourself**  
> Não repita a si mesmo.

A ideia é evitar redundância no código.

#### **Criando uma classe pai**

Para resolver a repetição, foi criada uma classe mais genérica chamada `Animal`.

```python
class Animal:
    def passear(self):
        print("Passear")
```

Agora, as outras classes podem herdar esse comportamento.

#### **Criando classes filhas**

As classes `Cachorro` e `Gato` passam a herdar da classe `Animal`.

```python
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass
```

A sintaxe da herança funciona colocando a classe pai entre parênteses.

#### **O uso do `pass`**

Como as classes ficaram vazias, foi utilizado o `pass`.

```python
pass
```

O `pass` funciona como um placeholder e indica ao Python que aquela classe existe, mesmo sem implementação no momento.

#### **Herdando métodos**

Mesmo sem definir o método `passear` dentro de `Cachorro`, o objeto consegue utilizá-lo porque herdou da classe `Animal`.

```python
caramelo_um = Cachorro()

caramelo_um.passear()
```

Saída:

```python
Passear
```

#### **Métodos exclusivos da classe filha**

Além dos métodos herdados, cada classe filha também pode ter métodos próprios. Foi adicionado um método `latir` apenas na classe `Cachorro`.

```python
class Cachorro(Animal):

    def latir(self):
        print("Au au")
```

Agora o objeto consegue usar tanto o método herdado quanto o método exclusivo.

```python
caramelo_um = Cachorro()

caramelo_um.passear()
caramelo_um.latir()
```

Saída:

```python
Passear
Au au
```

#### **Classe pai e classe filha**

Na herança:

- `Animal` é a **classe pai**
- `Cachorro` e `Gato` são as **classes filhas**

Tudo que estiver definido na classe pai pode ser utilizado pelas classes filhas.

#### **Aplicação prática**

A herança ajuda a:

- evitar repetição de código
- reutilizar comportamentos
- facilitar manutenção
- organizar melhor o sistema
- criar estruturas mais reutilizáveis

#### **Checklist**

Ao final desta aula, você aprendeu:

- Criação de classes pai e filha;
- Reutilização de métodos;
- Uso do princípio DRY;
- Uso do `pass`;
- Criação de métodos específicos em subclasses.

A herança é um dos pilares da programação orientada a objetos e será utilizada frequentemente em projetos maiores.