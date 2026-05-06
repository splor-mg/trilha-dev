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

## Processos e Portas

```bash
lsof -i         # Lista processos utilizando portas
kill -9 PID     # Encerra processo pelo identificador
```
#### Obs.: Utilize esses comandos quando uma porta estiver ocupada e impedir a execução do servidor local.
