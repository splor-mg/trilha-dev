---
comments: true
---
# Aula 036: Trabalhando com pastas e arquivos

## 🎥 Vídeo 36

Nesta aula, vamos aprender a usar o módulo `pathlib`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YRGN2-Avu8A?si=6BQbZpyK7VHF3aUG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **Módulo `pathlib`**

Nesta aula, continuamos estudando módulos nativos do Python e conhecemos o módulo `pathlib`, utilizado para manipular caminhos e arquivos de forma orientada a objetos.

O `pathlib` é muito útil para automações, leitura de arquivos, organização de diretórios e processamento de dados.

#### **Importando o `pathlib`**

Para utilizar o `pathlib`, precisamos importar a classe `Path`:

```python
from pathlib import Path
```

A classe `Path` representa caminhos de arquivos e diretórios.

#### **Criando um objeto `Path`**

Para trabalhar com um caminho, criamos uma instância da classe `Path`:

```python
from pathlib import Path

path = Path("aulas/034/ecommerce")
```

Nesse exemplo, `path` representa o diretório `ecommerce`.

#### **Verificando se um diretório existe**

O método `.exists()` verifica se o caminho informado existe:

```python
from pathlib import Path

path = Path("aulas/034/ecommerce")

print(path.exists())
```

Resultado:

```python
True
```

Se o diretório não existir:

```python
from pathlib import Path

path = Path("aulas/036/emails")

print(path.exists())
```

Resultado:

```python
False
```

#### **Criando diretórios**

Podemos criar um diretório utilizando o método `.mkdir()`:

```python
from pathlib import Path

path = Path("aulas/036/emails")

path.mkdir()
```

Após executar o código, a pasta `emails` será criada.

#### **Removendo diretórios**

O método `.rmdir()` remove um diretório:

```python
from pathlib import Path

path = Path("aulas/036/emails")

path.rmdir()
```

Após executar o código, o diretório será removido.

#### **Listando arquivos com `glob`**

O método `.glob()` permite localizar arquivos e diretórios utilizando padrões.

#### **Todos os arquivos**

```python
from pathlib import Path

path = Path(".")

for arquivo in path.glob("*.*"):
    print(arquivo)
```

#### **Filtrando arquivos por extensão:**

#### **Arquivos Python**

```python
from pathlib import Path

path = Path("aulas/034/ecommerce")

for arquivo in path.glob("*.py"):
    print(arquivo)
```

Resultado esperado

```python
dander.py
entrega.py
```

#### **Padrões comuns do `glob`**

| Padrão | Descrição |
|---|---|
| `*` | Todos os arquivos e diretórios |
| `*.*` | Todos os arquivos |
| `*.py` | Arquivos Python |
| `*.csv` | Arquivos CSV |
| `*.xlsx` | Arquivos Excel |

#### **Objetos iteráveis**

O método `.glob()` retorna um objeto iterável.
Por isso, normalmente utilizamos um `for` para percorrer os arquivos encontrados:

```python
for arquivo in path.glob("*.py"):
    print(arquivo)
```

#### **Aplicações práticas**

O `pathlib` pode ser utilizado para:

- Processar planilhas automaticamente
- Ler arquivos CSV
- Organizar diretórios
- Criar automações
- Trabalhar com arquivos de configuração
- Criar scripts utilitários

#### **Desafio da aula**

No repositório de exercícios existe uma pasta chamada `scripts`.

O desafio proposto foi:

1. Localizar o script `cria_pasta`;
2. Ler o código linha por linha;
3. Identificar quais módulos nativos estão sendo utilizados;
4. Entender por que foi criada uma automação para gerar pastas automaticamente.

Os módulos utilizados nesse script são:

- `pathlib`
- `argparse`

#### **Checklist**

Nesta aula aprendemos:

- O que é o módulo `pathlib`?
- Como importar a classe `Path`;
- Como verificar se arquivos e diretórios existem;
- Como criar e remover diretórios;
- Como localizar arquivos utilizando `glob`;
- Como utilizar o `pathlib` em automações.

O `pathlib` é uma das bibliotecas mais úteis do Python para manipulação de arquivos e diretórios.