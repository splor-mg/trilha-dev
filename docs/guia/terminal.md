---
title: Terminal
---

[← Voltar ao guia](../)

---

## Navegação e Arquivos

```bash
pwd       # Mostra o diretório atual
ls        # Lista arquivos e pastas
ls -la    # Lista detalhada (inclui arquivos ocultos)

cd pasta  # Entra em uma pasta
cd ..     # Volta um nível
cd ../..  # Volta dois níveis

mkdir nome-pasta  # Cria uma nova pasta
touch arquivo.txt # Cria um arquivo vazio

cp arquivo.txt copia.txt      # Copia arquivo
cp -r pasta origem/ destino/  # Copia pasta

mv arquivo.txt nova_pasta/        # Move arquivo
mv nome_antigo.txt nome_novo.txt  # Renomeia arquivo

rm -rf pasta  # Remove pasta e conteúdo (uso com cautela)

clear         # Limpa o terminal (alternativa ao Ctrl + L)
```

!!! warning "Atenção"
    O comando **`rm -rf`** remove arquivos permanentemente.

## Visualização e Inspeção

```bash
cat arquivo.txt       # Exibe conteúdo do arquivo
less arquivo.txt      # Visualiza arquivo paginado

head arquivo.txt      # Mostra início do arquivo
tail arquivo.txt      # Mostra final do arquivo
tail -f arquivo.txt   # Acompanha arquivo em tempo real

history               # Mostra histórico de comandos
```

## Busca

```bash
grep "texto" arquivo.txt      # Busca texto dentro de arquivo
grep -r "texto" .             # Busca recursiva em diretórios

find . -name "arquivo.txt"    # Busca arquivos por nome
```

## Atalhos úteis

```bash
Ctrl + L    # Limpa o terminal
Ctrl + C    # Interrompe um processo em execução
Ctrl + Z    # Suspende um processo
```

## Permissões

```bash
chmod +x script.sh            # Torna arquivo executável
chmod 755 arquivo             # Define permissões
chown usuario:grupo arquivo   # Altera dono do arquivo
```
