??? warning "Custo do GitHub Codespaces"
    O uso do GitHub Codespaces **não é totalmente gratuito**. Existe uma cota mensal gratuita, e após ultrapassá-la, haverá cobrança.

    Consulte os preços atualizados na documentação [Cobrança do GitHub Codespaces](https://docs.github.com/pt/billing/concepts/product-billing/github-codespaces), bem como as regras de cálculo da cota gratuita e cobranças na documentaçfão [Como aproveitar ao máximo o uso incluído](https://docs.github.com/pt/codespaces/troubleshooting/troubleshooting-included-usage).

    ### 🧮 Estimativa de uso neste curso

    Considerando o uso de **4 horas por semana**:

    - ~4 semanas/mês → **16 horas/mês (tempo real)**.

    A cota gratuita inclui:

    - **120 core-hours/mês**.
    - **15 GB-mês de armazenamento**.

    > O consumo de core-hours/mês é calculado sobre o **tempo de uso × número de cores da máquina (multiplicador)**.
    > O consumo de armazenamento é calculado sobre o utilizado e não sobre a capacidade total da máquina.

    ### 📊 Comparação por tipo de máquina

    | Máquina | Multiplicador | Uso mensal (tempo real) | Consumo (core-hours) | Situação |
    |--------|---------------|--------------------------|----------------------|----------|
    | 2 cores | 2 | 16 h | 32 | ✅ Dentro da cota |
    | 4 cores | 4 | 16 h | 64 | ✅ Dentro da cota |
    | 8 cores | 8 | 16 h | 128 | ⚠️ Excede a cota |
    | 16 cores | 16 | 16 h | 256 | ❌ Excede a cota |

    ### 💾 Armazenamento

    | Recurso        | Cota gratuita | Uso estimado | Situação |
    |----------------|--------------|-------------|----------|
    | Storage        | 15 GB-mês    | ~1–2 GB*    | ✅ Dentro da cota |

    \* Estimativa considerando um ambiente simples de desenvolvimento Python.

    ### 💡 Conclusão

    - Para este curso, recomenda-se usar máquinas de **2 ou 4 cores**.
    - Máquinas de **8 cores ou mais podem gerar cobrança**, mesmo com uso moderado.

    ### 🔒 Importante sobre cobranças

    Se sua conta **não possuir um método de pagamento cadastrado**, o uso será **interrompido automaticamente ao atingir a cota gratuita**.

    Ou seja, você **não será cobrado inesperadamente**, apenas não conseguirá continuar utilizando o Codespaces até o próximo ciclo ou até adicionar uma forma de pagamento.

    ⚠️ Custos podem ocorrer se você:
    - adicionar um método de pagamento.
    - aumentar o tempo de uso.
    - usar máquinas maiores.
    - manter múltiplos codespaces ativos.
