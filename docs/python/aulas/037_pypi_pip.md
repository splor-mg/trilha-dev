---
comments: true
---
# Aula 037: Pypi e pip

## 🎥 Vídeo 37

Nesta aula, vamos aprender a encontrar e instalar bibliotecas.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EF9cppje-oo?si=DP_PJjR-AWfSF6Ld" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é o `PyPI`?**

O **PyPI (Python Package Index)** é um repositório de pacotes da linguagem Python. Nele, desenvolvedores do mundo inteiro compartilham bibliotecas e ferramentas que podem ser instaladas e utilizadas em projetos Python.

Até agora, utilizamos módulos nativos do Python, disponíveis no Python Module Index. Já o `PyPI` permite acessar bibliotecas desenvolvidas pela comunidade.

#### **Exemplos de uso**

Um desenvolvedor pode criar um pacote para:

- envio de SMS;
- manipulação de Excel;
- criação de sites;
- automações;
- integração com APIs;
- análise de dados;
- entre outros.

Esses pacotes podem ser publicados no PyPI para que outras pessoas utilizem.

#### **Pesquisando pacotes**

O site do `PyPI` possui uma busca para encontrar bibliotecas.

Exemplo:

- pesquisar bibliotecas para envio de SMS;
- procurar ferramentas para criar sites estáticos;
- encontrar bibliotecas para trabalhar com Excel.

Muitas vezes, a escolha de uma ferramenta começa com pesquisas no Google ou documentação da comunidade.

#### **MkDocs**

Ao pesquisar ferramentas para criar sites estáticos com Python, podemos encontrar o MkDocs, utilizado no projeto do Trilha Dev. Existem diversos pacotes relacionados ao MkDocs no `PyPI`, cada um com funcionalidades específicas.

#### **OpenPyXL**

O pacote `openpyxl` é utilizado para trabalhar com arquivos Excel em Python.

Ele permite:

- ler planilhas;
- escrever dados;
- automatizar tarefas;
- processar arquivos grandes;
- manipular células e abas.

Documentação:

- instalação;
- primeiros passos;
- exemplos de uso;
- requisitos;
- referências da API.

#### **Cuidados ao usar bibliotecas da comunidade**

Como os pacotes são desenvolvidos pela comunidade, é importante observar:

- manutenção do projeto;
- data da última atualização;
- problemas conhecidos;
- documentação;
- segurança;
- popularidade da biblioteca.

Muitos projetos também possuem repositórios no GitHub, permitindo acompanhar o desenvolvimento e até contribuir.

#### **Instalando pacotes com `pip`**

O PyPI recomenda o uso do `pip` para instalar bibliotecas.

#### **Instalação do OpenPyXL**

```bash
pip install openpyxl
```

Após a instalação, já é possível importar o pacote no Python.

Exemplo:

```python
import openpyxl
```

#### **Instalando pacotes com `Poetry`**

Nos projetos do Trilha Dev, normalmente utilizamos o `Poetry` como gerenciador de dependências.

Exemplo:

```bash
poetry add openpyxl
```

#### **Importante**

Sempre utilize o gerenciador de pacotes adotado pelo projeto.

Os mais comuns são:

- pip
- Poetry

#### **Checklist**

O `PyPI` permite reutilizar soluções já desenvolvidas pela comunidade Python.

Antes de criar algo do zero, vale pesquisar:

- Se já existe uma biblioteca para resolver o problema;
- Como ela funciona;
- Se atende às necessidades do projeto;
- Se o projeto está ativo e bem mantido.

Isso acelera o desenvolvimento e aproveita o conhecimento compartilhado pela comunidade.