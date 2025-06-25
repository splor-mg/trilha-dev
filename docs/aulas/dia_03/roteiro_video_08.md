# DIA 3: Escrevendo e publicando
🎥 Vídeo 8 – "Escrevendo em Markdown"Roteiro para vídeo 9: "Escrevendo em Markdown"

1. Introdução rápida ao Markdown

"Agora que já temos o projeto MkDocs criado, chegou a hora de colocar conteúdo nele — e o formato que vamos usar para isso é o Markdown."

Markdown é uma linguagem de marcação simples e legível, criada para facilitar a escrita de textos estruturados como títulos, listas e links.

2. Principais comandos Markdown

Apresentação prática no arquivo index.md:
|__OBJETIVO__ | __MARKDOWN__|__Exemplo__|
| -------------------- | --------------------- |
| Título | # até ###### | # Título 1 |
| Texto em negrito | **texto** | **Importante** |
| Itálico |*texto*  | *ênfase* |
| Lista |- item  | - Primeiro item |
| Link | [texto](url) | [Meu GitHub](https://...) |
| Imagem | ![alt](url) | ![Minha foto](minha.jpg) |
| Código inline | `código` | Use o comando `git status`  |

3. Exercício prático: sua apresentação em Markdown

"Vamos pegar aquele texto de apresentação pessoal que você escreveu e transformá-lo em Markdown."

Exemplo antes (texto plano):

    Olá, meu nome é Raiane. Trabalho com processos administrativos há 8 anos e estou começando a aprender sobre tecnologia. Gosto de compartilhar o meu conhecimento e acredito que posso ajudar meus colegas com isso a melhorarem suas rotinas de trabalho com isso.

Exemplo depois (Markdown):

# Sobre mim

**Olá!** Meu nome é *Raiane*.

Trabalho com **processos administrativos** há mais de 8 anos e estou começando a aprender sobre **tecnologia**.

Gosto de **compartilhar o meu conhecimento** e acredito que posso ajudar meus colegas com isso a melhorarem suas rotinas de trabalho com isso.

[Veja meu perfil no GitHub](https://github.com/raianecardoso)

Sugestão: personalizar com mais seções (interesses, experiência, contato) e usar títulos e listas para clareza.

4. Comitar as alterações

"Agora que editamos o arquivo index.md, precisamos salvar essa mudança no histórico do projeto — o famoso comitar."

Passo a passo no terminal do Codespace:

git add .
git commit -m "Criação da página inicial com apresentação pessoal"
git push

add: adiciona os arquivos modificados

commit: registra uma nova versão com mensagem

push: envia para o GitHub

5. Resumo e chamada para o próximo vídeo

"Hoje você aprendeu como escrever textos com Markdown, editou a página inicial do seu site e salvou essa mudança no repositório com comandos Git. Isso é um grande passo!"

📌 Gancho:

"Mas espera aí... você talvez tenha notado que usamos comandos diferentes: pip, git, markdown. O que são todos esses comandos? No próximo vídeo, vamos entender como o terminal nos permite falar com diferentes ferramentas."