---
comments: true
---
# Aula 037: Pypi e pip

!!! info "Antes de começar"
    **7 min de vídeo + 15 min de prática aproximadamente**

    **Pré-requisito:** [Aula 036](../aulas/036_pastas_arquivos.md)

!!! abstract "Ao final desta aula você vai conseguir:"
    - Explicar o que é o `PyPI` e como ele se diferencia da biblioteca padrão do Python;
    - Encontrar e avaliar um pacote para uma necessidade específica;
    - Instalar um pacote com o `pip` e usá-lo no seu código;
    - Reconhecer por que, nos projetos da equipe, preferimos o Poetry.

## 🎥 Vídeo 37

<iframe width="560" height="315" src="https://www.youtube.com/embed/EF9cppje-oo?si=DP_PJjR-AWfSF6Ld" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é o `PyPI`?**

O **PyPI** (Python Package Index), em [pypi.org](https://pypi.org), é um repositório de pacotes da linguagem Python. Nele, desenvolvedores do mundo inteiro compartilham bibliotecas e ferramentas que podem ser instaladas e utilizadas em projetos Python.

Até aqui, utilizamos módulos **nativos** do Python, disponíveis no Python Module Index — aqueles que já vêm embutidos na linguagem. O `PyPI` vai além: dá acesso a bibliotecas desenvolvidas pela comunidade, que não acompanham a instalação do Python e precisam ser baixadas separadamente.

| | Biblioteca padrão | Pacotes do PyPI |
|---|---|---|
| Origem | Vem com o Python | Comunidade |
| Precisa instalar? | Não | Sim |
| Exemplos | `os`, `datetime`, `math` | `openpyxl`, `pypdf`, `mkdocs` |

A ideia central é simples: você quase nunca precisa criar tudo do zero. Boa parte do que precisa fazer já foi desenvolvida por alguém e está disponível para uso.

#### Exemplos de uso

Um desenvolvedor pode transformar uma solução em pacote e publicá-la no `PyPI` para que outras pessoas a utilizem. Há pacotes para praticamente tudo:

- envio de SMS;
- manipulação de Excel;
- criação de sites;
- automações;
- integração com APIs;
- análise de dados;
- entre outros.

#### Pesquisando pacotes

O site do `PyPI` tem uma busca para encontrar bibliotecas. Você pode, por exemplo:

- pesquisar bibliotecas para envio de SMS;
- procurar ferramentas para criar sites estáticos;
- encontrar bibliotecas para trabalhar com Excel.

Na prática, porém, a descoberta raramente começa dentro do próprio PyPI: ela costuma partir de uma pesquisa no Google ou da documentação da comunidade com uma pergunta do tipo *"qual a melhor ferramenta em Python para criar um site estático?"*. A partir do nome encontrado, você abre a página dele no `PyPI` para avaliar.

#### MkDocs

Ao pesquisar ferramentas para criar sites estáticos com Python, chegamos ao **MkDocs**, justamente a ferramenta usada no projeto do Trilha Dev. Existem diversos pacotes relacionados ao MkDocs no `PyPI`, cada um com funcionalidades específicas — você não precisa conhecer todos, apenas encontrar o que atende à sua necessidade.

#### Cuidados ao usar bibliotecas da comunidade

Como os pacotes são desenvolvidos pela comunidade, antes de adotar um deles vale observar:

- manutenção do projeto;
- data da última atualização;
- problemas conhecidos;
- documentação;
- segurança;
- popularidade da biblioteca.

Muitos projetos também têm repositório no GitHub, onde dá para acompanhar o desenvolvimento e até contribuir, se for open source.

!!! warning "Código da comunidade vem com responsabilidade"
    Por ser mantido por terceiros, um pacote pode ter bugs, falhas de segurança ou ficar sem manutenção. Não saia instalando qualquer coisa: leia a página, veja quando foi atualizado pela última vez e prefira projetos ativos e bem documentados.

#### OpenPyXL

O pacote `openpyxl` é usado para trabalhar com arquivos Excel em Python — útil quando uma planilha fica grande demais para processar manualmente. Ele permite:

- ler planilhas;
- escrever dados;
- automatizar tarefas;
- processar arquivos grandes;
- manipular células e abas.

Na página do pacote no `PyPI` você encontra a documentação, normalmente com instalação, primeiros passos, exemplos de uso, requisitos e referência da API. Vale lê-la antes de usar o pacote nos seus projetos.

#### Instalando pacotes com `pip`

Um pacote que você **nunca usou** ainda não está disponível, então, é preciso instalá-lo primeiro. O `PyPI` recomenda o `pip` para isso. No terminal:

**Instalação do OpenPyXL**

```bash
pip install openpyxl
```

O download leva alguns segundos. Ao final, você verá uma confirmação parecida com esta:

```text
Successfully installed openpyxl-3.1.5
```

A partir daí o pacote já pode ser importado e usado no seu código:

```python
from openpyxl import load_workbook

planilha = load_workbook("dados.xlsx")
aba = planilha.active
print(aba["A1"].value)   # Mostra o valor da célula A1
```

#### Instalando pacotes com `Poetry`

O `pip` está presente em qualquer instalação do Python, mas ele não é o único — e nos projetos do Trilha Dev normalmente utilizamos o `Poetry` como gerenciador de dependências.

```bash
poetry add openpyxl
```

!!! note "Importante"
    Sempre utilize o gerenciador de pacotes adotado pelo projeto em que você está. Os mais comuns são o `pip` e o `Poetry`. Antes de instalar algo, observe como aquele projeto gerencia suas dependências e siga o mesmo padrão.

#### Teste seus conhecimentos

??? question "Você quer usar a biblioteca `requests` num projeto novo e o Python acusa que ela não existe. Por que e o que fazer?"
    A `requests` não faz parte da biblioteca padrão —, é um pacote da comunidade, então não vem instalada com o Python. É preciso instalá-la antes de importar, com `pip install requests` (ou `poetry add requests`, se o projeto usa `Poetry`).

??? question "Você achou dois pacotes que fazem o que precisa. Quais informações ajudam a escolher?"
    O que cada um faz exatamente, os requisitos, a data da última atualização (projetos ativos são mais seguros), a documentação, a popularidade e a existência de um repositório aberto para acompanhar o desenvolvimento.

#### Recapitulando

!!! success "O que você viu nesta aula:"
    - O `PyPI` é o repositório de pacotes da comunidade Python e permite reutilizar soluções já desenvolvidas;
    - Pacotes da comunidade precisam ser instalados - a biblioteca padrão não;
    - Antes de criar algo do zero, pesquise se já existe uma biblioteca, como ela funciona, se atende ao projeto, se está ativa e bem mantida;
    - `pip install` instala um pacote;
    - Nos projetos do Trilha Dev usamos o `poetry add`.

??? example "Pratique!"
    Encontre no [pypi.org](https://pypi.org) um pacote para uma tarefa que você tenha (ler PDF, gerar gráfico, enviar e-mail) e instale-o no seu ambiente de exercícios. Depois, importe-o e rode um exemplo mínimo da documentação.

[Repositório com os exercícios](https://github.com/splor-mg/exercicios-python){ .md-button .md-button--primary }

[Como fazer os exercícios](../primeiros_passos/setup_repo_exercicios.md){ .md-button .md-button--primary }
