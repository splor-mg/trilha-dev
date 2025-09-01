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