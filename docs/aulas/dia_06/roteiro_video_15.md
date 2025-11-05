# "Como revisar e aprovar um Pull Request no GitHub"

## 1. Introdução
Na última aula, você aprendeu a criar um Pull Request. Agora vamos olhar do outro lado: como revisar e aprovar o que outra pessoa propôs.

Revisar um PR é parte essencial da colaboração: garante qualidade, evita erros e mantém o projeto organizado.

## 2. Onde encontrar os Pull Requests
Vamos começar abrindo nosso repositório no GitHub.

Acesse a aba "Pull requests" no topo do repositório.

Lá ficam todos os PRs abertos, aprovados ou fechados.

Clique em um PR para ver os detalhes.

## 3. Estrutura de um Pull Request
Ao abrir um PR, você verá várias seções importantes para análise.

**Descrição**

- Cheque se a descrição explica claramente o que foi feito.
- Veja se ela referencia uma issue (ex: Closes #1).

**Arquivos modificados**

- Clique na aba "Files changed" para ver exatamente o que foi alterado.
- Leia com atenção: o que mudou? Faz sentido? Há erros de digitação? Está dentro do escopo da tarefa?

**Commits**

- Clique na aba "Commits" para ver o histórico da branch.


## 4. Identificando e entendendo conflitos
Às vezes, o GitHub avisa que há um conflito e o PR não pode ser unido automaticamente à main.

**Por que isso acontece?**

- Alguém fez alterações no mesmo trecho de um arquivo que você também editou na sua branch.
- O Git não sabe qual versão manter.

**Como resolver?**

- Você precisa identificar o arquivo do conflito. O Git vai marcar os arquivos afetados com trechos assim:

diff

<<<<<<< HEAD
Seu conteúdo
=======
Conteúdo da main
>>>>>>> main

- Edite o arquivo manualmente, decidindo o que manter. Se você estiver fazendo essas alterações localmente:

```
git add .
git commit -m "Resolvendo conflitos com a main"
git push origin post-aprendizados
```

- Agora o GitHub vai atualizar o PR automaticamente, sem conflitos.

## 5. Aprovar ou comentar
Depois de revisar:

- Se estiver tudo certo, clique em "Review changes" e selecione "Approve"

- Se tiver dúvidas ou sugestões, selecione "Comment" ou "Request changes"


## 6. Fazer o merge (mesclar o PR)
Se o PR foi aprovado e não há conflitos:

- Clique em "Merge pull request"
- Depois, clique em "Confirm merge"
- Opcional: apagar a branch com o botão "Delete branch" (o conteúdo já foi incorporado na main).

## 7. Conclusão
Agora você sabe como revisar, aprovar e integrar uma contribuição no seu projeto. Com essa prática, o código fica melhor, mais organizado e todo mundo aprende junto.
