## 1. Abertura: a lógica da colaboração no mundo do código

Até aqui, você criou um site com MkDocs, aprendeu sobre versionamento com Git, editou conteúdos com Markdown... Agora chegou o momento de entender como tudo isso ganha vida no mundo real: com colaboração e publicação.

No mundo da programação, quase nada é feito sozinho.

Os projetos crescem com contribuições de várias pessoas — cada uma melhora uma parte, corrige um erro, documenta algo.

Isso é o que chamamos de código aberto (open source): qualquer pessoa pode contribuir com um projeto público.

## 2. Fazendo um paralelo com a colaboração tradicional

Pensa quando você apresenta um trabalho com colegas: cada um escreve uma parte, revisa, alguém cuida da formatação... no final, entregam algo em grupo.

A lógica é parecida com projetos no GitHub.

- Cada pessoa trabalha em uma branch (linha de trabalho).

- Depois junta tudo com um pull request.

- Outras pessoas podem revisar, comentar, sugerir melhorias.

## 3. Como isso funciona com GitHub

GitHub é uma plataforma que permite armazenar e colaborar em projetos com Git.

Em projetos públicos, qualquer pessoa pode:

- Ver o código e documentação

- Sugerir melhorias

- Fazer perguntas (Issues)

- Propor mudanças (Pull Requests)

Você também pode usar isso no seu time de trabalho para criar processos mais claros, colaborativos e auditáveis.

## 4. Hora de publicar: usando GitHub Pages

Agora vamos dar o próximo passo: publicar seu site na internet usando o GitHub Pages.

Essa é uma forma gratuita e fácil de hospedar seu portfólio.

## 5. Preparando o projeto para publicação
No terminal, dentro do seu projeto:

```
mkdocs build
```
Esse comando gera a pasta site/ com os arquivos finais do seu site.

## 6. Atualizando o arquivo de configuração do projeto

No arquivo mkdocs.yml, adicione:

```
site_url: https://seuusuario.github.io/seurepositorio/
```
Substitua seu usuario e seu repositorio pelos nomes corretos do seu GitHub.

## 7. Criando o arquivo de deploy

Se ainda não estiver no projeto, crie o arquivo `.github/workflows/gh-pages.yml` com o seguinte conteúdo:

```
name: Deploy MkDocs site to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - run: pip install mkdocs mkdocs-material
      - run: mkdocs gh-deploy --force
```

## 8. Subindo para o GitHub
No terminal:

```
git add .
git commit -m "Preparação para publicação do site"
git push origin main
```

Espere alguns minutos, e seu site estará disponível no endereço configurado.

## 9. Conclusão e convite

Hoje você aprendeu como os projetos abertos são construídos com colaboração, como o GitHub ajuda nesse processo, e — o mais importante — colocou seu portfólio no ar! Parabéns! 

Na próxima aula, nós vamos ver como melhorar o nosso projeto, contribuir, fazer perguntas e realmente se integrar a uma rede de conhecimento. 

📌 Dica final:

Compartilhe o link do seu site com colegas e amigos. E não se esqueça: você pode continuar melhorando esse site com novos conteúdos, posts e ajustes.

