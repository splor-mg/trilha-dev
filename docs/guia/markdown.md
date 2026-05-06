---
Title: Markdown
---

# Markdown

[← Voltar ao guia](../)

---

## Títulos

=== "Resultado"

    # Título
    ## Subtítulo
    ### Subtítulo menor

=== "Código"

    ```md
    # Título
    ## Subtítulo
    ### Subtítulo menor
    ```

---

## Formatação de texto

=== "Resultado"

    **Negrito**

    *Itálico*

=== "Código"

    ```md
    **Negrito**
    *Itálico*
    ```

---

## Lista

=== "Resultado"

    - Item de lista

=== "Código"

    ```md
    - Item de lista
    ```

---

## Link

=== "Resultado"

    [Trilha Dev](https://trilhadev.planejamento.mg.gov.br/main/)

=== "Código"

    ```md
    [Texto do link](https://trilhadev.planejamento.mg.gov.br/main/)
    ```

---

## Imagem

=== "Resultado"

    ![Texto da imagem](../../assets/logo.png)

=== "Código"

    ```md
    ![Texto da imagem](URL)
    ```

    !!! info "Como usar imagens no projeto"

        **Imagem local (recomendado):**

        - Adicione a imagem dentro da pasta do projeto, por exemplo:

              docs/assets/imagens/exemplo.png

        - Referencie no Markdown usando caminho relativo:

        ```md
        ![Descrição](../../assets/imagens/exemplo.png)
        ```

        - Vantagem: funciona offline e não depende de links externos.

        **Imagem por URL (externa):**

        - Use um link direto para a imagem:

        ```md
        ![Descrição](https://exemplo.com/imagem.png)
        ```

    !!! warning "Atenção"
        URL externa pode não funcionar em redes com restrição ou se o link sair do ar.

---

## Código inline

=== "Resultado"

    Use `print()` no Python

=== "Código"

    ```md
    `print()`
    ```
