---
title: Terminal
---

# :material-console: Terminal

[← Voltar ao guia](../)

---

## **Navegação**

Mostra o diretório atual:
```bash
pwd
```

Lista arquivos e pastas:
```bash
ls
```

Lista arquivos e pastas em formato detalhado, incluindo arquivos ocultos:
```bash
ls -la
```

Entra em uma pasta:
```bash
cd pasta
```

Volta um nível:
```bash
cd ..
```

Volta dois níveis:
```bash
cd ../..
```

Vai para a pasta pessoal do usuário:
```bash
cd ~
```

Volta para o último diretório acessado:
```bash
cd -
```

---

## **Arquivos e pastas**

Cria uma nova pasta:
```bash
mkdir nome-da-pasta
```

Cria pastas aninhadas de uma vez:
```bash
mkdir -p pasta/subpasta
```

Cria um arquivo vazio:
```bash
touch arquivo.txt
```

Copia um arquivo:
```bash
cp arquivo.txt copia.txt
```

Copia uma pasta inteira:
```bash
cp -r origem/ destino/
```

Move um arquivo para outra pasta:
```bash
mv arquivo.txt outra-pasta/
```

Renomeia um arquivo:
```bash
mv nome-antigo.txt nome-novo.txt
```

Remove um arquivo:
```bash
rm arquivo.txt
```

Remove uma pasta e todo o seu conteúdo:
```bash
rm -r pasta/
```

!!! warning "Atenção"
    O `rm` remove permanentemente, sem lixeira. Use com cuidado.

---

## **Visualização de conteúdo**

Exibe o conteúdo completo de um arquivo:
```bash
cat arquivo.txt
```

Visualiza o arquivo paginado (tecle `q` para sair):
```bash
less arquivo.txt
```

Mostra as primeiras linhas do arquivo:
```bash
head arquivo.txt
```

Mostra as últimas linhas do arquivo:
```bash
tail arquivo.txt
```

---

## **Edição no terminal**

Abre o editor de texto no terminal:
```bash
nano arquivo.txt
```

---

## **Busca**

Busca um texto dentro de um arquivo:
```bash
grep "texto" arquivo.txt
```

Busca recursiva em todos os arquivos do diretório:
```bash
grep -r "texto" .
```

Busca arquivos pelo nome:
```bash
find . -name "arquivo.txt"
```

---

## **Histórico**

Lista os últimos comandos executados:
```bash
history
```

---

## **Compactação**

Compacta uma pasta em zip:
```bash
zip -r arquivos.zip pasta/
```

Extrai um arquivo zip:
```bash
unzip arquivos.zip
```

---

## **Atalhos úteis**

| Atalho | Ação |
|--------|------|
| `Ctrl + L` | Limpa o terminal |
| `Ctrl + C` | Interrompe o processo em execução |
| `↑` / `↓` | Navega pelo histórico de comandos |

---
