import random

def gerar_mensagem(nome):
    # Passo 1 — gera uma chave aleatória entre 1 e 25
    chave = random.randint(1, 25)

    # Passo 2 — monta a mensagem original (REGRA: caixa alta, sem acentos). Caso queira modificar a mensagem, altere abaixo.
    mensagem = f"PARABENS, {nome.upper()}! VOCE CONCLUIU O CURSO TRILHA DEV PYTHON"

    # Passo 3 — codifica a mensagem com a Cifra de César
    mensagem_codificada = ""
    for char in mensagem:
        if char.isalpha():
            novo_indice = (ord(char) - ord('A') + chave) % 26
            nova_letra = chr(novo_indice + ord('A'))
            mensagem_codificada += nova_letra
        else:
            mensagem_codificada += char

    return chave, mensagem_codificada


# Exemplo de uso
chave, mensagem_codificada = gerar_mensagem("") # Insira o nome do aluno(a) aqui.
print(f"Chave: {chave}")
print(f"Mensagem codificada: {mensagem_codificada}")