---
comments: true
---
# DIA 6: Trabalhando em equipe: colaborando com segurança

## 🎥 Vídeo 14 – Branch e Pull Request

Neste vídeo, vamos ensinar sobre como a colaboração acontece no Github, com branches e PRs.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHB0n4xezs?si=LnffBqb6Y4krZwag" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 🎥 Vídeo 15 – Revisão de um Pull Request

Nosso objetivo neste vídeo é mostrar o básico de como avaliar um PR.

<iframe width="560" height="315" src="https://www.youtube.com/embed/E5Qh93eZiCA?si=pzURDuF1cYwQiGb3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

??? tip "Batalha de Commits: Resolvendo Conflitos no Git"

    Aqui quem manda é ??? — vencedor oficial da batalha do Git! :trophy:

??? tip "Conflitos na avaliação de um PR"

     **Conflitos**

    Um conflito em um pull request ocorre quando o sistema de controle de versão, no caso o Git, não consegue mesclar automaticamente as alterações de duas branches diferentes devido a alterações conflitantes nos mesmos arquivos ou linhas de código. Isso geralmente acontece quando duas ou mais pessoas trabalham no mesmo trecho de código simultaneamente. 
    
    **Como resolver conflitos?**

    - **Abrir a pull request e identificar os arquivos com conflitos:** 
    O git indica quais arquivos precisam ser resolvidos.

    - **Abrir o arquivo com conflito e examinar as marcações:** 
    Você verá as áreas com conflitos, indicando as versões de código de cada branch. Os marcadores especiais  são: <<<<<<<, =======, e >>>>>>>.

    - **Escolher qual versão manter ou mesclar as alterações:** 
    Você pode escolher manter a versão de uma das branches, mesclar as alterações manualmente, ou remover partes de ambos os códigos para criar uma nova versão. 

    - **Remover os marcadores de conflito:** 
    Depois de resolver o conflito, você deve remover os marcadores do código.

    - **Fazer commit das alterações e atualizar a pull request:** 
    Após resolver todos os conflitos, você pode fazer commit das alterações e concluir a mesclagem.
__________

### Teste seus conhecimentos!

[Quiz dia 06](quiz_dia_06.md){ .md-button .md-button--primary } 

### Checklist Dia 6:
- [ ] Assistir aos 2 vídeos
- [ ] Entender o conceito de branches
- [ ] Aprender sobre Pull Requests
- [ ] Praticar criação de branches
- [ ] Criar um Pull Request
- [ ] Aprender a revisar PRs
- [ ] Entender resolução de conflitos
- [ ] Completar o quiz acima