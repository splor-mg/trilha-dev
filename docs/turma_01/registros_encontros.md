---
comments: true
---

# Registros dos Encontros da Primeira Turma

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

## 3º Encontro

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

```vegalite
{
  "schema-url": "assets/charts/lines.json"
}
```
