---
comments: true
---
# Aula 033: Módulos

## 🎥 Vídeo 33

Nesta aula, vamos aprender sobre módulos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QrkFD1OSUTQ?si=1Uo6ZuDuefzkAiTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### O que são módulos?

Módulos em Python são arquivos `.py` que contêm código Python, como funções, classes e variáveis. Eles são utilizados para organizar melhor o código e separar funcionalidades em diferentes arquivos.

#### Por que utilizar módulos?

À medida que os projetos crescem, o código tende a ficar mais extenso e complexo.

Organizar o código em módulos ajuda a:

- facilitar manutenção;
- melhorar leitura;
- reutilizar funções;
- separar responsabilidades;
- tornar o projeto mais organizado.

A aula faz uma analogia com um supermercado:

- cada seção possui produtos organizados por categoria;
- os módulos funcionam como essas seções;
- cada arquivo agrupa funcionalidades relacionadas.

#### Criando funções

Foram criadas duas funções simples:

- converter libras para quilogramas;
- converter quilogramas para libras.

```python
def libras_para_kilogramas(libras):
    return libras * 0.45

def kilogramas_para_libras(kg):
    return kg * 2.22
```

#### Criando um módulo

Depois, foi criado um novo arquivo chamado:

```python
conversores.py
```

As funções foram movidas para esse arquivo. Assim, o arquivo `conversores.py` passou a funcionar como um módulo.

#### Importando um módulo inteiro

A primeira forma apresentada foi importar o módulo completo usando `import`.

```python
import conversores
```

Depois disso, as funções podem ser acessadas usando:

```python
conversores.nome_da_funcao()
```

Exemplo:

```python
print(conversores.kilogramas_para_libras(10))
```

Saída:

```python
22.2
```

#### Como funciona o acesso com ponto

Quando o módulo é importado, ele passa a ser tratado como um objeto dentro do arquivo atual.

Por isso, utiliza-se a sintaxe:

```python
modulo.funcao()
```

#### Importando apenas uma função

A segunda forma apresentada foi importar diretamente a função desejada.

```python
from conversores import libras_para_kilogramas
```

Assim, a função pode ser usada diretamente.

```python
print(libras_para_kilogramas(100))
```

Saída:

```python
45.0
```

#### Diferença entre as duas formas:

##### 1. Importando o módulo inteiro

```python
import conversores
```

Vantagem:

- útil quando várias funções do módulo serão utilizadas.

Uso:

```python
conversores.funcao()
```

##### 2. Importando apenas a função

```python
from conversores import libras_para_kilogramas
```

Vantagem:

- mais prático quando apenas uma função será utilizada.

Uso:

```python
libras_para_kilogramas()
```

#### Organização de código

A principal ideia dos módulos é dividir o código de maneira lógica.

Exemplo:

- um módulo para conversões;
- outro para autenticação;
- outro para banco de dados;
- outro para utilidades.

Isso torna o sistema mais organizado e reutilizável.

#### Aplicação prática

Módulos ajudam a:

- reutilizar código
- evitar arquivos gigantes
- melhorar manutenção
- facilitar leitura
- organizar projetos maiores

#### Checklist

Ao final desta aula, você aprendeu:

- o que são módulos?;
- como criar um módulo;
- como importar módulos;
- como importar funções específicas;
- como acessar funções de outros arquivos;
- importância da organização de código.

Os módulos são fundamentais para desenvolver projetos maiores e mais organizados em Python.