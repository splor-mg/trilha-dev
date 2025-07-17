# Aula extra `.gitignore`

## 1. Introdução 

O .gitignore é um filtro de qualidade para o que realmente deve estar no seu repositório.

Você quer versionar:

- Código
- Documentação
- Configurações do projeto
- Arquivos necessários para que outra pessoa possa clonar e rodar

Você não quer versionar:

- Arquivos temporários
- Informações sensíveis, como senhas.
- Configurações locais
- Logs, caches e ambientes virtuais

## 2. O que acontece ao adicionar o .gitignore depois de ter arquivos commitados:

- O Git não vai remover automaticamente os arquivos já versionados, mesmo que eles passem a estar listados no .gitignore.

- O .gitignore passa a funcionar apenas para novos arquivos ou alterações futuras de arquivos que ainda não estão sendo rastreados pelo Git.

## 3. O que você pode fazer:
Se você quer parar de versionar arquivos que já foram incluídos, siga este processo:

- Crie ou edite seu .gitignore com as regras apropriadas.
- Para parar de rastrear arquivos que já foram comitados, use: `git rm -r --cached .`
- Depois disso, adicione e commite a mudança:
```
git add .gitignore
git commit -m "Adiciona .gitignore e remove arquivos desnecessários do versionamento
```
## 4. Gerando o arquivo .gitignore

O gitignore.io é uma ferramenta excelente para gerar arquivos `.gitignore` personalizados.

- Acesse https://www.toptal.com/developers/gitignore
- Pesquise por Python, Vscode
- Copie o conteúdo em aquivo `.gitignore` na raiz do projeto