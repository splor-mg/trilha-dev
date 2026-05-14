---
comments: true
---
# Aula 034: Pacotes

## 🎥 Vídeo 34

Nesta aula, vamos aprender sobre pacotes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VUBAKaWtybQ?si=q8ck6KN_14Onqc--" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Conversa com o ChatGPT](https://chatgpt.com/share/69fa086e-26fc-83e9-9f21-57eaf8ef5540) sobre o erro encontrado na aula.

#### O que são pacotes?

Pacotes são uma forma de organizar o código Python em diretórios. Eles funcionam como “pastas especiais” que agrupam módulos relacionados. A ideia dos pacotes é facilitar a organização de projetos maiores, separando funcionalidades em diferentes partes do sistema.

#### Relação entre módulos e pacotes

Na aula anterior, foram apresentados os módulos, que são arquivos `.py`.

Os pacotes funcionam como agrupadores desses módulos.

A aula utiliza a analogia de uma loja de departamentos:

- o pacote seria a seção da loja;
- os módulos seriam os grupos internos daquela seção.

Por exemplo:

```python
# Seções da loja
homens
mulheres
infantil
```

Dentro de cada seção poderiam existir módulos como:

- sapatos;
- moda praia;
- vestuário;
- acessórios.

#### Por que usar pacotes?

Pacotes ajudam a:

- organizar projetos maiores;
- separar funcionalidades;
- facilitar manutenção;
- melhorar reutilização do código;
- tornar a navegação do projeto mais simples.

Além disso, frameworks e bibliotecas Python utilizam bastante essa estrutura.

#### Criando um pacote

Foi criado um diretório chamado `ecommerce`.

```text
ecommerce/
```

Inicialmente, ele é apenas uma pasta comum.

#### O arquivo `__init__.py`

Para que o Python reconheça a pasta como um pacote, foi criado o arquivo:

```python
__init__.py
```

Esse arquivo torna o diretório um pacote Python.

A estrutura ficou assim:

```text
ecommerce/
│
├── __init__.py
```

#### Criando um módulo dentro do pacote

Dentro do pacote `ecommerce`, foi criado um módulo chamado `entrega.py`.

```text
ecommerce/
│
├── __init__.py
├── entrega.py
```

#### Criando uma função no módulo

Dentro do módulo `entrega.py`, foi criada uma função chamada `calculadora_entrega`.

```python
def calculadora_entrega():
    print("Calculando o valor de entrega")
```

#### Importando funções de um pacote

No arquivo principal (`app.py`), a função foi importada diretamente.

```python
from ecommerce.entrega import calculadora_entrega
```

Depois disso, a função pode ser utilizada normalmente.

```python
calculadora_entrega()
```

Saída:

```python
Calculando o valor de entrega
```

#### Como funciona esse import

Nesse caso:

- `ecommerce` → pacote;
- `entrega` → módulo;
- `calculadora_entrega` → função.

O Python acessa cada nível usando ponto (`.`).

#### Erro de importação

Durante a aula aconteceu o erro:

```python
ModuleNotFoundError
```

Isso aconteceu porque o pacote estava fora da raiz do projeto executado pelo Python. O interpretador entendia que a pasta da aula era a raiz do projeto e, por isso, não encontrava o pacote `ecommerce`.

#### Solução utilizada

A solução foi mover a pasta `ecommerce` para dentro da pasta da aula. Depois disso, a importação funcionou corretamente.

#### Outra forma de importação

Também foi apresentada outra maneira de importar módulos.

```python
from ecommerce import entrega
```

Nesse caso, o módulo inteiro é importado.

Para acessar a função, é necessário usar:

```python
entrega.calculadora_entrega()
```

#### Diferença entre as duas formas

Importando diretamente a função:

```python
from ecommerce.entrega import calculadora_entrega
```

A função pode ser usada diretamente.

```python
calculadora_entrega()
```

Importando o módulo:

```python
from ecommerce import entrega
```

É necessário acessar a função usando ponto.

```python
entrega.calculadora_entrega()
```

#### Estrutura final do projeto

A estrutura criada durante a aula ficou semelhante a:

```text
034/
│
├── app.py
│
└── ecommerce/
    ├── __init__.py
    └── entrega.py
```

#### Aplicação prática

Pacotes são utilizados constantemente em projetos reais e frameworks.

Eles ajudam a:

- separar responsabilidades
- organizar funcionalidades
- reutilizar código
- estruturar aplicações maiores
- facilitar manutenção e crescimento do projeto

#### Checklist

Ao final desta aula, você aprendeu:

- o que são pacotes?;
- diferença entre módulos e pacotes;
- criação de diretórios como pacotes Python;
- uso do arquivo `__init__.py`;
- criação de módulos dentro de pacotes;
- importação de funções e módulos;
- uso do operador `.` para acessar módulos e funções;
- entendimento básico sobre estrutura de projetos Python.