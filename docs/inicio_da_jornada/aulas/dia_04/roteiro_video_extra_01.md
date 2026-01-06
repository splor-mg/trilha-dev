## Aula Extra – Voltando no Tempo com o Git
### Objetivo da aula:
Ensinar como navegar entre diferentes estados do projeto usando Git, mostrando na prática como visualizar versões antigas, voltar para pontos anteriores e comparar mudanças.

### 1. Abertura (1 min)
Cumprimentar e introduzir o tema com metáfora:

"Hoje vamos aprender como o Git nos dá uma máquina do tempo para nossos projetos."

- Explicar rapidamente por que isso é útil:
- Recuperar arquivos apagados acidentalmente
- Analisar código antigo
- Testar versões anteriores sem perder o que já foi feito

### 2. Como o Git registra o tempo (2 min)
- Explicar que cada commit é como uma "foto" do projeto naquele momento.
- Mostrar visualmente (no quadro ou em slides) a linha do tempo:
> Commit A → Commit B → Commit C → Commit D
- Explicar o conceito de hash e por que ele identifica unicamente cada momento.

### 3. Principais comandos para viajar no tempo (5 min)
- Demonstração no Codespaces: `git log`
- Mostra a lista de commits: `git show <hash>`
  - Usar opções como `--oneline` para visualização mais limpa.
- Visualiza as alterações de um commit específico. `git checkout <hash>`
- Muda o estado do projeto para um momento específico.
- Explicar que isso coloca o repositório em “detached HEAD”.
    - No Git, o HEAD é como um ponteiro que indica onde você está no histórico.- Normalmente, o HEAD aponta para um branch, e esse branch aponta para um commit.
    - Quando você navega para um commit específico (e não para um branch), o HEAD fica "desanexado" — isso é o detached HEAD.
    - Se você fizer commits nessa situação, eles não estarão vinculados a nenhum branch. Se você trocar de branch, pode perder o acesso fácil a esses commits, a menos que crie um branch novo para eles.
    - É como “entrar numa máquina do tempo” para ver um momento específico, mas que, se fizer mudanças lá, é preciso criar um branch antes para não perder o trabalho.

### Exemplo de quando acontece:
`git switch -`

### Volta para o branch anterior.

`git revert` vs `git reset`

#### Diferença entre git revert e git reset
Comando| O que faz | Afeta histórico público?|	Preserva histórico anterior?|
-------|-----------| ------------------------|------------------------------|
git revert | Cria um novo commit que desfaz as alterações de um commit anterior.| Não — seguro para repositórios compartilhados.| Sim, o commit original continua existindo no histórico.|
git reset|	Move o ponteiro do branch para um commit anterior, podendo descartar commits feitos depois dele.| Sim — altera histórico, perigoso em repositórios compartilhados.| Não, commits removidos podem ficar inacessíveis.

- `git revert`: “Desfaz o efeito de um commit criando um novo commit que reverte as mudanças. Seguro para trabalhar em equipe.”
- `git reset`: “Volta no tempo e apaga a parte da história como se nunca tivesse acontecido. Perigoso se outros já baixaram esses commits.”

### 4. Exemplo prático guiado (5 min)
- Criar um arquivo historia.txt e fazer 3 commits modificando o conteúdo.
- Mostrar o git log e navegar para um commit antigo.
- Alterar o arquivo nesse estado antigo, depois voltar para o presente.
- Mostrar como restaurar uma versão anterior de um único arquivo usando `git restore --source <hash> arquivo.txt.`

### 5. Boas práticas e dicas (2 min)
- Sempre verificar o git status antes de mudar de estado.
- Histórico compartilhado → use revert.
- Histórico local ainda não enviado → pode usar reset.
- Usar nomes claros nas mensagens de commit para facilitar achar o ponto certo.

### 6. Fechamento (1 min)
Reforçar que o Git não é só para guardar o que está pronto, mas também para explorar e recuperar trabalhos passados.

Convite para praticar: criar um mini-projeto e fazer 5 commits, depois visitar cada momento usando os comandos aprendidos.