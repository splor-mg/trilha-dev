# Quiz - Dia 6: Branches e Pull Requests

Teste seus conhecimentos sobre branches, pull requests e colaboração segura!

<div class="grid" markdown>

=== ":tools: Como usar este quiz:"

    1. **Leia atentamente** cada pergunta
    2. **Selecione** a resposta que você considera correta
    3. **Clique em "Verificar"** para ver se acertou
    4. **Leia as explicações** que aparecem para cada resposta
    5. **Use o botão "Atualizar"** para tentar novamente se desejar
    
=== ":bulb: Dicas para melhor aproveitamento:"

    * Tente responder sem consultar o material primeiro
    * Leia sempre as explicações das respostas
    * Use o quiz como forma de revisar o conteúdo
    * Não se preocupe se errar - é parte do aprendizado!

</div>

## Questão 1: Branch (Ramo)

<?quiz?>
question: O que é uma branch no Git?
answer: Um arquivo de configuração
answer-correct: Uma cópia da linha principal onde você pode testar novas ideias
answer: Um tipo de commit
answer: Uma mensagem de erro
content:
<p><strong>Explicação:</strong> Uma branch é como uma cópia da sua linha principal de desenvolvimento, onde você pode testar e desenvolver novas ideias sem interferir no que já está funcionando.</p>
<?/quiz?>

## Questão 2: Vantagens das Branches

<?quiz?>
question: Qual é uma vantagem de usar branches?
answer: Torna o código mais lento
answer: Cria conflitos automaticamente
answer: Deleta arquivos antigos
answer-correct: Permite testar sem afetar o site em produção
content:
<p><strong>Explicação:</strong> As branches permitem testar sem afetar o site em produção e facilitam o trabalho em equipe, pois cada pessoa pode trabalhar em sua própria branch.</p>
<?/quiz?>

## Questão 3: Pull Request

<?quiz?>
question: Para que serve um Pull Request (PR)?
answer: Criar uma nova branch
answer: Deletar arquivos
answer: Fazer backup do projeto
answer-correct: Revisar e integrar mudanças de forma organizada e segura
content:
<p><strong>Explicação:</strong> O Pull Request serve para revisar o que foi feito, comentar, pedir sugestões e, por fim, juntar (fazer o merge) com a branch principal de forma organizada e segura.</p>
<?/quiz?>

## Questão 4: Criando uma Branch

<?quiz?>
question: Qual comando cria e muda para uma nova branch?
answer: git branch nome-da-branch
answer: git create nome-da-branch
answer: git new nome-da-branch
answer-correct: git checkout -b nome-da-branch
content:
<p><strong>Explicação:</strong> O comando git checkout -b cria e muda para uma nova branch. Por exemplo: git checkout -b post-aprendizados cria e entra na branch "post-aprendizados".</p>
<?/quiz?>

## Questão 5: Nomes de Branches

<?quiz?>
question: Como devemos nomear as branches?
answer: Nomes muito longos e detalhados
answer-correct: Nomes curtos e descritivos
answer: Nomes com números aleatórios
answer: Nomes em maiúsculas sempre
content:
<p><strong>Explicação:</strong> É uma boa prática escolher nomes curtos e descritivos para as branches, como "post-aprendizados" ou "corrigir-links".</p>
<?/quiz?>

## Questão 6: Conflitos no Git

<?quiz?>
question: Por que acontecem conflitos no Git?
answer: Porque o Git é confuso
answer: Porque há muitos arquivos
answer: Porque a internet está lenta
answer-correct: Alguém editou o mesmo trecho de arquivo que você também editou
content:
<p><strong>Explicação:</strong> Conflitos acontecem quando alguém fez alterações no mesmo trecho de um arquivo que você também editou na sua branch. O Git não sabe qual versão manter.</p>
<?/quiz?>

## Questão 7: Revisão de PR

<?quiz?>
question: O que devemos verificar ao revisar um Pull Request?
answer: Apenas se o código funciona
answer-correct: Se a descrição explica claramente o que foi feito
answer: Apenas se não há erros de digitação
answer: Apenas se está bonito
content:
<p><strong>Explicação:</strong> Ao revisar um PR, devemos verificar se a descrição explica claramente o que foi feito, se referencia uma issue, se os arquivos modificados fazem sentido e se estão dentro do escopo da tarefa.</p>
<?/quiz?>

## Questão 8: Merge de PR

<?quiz?>
question: Quando podemos fazer o merge de um Pull Request?
answer: Sempre que quisermos
answer: Apenas quando há conflitos
answer: Nunca, pois é perigoso
answer-correct: Quando foi aprovado e não há conflitos
content:
<p><strong>Explicação:</strong> Podemos fazer o merge quando o PR foi aprovado e não há conflitos. Isso garante que a integração seja segura e organizada.</p>
<?/quiz?>

## Questão 9: Boa Prática com PR

<?quiz?>
question: Qual é uma boa prática ao criar um Pull Request?
answer: Criar PRs sem descrição
answer: Não revisar o código
answer: Fazer merge imediatamente
answer-correct: Sempre associar o PR com a issue que deu origem à tarefa
content:
<p><strong>Explicação:</strong> É uma boa prática sempre associar o PR com a issue que deu origem à tarefa, incluindo referências como "Closes #1" na descrição.</p>
<?/quiz?>

---

[Voltar ao Dia 6](dia_06.md){ .md-button .md-button--primary }
[Voltar às aulas](../index.md){ .md-button .md-button--secondary } 