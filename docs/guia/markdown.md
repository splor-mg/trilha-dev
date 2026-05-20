---
title: Markdown e Comandos Mkdocs
---

# :simple-markdown: Markdown e Comandos Mkdocs

[← Voltar ao guia](../)

---

## **[Markdown](https://www.markdownguide.org/)**


## **Títulos**

=== "Resultado"
    # Título 1
    ## Título 2
    ### Título 3

=== "Código"
    ```md
    # Título 1
    ```
    ```md
    ## Título 2
    ```
    ```md
    ### Título 3
    ```

---

## **Formatação de texto**

=== "Resultado"
    **Negrito**

    *Itálico*

    ~~Tachado~~

    `código inline`

=== "Código"
    Negrito:
    ```md
    **texto**
    ```
    Itálico:
    ```md
    *texto*
    ```
    Tachado:
    ```md
    ~~texto~~
    ```
    Código inline:
    ```md
    `texto`
    ```

---

## **Listas**

=== "Resultado"
    - Item A
    - Item B
        - Subitem

    1. Primeiro
    2. Segundo

=== "Código"
    Lista com marcadores:
    ```md
    - Item A
    - Item B
        - Subitem
    ```
    Lista numerada:
    ```md
    1. Primeiro
    2. Segundo
    ```

---

## **Links**

=== "Resultado"
    [Trilha Dev](https://trilhadev.planejamento.mg.gov.br/main/)

=== "Código"
    ```md
    [Texto do link](https://url.com)
    ```

---

## **Imagens**

=== "Resultado"

    ![Texto da imagem](../../assets/logo.png)


=== "Código"
    Imagem local (recomendado):
    ```md
    ![Descrição](../../assets/imagens/logo.png)
    ```
    Imagem por URL externa:
    ```md
    ![Descrição](https://exemplo.com/imagem.png)
    ```

    !!! info "Imagem local"
        Salve a imagem dentro do projeto em `docs/assets/imagens/` e referencie com caminho relativo. Funciona offline e não depende de links externos.

    !!! warning "Imagem externa"
        Links de URL podem parar de funcionar se o endereço mudar ou a rede restringir acesso externo.

---

## **Blocos de código**

=== "Resultado"
    ```python
    nome = input("Qual seu nome? ")
    print(f"Olá, {nome}!")
    ```

=== "Código"
    ````md
    ```python
    nome = input("Qual seu nome? ")
    print(f"Olá, {nome}!")
    ```
    ````

---

## **Tabelas**

=== "Resultado"
    | Comando | O que faz |
    |---------|-----------|
    | `git add` | Adiciona ao stage |
    | `git commit` | Registra alterações |

=== "Código"
    ```md
    | Coluna 1 | Coluna 2 |
    |----------|----------|
    | valor    | valor    |
    ```

---

## **Admonitions**

=== "Resultado"
    !!! tip "Dica"
        Texto da dica.

    !!! warning "Atenção"
        Texto de alerta.

    !!! info "Informação"
        Texto informativo.

=== "Código"
    ```md
    !!! tip "Dica"
        Texto da dica.
    ```
    ```md
    !!! warning "Atenção"
        Texto de alerta.
    ```
    ```md
    !!! info "Informação"
        Texto informativo.
    ```

---

## **Abas**

=== "Resultado"
    === "Python"
        ```python
        print("Olá!")
        ```
    === "Terminal"
        ```bash
        echo "Olá!"
        ```

=== "Código"
    ```md
    === "Python"
        ```python
        print("Olá!")
        ```
    === "Terminal"
        ```bash
        echo "Olá!"
        ```
    ```

## **[Comandos MkDocs](https://www.mkdocs.org/)**

Inicia o servidor local com preview em tempo real:
```bash
mkdocs serve
```

!!! info "Servidor local"
    Após rodar o comando, acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador.

Gera o site estático na pasta `site/`:
```bash
mkdocs build
```

## **Estrutura do projeto**

Arquivo de configuração do site:
```bash
mkdocs.yml
```

Pasta onde ficam os arquivos `.md`:
```bash
docs/
```

Pasta gerada após o build (não commitar):
```bash
site/
```

!!! tip "Dica"
    Adicione `site/` ao `.gitignore` para não versionar a pasta de build.
