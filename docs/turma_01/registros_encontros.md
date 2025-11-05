---
comments: true
---

# **Registros dos Encontros da Primeira Turma**

## 1º Encontro

- Data: 14/08/2025
- Gravação: [Link do YouTube](https://www.youtube.com/watch?v=B6nQjFfbLxs)

### Dúvidas

- Preciso desenvolver um projeto pessoal ao longo do curso ou posso já desenvolver um projeto relacionado às atividades do trabalho?

### Sugestões

- Fou sugerido pelo Bruno Rosa (DCMEFO) a construção de um Banco de Projetos. Nesse banco, vamos inserir as ideias de pprojetos que podem ser desenvolvido no âmbito da SPLOr, usando as ferramentas que serão tratadas ao longo do curso.
- Gabriel Dornas sugeriu que esse Banco seja uma Discussão, ferramenta já disponível no github, dentro da organização da Splor. Veja aqui o [Banco de Projetos](https://github.com/splor-mg/trilha-dev/discussions/49) e compartilhe as suas ideias! :bulb:

### Avisos e alinhamentos

- Os alunos devem habilitar o duplo fator de autenticação da sua conta do Github para segurança dos dados da Splor.
- O curso contará com um certificado de participação de 30h, que será emitido para aqueles que apresentarem o projeto de um site estático, conforme orientaçõe do curso.

---

## 2º Encontro

- Data: 22/08/2025
- Gravação: [Link do YouTube](https://youtu.be/rQLcSIbf9Ts)

### Dúvidas
_a partir do minuto 00:03:00_

- A cada aula preciso criar um novo Codespace ou devo continuar usando o mesmo?
- Cada vez que abro o Codespace preciso fazer novamente a instalação de todos os requisitos do projeto?
- Se eu abrir um novo repositório, vou precisar instalar todas as ferramentas novamente?

_a partir do minuto 00:14:00_

- Se o Codespaces não salva as minhas alterações e pode ser excluído, onde as minhas alterações são salvas?
_a partir do minuto 00:35:00_
- Vale mais a pena fazer o setup da máquina local ou usar apenas o Codespaces?

_a partir do minuto 00:46:00_

- Iniciei uma tarefa, mas não conclui. Devo fazer o commit?
- Qual o melhor momento para fazer o commit?
- Só o comando `git add` é suficiente para salvar as nossas alterações?

_a partir do minuto 00:51:00_

- Se eu tiver uma dúvida ao longo do curso, eu devo deixar nos comentários, perguntar durante os encontros ou abrir um novo issue?

_a partir do minuto 01:02:00_

- Como posso incluir imagens em arquivos `.md`?

_a partir do minuto 01:11:00_

- Como os atalhos `ctrl + c` e `ctrl +v` funcionam no terminal?


### Issues criados no encontro

- [Sugestão de criar lista de principais comandos usados nas aulas](https://github.com/splor-mg/trilha-dev/issues/57)
- [Descobrir porque o Poetry pode estar instalado em projeto que já tem um codespaces com a ferramenta instalada](https://github.com/splor-mg/trilha-dev/issues/56)

### Avisos e Alinhamentos

- Os novos usuários do Github foram convidados para fazer parte da organização `splor-mg` no Github. O convite foi enviado para o e-mail cadastrado na conta do  github do usuário.
- Desafio lançado: Encontrar um erro ou uma sugestão de melhoria neste site e abrir um [issue no repositório do Trilha-dev](https://github.com/splor-mg/trilha-dev/issues).


## 3º Encontro

- Data: 29/08/2025
- Gravação: [Link do YouTube](https://youtu.be/8puLzCrlfYg)

### Dúvidas

_a partir do minuto 00:15:00_

- Como funciona a ativação do fator de dupla autenticação no Github?

_a partir do minuto 00:20:00_

- E se eu precisar instalar uma nova dependência durante a execução do meu projeto?
- Quais outros tipos de depend6encias poderiam surgir?

_a partir do minuto 00:25:00_

- Como eu descubro se a ferramenta, ou dependência, que eu quero implementar no meu projeto é compatível com as demais ferramentas utilizadas, como o mkdocs?

_Exemplo 01 de uso da biblioteca Vegalite._

```vegalite
{
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```
_Exemplo 02 de uso da biblioteca Vegalite._

```vegalite
{
  "schema-url": "assets/charts/lines.json"
}
```

_a partir 00:53:00_

- Qual a melhor ferramenta para documentar o nosso trabalho? Um novo site estático, um issue, o [Handbook da Splor](https://splor-mg.github.io/handbook/)?

_a partir 00:59:00_
- Qual a melhor ferramenta para documentar informações básicas da Splor?

### Issues criados no encontro
- [Criar uma lista de histórico de perguntas que serão utilizadas na aba FAQ](https://github.com/splor-mg/handbook/issues/142#issuecomment-3242406725)
- [Como procurar uma nova ferramenta para MKDOCS](https://github.com/splor-mg/trilha-dev/issues/72)

### Avisos e Alinhamentos

- Desafio lançado: Instalar a biblioteca [Mermaid](https://squidfunk.github.io/mkdocs-material/reference/diagrams/) para incluir fluxo e diagramas no seu site. :rocket:
- O encontro da próxima semana será dividido entre tira-dúvidas e um Live Code, no qual criaremos uma sessão no Handbook.

## 4º Encontro

- Data: 04/09/2025
- Gravação: [Link do YouTube](https://youtu.be/9TqAc1l_XhY)

### Dúvidas

_a partir do minuto 00:11:00_

- Como disponibilizar um documento de texto (.docx) para download no meu site mkdocs?
!!! note ""

    Para responder essa questão, além das dicas do vídeo, foi criado este [issue](https://github.com/splor-mg/trilha-dev/issues/78). Não deixe de acompanhar o desenvolvimento dessa questão por lá também!

_a partir do minuto 00:25:00_

- Depois do meu site publicado, como posso visualizar em tempo real as alterações que estou fazendo?

### Avisos e Alinhamentos
#### Projetos Especiais

- Os dois últimos encontros do Trilha - Dev, 25/09/2025 e 02/10/2025, serão dedicados ao desenvolvimento de um projeto especial.
- Este projeto especial será desenvolvido por diretoria. A ideia é que os membros das diretorias, em vista do conteúdo abordado, escolham um processo para ser remodelado usando as ferramentas propostas no curso.
- Os encontros serão usados para auxílio na estruturação e desenvolvimento dos projetos, inclusive com o compartilhamento com os colegas da proposta de cada um.
- Desse modo, para a próxima semana, os participantes devem trazer sugestões de processos das suas respectivas diretorias para fazermos um projeto final do curso.

## 5º Encontro

- Data: 11/09/2025
- Gravação: [Link do YouTube](https://youtu.be/udTThKmJUXY)

### Dúvidas

_a partir do minuto 00:04:00_

- Qual a diferença entre os comandos `git checkout` e `git switch`?

_a partir do minuto 00:22:00_

- **Live Code** :rocket::rocket::rocket:
    - Criação de uma aba de Perguntas frequentes - FAQ no Handbook da Splor/MG.
    - Confira o issue criado para execução dessa tarefa: [Criar aba Perguntas frequentes no Handbook](https://github.com/splor-mg/handbook/issues/144)
    - Confira o resultado: [FAQ](https://splor-mg.github.io/handbook/faq/)

_a partir do minuto 00:28:00_

- O que eu devo colocar no arquivo `read.md`?

### Avisos e Alinhamentos
#### Projetos Especiais

- Os projetos desenvolvidos no âmbito do Trilha-Dev serão apresentados para toda a Splor.
- Nas próximas semanas, vamos discutir os projetos escolhidos e iniciar o seu desenvolvimento.

## 6º Encontro

- Data: 18/09/2025
- Gravação: [Link do YouTube](https://youtu.be/iDtrgsdpOK4)

### Dúvidas

_a partir do minuto 00:01:00_

- O que eu faço quando abro um pull request e o Github indica conflito?

_a partir do minuto 00:11:00_

- O que eu faço quando eu preciso atualizar uma ferramenta que eu uso no meu projeto?

_a partir do minuto 00:26:00_

- Na organização da Splor, existem regras para contribuir ou qualquer membro pode fazer alterações nos respositórios?

_a partir do minuto 00:40:00_

- Qual a diferença entre fazer o clone e o _fork_ de um repositório?

_a partir do minuto 00:56:00_

- Como eu posso usar o terminal quando o servidor está ligado?

### Avisos e Alinhamentos

- Finalizado o material do curso, aqueles que quiserem certificado de conclusão, deverão abrir um issue no reposiório do Trilha - Dev, marcando a `raianecardoso`, e indicando a url pública do site construído no decorrer do curso. Veja as orientações completas em [certificação](../certificacao.md).
