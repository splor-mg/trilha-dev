---
title: Sistema
---

# Sistema

[← Voltar ao guia](../)

---

## Integração com o sistema

```bash
code .          # Abre projeto no VS Code
explorer.exe .  # Abre pasta no Windows Explorer
wsl --shutdown  # Reinicia WSL (executado no PowerShell)
```

## Informações do sistema

```bash
whoami      # Mostra usuário atual
uname -a    # Informações do sistema operacional
df -h       # Espaço em disco
```

## Processos e Portas

```bash
lsof -i         # Lista processos utilizando portas
kill -9 PID     # Encerra processo pelo identificador
ps aux          # Lista processos ativos
top             # Monitora processos em tempo real
kill PID        # Finaliza processo
```
#### Obs.: Utilize esses comandos quando uma porta estiver ocupada e impedir a execução do servidor local.
