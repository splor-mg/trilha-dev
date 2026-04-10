---
comments: true
---
# Aula 015: Estruturas de repetição

## 🎥 Vídeo 15

Nesta aula, vamos aprender sobre estruturas de repetição com o `while` loop.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gsRNR-9tPz8?si=rIlINfPv-lkGzbrc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### **O que é o while?**

O **while** é utilizado para criar _loops_, ou seja, repetir um bloco de código enquanto uma condição for _verdadeira_.

A estrutura básica é:

``` py
while condição:
  # bloco de código
```

#### **Exemplo básico**

Vamos criar uma variável de controle:

``` py
i = 1
while i <= 5:
  print(i)
  i = i + 1

print('Terminou!')
```

Funcionamento:

- i = 1 → imprime 1
- incrementa → i = 2
- verifica → 2 <= 5 → imprime 2
- continua até i = 5

Quando:

``` py
- i = 6 → 6 <= 5 é falso
- o loop termina
```

Podemos adicionar:

``` py
print("Loop terminado")
```

#### **Importância do incremento**

O incremento **(i + 1)** é essencial.
Sem ele a condição permaneceria sempre _verdadeira_, gerando um _loop infinito_.

#### **Exemplo com repetição de _string_**

Podemos usar o valor de **i** para repetir uma _string_:

``` py
i = 1
while i <= 5:
  print("*" * i)
  i = i + 1
```

Resultado:

``` py
*
**
***
****
*****
```

Nesse caso:

- A string **"*"** é multiplicada por **i**
- O número de repetições aumenta a cada iteração

#### **Funcionamento do _loop_**

O **while** segue este fluxo:

1.  Verifica a condição;
2.  Executa o bloco;
3.  Retorna para a condição;
4.  Repete enquanto for _verdadeira_.

#### **Checklist**

Ao final desta aula você aprendeu:

- O que é e como funciona o **while**?
- Como criar _loops_ em Python
- A importância da variável de controle
- Como evitar _loops infinitos_
- Como utilizar repetição para gerar padrões

Estruturas de repetição são fundamentais para automatizar tarefas e executar ações repetidas em programas.
