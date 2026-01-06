## 🎥 Vídeo 11 – Comandos Git

### 1. Abertura: Por que usar o Git?

"Você já imaginou poder voltar no tempo e recuperar uma versão anterior de um documento? Ou acompanhar exatamente o que mudou e quem fez cada alteração em um projeto? Isso é o que o Git permite fazer com seus arquivos."

O Git é um sistema de controle de versão. Ele acompanha todas as mudanças feitas em arquivos ao longo do tempo. É como um histórico completo do seu projeto.

### 2. O que é o Git e como começar a usá-lo

"O Git é um programa, e para usá-lo no seu projeto, ele precisa estar instalado na sua máquina — e ativado dentro do repositório."

Verifique se o Git está instalado:

`git --version`

Ative o Git em um projeto com:

`git init`

Isso cria uma pasta `.git` oculta no seu projeto — é ali que o Git guarda todo o histórico.

### 3. Entendendo os status dos arquivos

Depois que o Git está ativo, ele começa a monitorar as alterações nos arquivos. Para ver o que está acontecendo, usamos:

`git status`

Você pode ver diferentes estados:

|Status |Significado|
| -------------------- | --------------------- |
| Untracked| Arquivo novo que o Git ainda não monitora. Use git add para começar a rastrear.|
| Modified| Arquivo já conhecido pelo Git, mas que foi alterado. Ainda não pronto para salvar.|
| Staged / Ready to commit | Arquivo marcado com git add para ser incluído no próximo "snapshot". |

Visualizar isso com `git status` é essencial antes de qualquer commit.

### 4. O que é um commit?

"Um commit é como um ponto de salvamento. Nele você registra o que mudou no projeto com uma mensagem clara."

Para criar um commit:

`git add nome-do-arquivo`  # ou `git add .` para tudo
`git commit -m "mensagem explicando a mudança"`

#### Boas práticas:

Faça commits pequenos e frequentes.

- Escreva mensagens claras e objetivas.

- ✅ "Adiciona nova seção sobre comandos Git"

- ❌ "Update" ou "Coisas novas"

### 5. Enviando e recebendo alterações do repositório remoto

"Até agora, as mudanças estão só no seu ambiente local. Para colaborar com outras pessoas (ou salvar no GitHub), precisamos enviar e buscar alterações com `git push` e `git pull.`"

Para enviar suas mudanças:

`git push origin main`

Para trazer atualizações do repositório remoto:

`git pull origin main`

Usar o nome do destino (origin) e da branch (main) evita erros e torna seu comando mais explícito.

### 6. Recapitulando com um fluxo completo

- Você faz alterações no projeto.

- Verifica o status:

`git status`

- Adiciona os arquivos:

`git add .`

- Cria um commit:

`git commit -m "Mensagem clara"`

- Envia para o GitHub:

`git push origin main`

### 7. Gancho para o próximo vídeo

"Agora que você sabe registrar e versionar mudanças com o Git, que tal aprender como trabalhar em equipe sem pisar no trabalho de ninguém? No próximo vídeo, vamos falar sobre branches, pull requests e colaboração no GitHub!" 
