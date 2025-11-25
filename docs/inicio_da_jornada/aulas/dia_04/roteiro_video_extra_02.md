## Aula extra: Mergulhando no Git
### 1. Abertura (1 min)

“Hoje vamos falar sobre algo que está no DNA do Git: o versionamento. Antes do Git existir, já havia ferramentas que faziam isso — mas o Git trouxe uma revolução que mudou a forma como o mundo desenvolve software.”

### 2. O que é versionamento? (3 min)
- Conceito: registro histórico das alterações em arquivos ao longo do tempo.
    - Salvar versões diferentes de um documento no computador (v1, v2, final, final-final).
    - Controle de histórico em Google Docs.

- Benefícios:
    - Recuperar versões anteriores.
    - Saber quem alterou o quê e quando.
    - Trabalhar de forma colaborativa sem perder alterações.

### 3. Antes do Git (3 min)

- Ferramentas que vieram antes:
    - CVS (Concurrent Versions System) – 1986.
    - Subversion (SVN) – 2000.
    - Mercurial – 2005.

- Limitações comuns:

    - Centralização (dependência de um servidor único).
    - Desempenho lento em grandes projetos.
    - Difícil trabalhar offline.

### 4. A chegada do Git (5 min)

- Criado por Linus Torvalds em 2005 para desenvolver o kernel Linux.
- rápido, seguro, distribuído.
- Diferenças marcantes:
    - Distribuído: cada pessoa tem o repositório completo.
    - Velocidade: operações locais, sem depender de servidor.
    - Segurança: commits identificados por hashes SHA-1.
    - Ramos (branches): leves e fáceis de criar/mesclar.
    - Popularização via GitHub: colaboração e código aberto.

### 5. Demonstração 

Mostrar slide que explica funcionamento de apontamentos, juntamente com a explicação.

O Git funciona com um banco de dados de objetos (chamado object store), que fica dentro da pasta .git/objects. Esses objetos podem ser de quatro tipos principais:

- Blob (Binary Large Object) – é o conteúdo de um arquivo (não guarda nome, só o conteúdo).
- Tree – descreve um diretório: lista nomes de arquivos, seus modos (permissões) e aponta para blobs ou outras trees.
- Commit – guarda o “estado” do projeto naquele momento, apontando para uma tree (raiz do projeto), o commit pai, autor, data e mensagem.
- Tag – aponta para um commit e serve para marcar versões.

#### Como o Git evita duplicar arquivos
Quando você altera apenas um arquivo e cria um commit:

- O Git cria um novo blob para esse arquivo alterado.
- Os outros arquivos não são duplicados — o Git apenas reaproveita os blobs existentes dos commits anteriores.
- A nova tree (diretório raiz) aponta para esses blobs já existentes.

É como um conjunto de “caixinhas” (objetos) onde cada conteúdo é guardado apenas uma vez.

O identificador de cada objeto é um hash SHA-1 gerado a partir do seu conteúdo — se o conteúdo não muda, o hash também não muda, e o Git não cria um novo objeto.

**Analogia rápida:** Imagine que cada commit é um “mapa” que diz onde estão os arquivos. Se um arquivo não mudou, o mapa só aponta para a mesma “cópia” já existente no depósito, sem criar outra.

### Estrutura típica da pasta .git

1. `objects/`
- Onde o Git armazena todo o histórico — blobs, trees, commits e tags.
- É a parte mais importante do repositório, porque sem ela você perde todos os dados versionados.

2. `refs/`
- Guarda os ponteiros para commits.
- Dentro dela existem subpastas:
    - `heads/` → cada arquivo representa uma branch e aponta para o commit mais recente.
    - `tags/` → cada arquivo representa uma tag e aponta para um commit específico.
    - `remotes/` → referência para branches de repositórios remotos.

3. `HEAD`
- Arquivo de texto simples que indica qual branch você está usando no momento (ex.: `ref: refs/heads/main`).

4. `config`
- Arquivo com as configurações locais do repositório (nome, e-mail, URL do remoto, etc.).
- Complementa as configurações globais que ficam no seu usuário (`~/.gitconfig`).

5. `index`
- Também chamado de staging area ou cache.
- É onde o Git guarda a “fotografia” dos arquivos que estão prontos para o próximo commit.

6. `logs/`
- Registro de tudo que aconteceu com as referências (refs), usado para o comando git reflog.
- Serve para recuperar commits perdidos.

7. `hooks/`
- Scripts que o Git executa em determinados momentos (por exemplo, antes de um commit ou push).
- Usados para automação, testes, padronização de mensagens, etc.

8. `info/`
- Contém informações adicionais sobre o repositório, como o arquivo exclude (um .gitignore local só para esse repositório).

9. `description`
- Texto usado por interfaces de Git (como GitWeb) para mostrar uma descrição do repositório.
- No Git normal, quase nunca é usado.

#### Resumo:
- A pasta .git é como o “HD secreto” do seu repositório.
- Tudo que você vê na sua pasta de trabalho é apenas uma cópia de trabalho (working directory).
- O que vale mesmo para o Git está dentro de .git.