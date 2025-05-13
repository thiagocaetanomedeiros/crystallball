Aqui estão as fórmulas contidas no arquivo PDF, juntamente com o código Python para cada uma delas:

1.  **Cálculo da Taxa Efetiva Anual a partir do PU (Preço Unitário)**[cite: 106, 107]:

    * Fórmula:  $Taxa=([\frac{VN}{PU}]^{\frac{252}{du}}-1)x~100$
    * Onde:
        * $VN$ = Valor Nominal do título
        * $PU$ = Preço Unitário do título
        * $Taxa$ = Taxa Efetiva anual
        * $du$ = dias úteis
    * Código Python:

        ```python
        def calcular_taxa_efetiva(VN, PU, du):
          """
          Calcula a taxa efetiva anual a partir do preço unitário.

          Args:
              VN (float): Valor Nominal do título.
              PU (float): Preço Unitário do título.
              du (int): Dias úteis.

          Returns:
              float: Taxa Efetiva anual.
          """
          taxa = ((VN / PU) ** (252 / du) - 1) * 100
          return taxa

        # Exemplo de uso
        VN = 1000  # Valor Nominal
        PU = 883    # Preço Unitário
        du = 252    # Dias úteis

        taxa = calcular_taxa_efetiva(VN, PU, du)
        print(f"A Taxa Efetiva anual é: {taxa:.2f}%")
        ```

2.  **Cálculo do PU a partir da Taxa Efetiva Anual**[cite: 107]:

    * Fórmula: $PU=\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{du}{252}}}$
    * Onde:
        * $VN$ = Valor Nominal do título
        * $PU$ = Preço Unitário do título
        * $Taxa$ = Taxa Efetiva anual
        * $du$ = dias úteis
    * Código Python:

        ```python
        def calcular_pu(VN, taxa, du):
          """
          Calcula o Preço Unitário do título a partir da taxa efetiva anual.

          Args:
              VN (float): Valor Nominal do título.
              taxa (float): Taxa Efetiva anual.
              du (int): Dias úteis.

          Returns:
              float: Preço Unitário do título.
          """
          pu = VN / ((taxa / 100 + 1) ** (du / 252))
          return pu

        # Exemplo de uso
        VN = 1000  # Valor Nominal
        taxa = 13.25 # Taxa Efetiva anual
        du = 252    # Dias úteis

        pu = calcular_pu(VN, taxa, du)
        print(f"O Preço Unitário do título é: R$ {pu:.2f}")
        ```

3.  **Conversão de Taxa Periódica**[cite: 126]:

    * Fórmula: $De\ Taxa\ periodo_0\ para\ taxa\ periodo_1 = (1 + i\%)^{\frac{n}{m}} - 1$
    * Onde:
        * $i$ = Taxa de Juros em um determinado período (ex. ano)
        * $m$ = Número de dias referente aos juros (exemplo 252)
        * $n$ = Número de dias referente ao período que se deseja calcular a taxa (exemplo semestre ou 126 dias)
    * Código Python:

        ```python
        def converter_taxa_periodica(i, m, n):
          """
          Converte a taxa de juros de um período para outro.

          Args:
              i (float): Taxa de Juros no período original (ex. ano).
              m (int): Número de dias do período original.
              n (int): Número de dias do período para conversão.

          Returns:
              float: Taxa de juros no novo período.
          """
          taxa_convertida = (1 + i / 100) ** (n / m) - 1
          return taxa_convertida

        # Exemplo de uso
        taxa_anual = 10  # 10% ao ano
        dias_ano = 252
        dias_semestre = 126

        taxa_semestral = converter_taxa_periodica(taxa_anual, dias_ano, dias_semestre)
        print(f"Taxa semestral: {taxa_semestral * 100:.3f}%")
        ```

4.  **Cálculo do PU de Título Prefixado com Cupons**[cite: 120, 121, 122]:

    * Fórmula: $PU = \sum_{t=1}^{T} \frac{Ct}{[\frac{Taxa}{100} + 1]^{\frac{t}{252}}} + \frac{VN}{[\frac{Taxa}{100} + 1]^{\frac{T}{252}}}$
    * Onde:
        * $PU$ = Preço unitário do ativo.
        * $VN$ = Valor Nominal do título.
        * $Ct$ = Pagamento de principal, cupom ou ambos no período t.
        * $t$ = Cada um dos períodos (anual, semestral ou outro) para cada pagamento.
        * $T$ = Quantidade de Períodos até o último vencimento.
        * $Taxa$ = Taxa de retorno do Título até o vencimento
        * $d.u.$ = dias úteis
    * Código Python:

        ```python
        def calcular_pu_prefixado_cupom(cupons, datas_cupons, VN, taxa, data_hoje):
            """
            Calcula o Preço Unitário de um título prefixado com cupons.

            Args:
                cupons (list): Lista dos valores dos cupons.
                datas_cupons (list): Lista das datas de pagamento dos cupons.
                VN (float): Valor Nominal do título.
                taxa (float): Taxa de retorno do título até o vencimento (a.a.).
                data_hoje (date): Data de hoje.

            Returns:
                float: Preço Unitário do título.
            """

            PU = 0
            for i, cupom in enumerate(cupons):
                du = np.busday_count(data_hoje, datas_cupons[i])
                PU += cupom / ((1 + taxa / 100) ** (du / 252))

            du_vencimento = np.busday_count(data_hoje, datas_cupons[-1])
            PU += VN / ((1 + taxa / 100) ** (du_vencimento / 252))

            return PU

        # Exemplo de uso
        import datetime
        import numpy as np

        VN = 1000
        taxa_anual = 11
        data_hoje = datetime.date(2023, 9, 25)
        datas_pagamento = [datetime.date(2024, 1, 2), datetime.date(2024, 7, 1), datetime.date(2025, 1, 2)]
        cupons = [48.80885, 48.80885, 1048.80885]  # Inclui o VN no último pagamento

        pu = calcular_pu_prefixado_cupom(cupons, datas_pagamento, VN, taxa_anual, data_hoje)
        print(f"O Preço Unitário do título é: R$ {pu:.2f}")
        ```

5.  **Cálculo do VNA (Valor Nominal Atualizado) para títulos IPCA+**[cite: 162, 163, 164]:

    * Fórmula: $VNA = 1.000 * \prod_{i=1}^{n-1} (1 + \frac{Indice\ Mensal_n}{100})$
    * Código Python:

        ```python
        def calcular_vna(indices_mensais):
          """
          Calcula o Valor Nominal Atualizado (VNA) para títulos IPCA+.

          Args:
              indices_mensais (list): Lista das variações mensais do IPCA (em %).

          Returns:
              float: Valor Nominal Atualizado.
          """
          vna = 1000
          for indice in indices_mensais:
            vna *= (1 + indice / 100)
          return vna

        # Exemplo de uso
        indices_mensais = [0.5, 0.6, 0.4]  # Exemplo de variações mensais do IPCA
        vna = calcular_vna(indices_mensais)
        print(f"O Valor Nominal Atualizado (VNA) é: R$ {vna:.2f}")
        ```

6.  **Cálculo do VNA com Projeção Mensal**[cite: 165, 166, 167]:

    * Fórmula: $VNA = 1.000 * \prod_{1}^{n-1} (1 + \frac{Indice\ Mensal_n}{100}) * (1 + \frac{Projeção\ Mensal}{100})^{\frac{du\ dia}{du_{mes}}}$
    * Onde:
        * $Du\ dia$ = número de dias úteis entre a última divulgação do índice e a data de cálculo;
        * $Du\ Mês$ = número de dias úteis entre a última e a próxima divulgação do índice.
    * Código Python:

        ```python
        import numpy as np

        def calcular_vna_projecao(indices_mensais, projecao_mensal, du_dia, du_mes):
          """
          Calcula o VNA para títulos IPCA+ com projeção mensal.

          Args:
              indices_mensais (list): Variações mensais do IPCA até a última divulgação.
              projecao_mensal (float): Projeção mensal do IPCA (%).
              du_dia (int): Dias úteis entre a última divulgação e a data de cálculo.
              du_mes (int): Dias úteis entre a última e a próxima divulgação.

          Returns:
              float: Valor Nominal Atualizado.
          """

          vna = 1000
          for indice in indices_mensais:
              vna *= (1 + indice / 100)
          vna *= (1 + projecao_mensal / 100) ** (du_dia / du_mes)
          return vna

        # Exemplo de uso
        indices_mensais = [0.5, 0.6, 0.4]
        projecao_mensal = 0.7
        du_dia = 10
        du_mes = 20

        vna = calcular_vna_projecao(indices_mensais, projecao_mensal, du_dia, du_mes)
        print(f"VNA com projeção: R$ {vna:.2f}")
        ```

7.  **Cálculo do PU para Títulos IPCA+**[cite: 179]:

    * Fórmula: $PU = \frac{VNA}{[\frac{Taxa}{100} + 1]^{\frac{du}{252}}}$
    * Código Python:

        ```python
        def calcular_pu_ipca(VNA, taxa, du):
          """
          Calcula o Preço Unitário (PU) para títulos IPCA+.

          Args:
              VNA (float): Valor Nominal Atualizado.
              taxa (float): Taxa de juros anual (%).
              du (int): Dias úteis até o vencimento.

          Returns:
              float: Preço Unitário do título.
          """
          pu = VNA / ((1 + taxa / 100) ** (du / 252))
          return pu

        # Exemplo de uso
        VNA = 4144.46
        taxa = 5.5
        du = 223

        pu = calcular_pu_ipca(VNA, taxa, du)
        print(f"O Preço Unitário (PU) é: R$ {pu:.2f}")
        ```

8.  **Conversão da Taxa Anual para Taxa Diária**[cite: 210]:

    * Fórmula: $De\ Taxa\ Anual\ para\ Taxa\ diária = (1 + Taxa\ Anual\%)^{\frac{1}{252}} - 1$
    * Código Python:

        ```python
        def converter_taxa_anual_para_diaria(taxa_anual):
          """
          Converte uma taxa de juros anual para a taxa diária equivalente (considerando 252 dias úteis).

          Args:
              taxa_anual (float): A taxa de juros anual (em %).

          Returns:
              float: A taxa de juros diária equivalente.
          """
          taxa_diaria = (1 + taxa_anual / 100) ** (1 / 252) - 1
          return taxa_diaria

        # Exemplo de uso
        taxa_anual = 13.15  # Exemplo de taxa anual
        taxa_diaria = converter_taxa_anual_para_diaria(taxa_anual)
        print(f"Taxa diária: {taxa_diaria * 100:.5f}%")
        ```

9.  **Capitalização Diária**[cite: 211]:

    * Fórmula: $Capitalização\ diária = DI\ diário * \% do\ DI$
    * Código Python:

        ```python
        def calcular_capitalizacao_diaria(di_diario, percentual_di):
          """
          Calcula a capitalização diária de um título referenciado ao DI.

          Args:
              di_diario (float): A taxa DI diária.
              percentual_di (float): O percentual do DI a ser considerado (ex: 120%).

          Returns:
              float: A capitalização diária.
          """
          capitalizacao_diaria = di_diario * (percentual_di / 100)
          return capitalizacao_diaria

        # Exemplo de uso
        di_diario = 0.000490375  # Exemplo de taxa DI diária (já convertida para decimal)
        percentual_di = 120       # 120% do DI
        capitalizacao = calcular_capitalizacao_diaria(di_diario, percentual_di)
        print(f"Capitalização diária: {capitalizacao * 100:.5f}%")
        ```

10. **Valor Nominal Atualizado Diário**[cite: 212]:

    * Fórmula: $VN\ de\ hoje = VN\ de\ ontem * (1 + Cap.\ Diária)$
    * Código Python:

        ```python
        def calcular_vn_hoje(vn_ontem, cap_diaria):
          """
          Calcula o Valor Nominal (VN) de hoje a partir do VN de ontem e da capitalização diária.

          Args:
              vn_ontem (float): Valor Nominal do dia anterior.
              cap_diaria (float): Capitalização diária (em decimal).

          Returns:
              float: Valor Nominal de hoje.
          """
          vn_hoje = vn_ontem * (1 + cap_diaria)
          return vn_hoje

        # Exemplo de uso
        vn_ontem = 1000.00  # Exemplo de VN de ontem
        cap_diaria = 0.000588450  # Exemplo de capitalização diária
        vn_hoje = calcular_vn_hoje(vn_ontem, cap_diaria)
        print(f"Valor Nominal de hoje: {vn_hoje:.2f}")
        ```

11. **Cálculo do Valor Nominal para Títulos DI + Taxa Pré**[cite: 217, 218]:

    * Fórmula: $VN_t = VN_{t-1} * (1 + Taxa\ Pre\ a.a.)^{\frac{n}{252}} * (1 + Taxa\ Pos\ a.a.)^{\frac{n}{252}}$
    * Código Python:

        ```python
        def calcular_vn_di_taxa_pre(vn_anterior, taxa_pre, taxa_pos, n_dias):
          """
          Calcula o Valor Nominal (VN) de um título DI + Taxa Pré.

          Args:
              vn_anterior (float): VN do período anterior.
              taxa_pre (float): Taxa Pré-fixada a.a. (em %).
              taxa_pos (float): Taxa Pós-fixada (DI) a.a. (em %).
              n_dias (int): Número de dias no período.

          Returns:
              float: VN atualizado.
          """

          vn_atualizado = vn_anterior * \
                         ((1 + taxa_pre / 100) ** (n_dias / 252)) * \
                         ((1 + taxa_pos / 100) ** (n_dias / 252))
          return vn_atualizado

        # Exemplo de uso
        vn_anterior = 1000.00
        taxa_pre = 2.0
        taxa_pos = 12.65
        n_dias = 10

        vn_atual = calcular_vn_di_taxa_pre(vn_anterior, taxa_pre, taxa_pos, n_dias)
        print(f"Valor Nominal atualizado: R$ {vn_atual:.2f}")
        ```

12. **Cálculo da Taxa de Juros Futura Esperada (FRA)**[cite: 253, 254, 255]:

    * Fórmula: $(1 + i_{(t, t+1)}) * (1 + i^e_{(t+1, t+2)}) = (1 + i_{(t, t+2)})$
    * Onde:
        * $(1 + i_{(t, t+1)})$ é a taxa de juros praticada entre t e t+1
        * $(1 + i_{(t, t+2)})$ é a taxa de juros praticada entre t e t+2
        * $(1 + i^e_{(t+1, t+2)})$ é a taxa de juros esperada entre o tempo t+1 e t+2
    * Código Python:

        ```python
        def calcular_taxa_juros_futura(taxa_tt1, taxa_tt2):
          """
          Calcula a taxa de juros futura esperada usando a fórmula do FRA.

          Args:
              taxa_tt1 (float): Taxa de juros entre o período t e t+1 (em decimal).
              taxa_tt2 (float): Taxa de juros entre o período t e t+2 (em decimal).

          Returns:
              float: A taxa de juros futura esperada entre t+1 e t+2 (em decimal).
          """
          taxa_futura = (1 + taxa_tt2) / (1 + taxa_tt1) - 1
          return taxa_futura

        # Exemplo de uso
        taxa_jan_mar = 0.03  # 3%
        taxa_jan_jul = 0.075 # 7.5%
        taxa_mar_jul = calcular_taxa_juros_futura(taxa_jan_mar, taxa_jan_jul)
        print(f"Taxa de juros esperada entre março e julho: {taxa_mar_jul * 100:.2f}%")
        ```

13. **Cálculo da Duration**[cite: 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305]:

    * Fórmula: $Duration = \frac{\sum_{t=1}^{N} t_i \frac{CF_t}{(1 + i)^n}}{\sum_{t=1}^{N} \frac{CF_t}{(1 + i)^n}}$
    * Onde:

        * N = número de períodos até o vencimento.
        * CFt = é o fluxo de caixa no período t.
        * ti = é o prazo até o recebimento do fluxo
        * i = é a taxa de desconto.
    * Código Python:

        ```python
        def calcular_duration(fluxos_caixa, prazos, taxa_desconto):
            """
            Calcula a Duration de um título de renda fixa.

            Args:
                fluxos_caixa (list): Lista dos fluxos de caixa do título.
                prazos (list): Lista dos prazos correspondentes a cada fluxo de caixa (em anos).
                taxa_desconto (float): Taxa de desconto anual (em decimal).

            Returns:
                float: A Duration do título.
            """

            numerador = sum(t * cf / ((1 + taxa_desconto) ** t) for t, cf in zip(prazos, fluxos_caixa))
            denominador = sum(cf / ((1 + taxa_desconto) ** t) for t, cf in zip(prazos, fluxos_caixa))
            duration = numerador / denominador if denominador else 0
            return duration

        # Exemplo de uso
        fluxos_caixa = [40, 40, 1040]  # Fluxos de caixa
        prazos = [1, 2, 3]             # Prazos em anos
        taxa_desconto = 0.04          # Taxa de desconto

        duration = calcular_duration(fluxos_caixa, prazos, taxa_desconto)
        print(f"A Duration do título é: {duration:.2f} anos")
        ```

14. **Cálculo da Variação Percentual do Título**[cite: 300, 301, 302, 303, 304, 305]:

    * Fórmula: $ΔP ≈ -Duration * Δi$
    * Código Python:

        ```python
        def calcular_variacao_percentual(duration, variacao_taxa):
          """
          Calcula a variação percentual do preço de um título usando a Duration.

          Args:
              duration (float): A Duration do título.
              variacao_taxa (float): A variação na taxa de juros (em decimal).

          Returns:
              float: A variação percentual do preço do título.
          """
          variacao_percentual = -duration * variacao_taxa
          return variacao_percentual

        # Exemplo de uso
        duration = 2.88
        variacao_taxa = 0.05 - 0.04  # Variação de 4% para 5%
        variacao_percentual = calcular_variacao_percentual(duration, variacao_taxa)

        print(f"A variação percentual do título é: {variacao_percentual * 100:.2f}%")
        ```

15. **Medindo a Convexidade**[cite: 316, 317, 318, 319, 320, 321]:

    * Fórmula: $Convexidade = \frac{V+ + V- - 2V_0}{2V_0(Δy)^2}$

        * Onde:

            * V+ = Preço quando os juros caem y%
            * V- = Preço quando os juros sobem y%
            * V₀ = Preço Inicial
            * Δy = variação das taxas de juros
    * Código Python:

        ```python
        def calcular_convexidade(preco_aumento, preco_reducao, preco_inicial, variacao_taxa):
          """
          Calcula a convexidade de um título de renda fixa.

          Args:
              preco_aumento (float): Preço do título quando a taxa de juros aumenta.
              preco_reducao (float): Preço do título quando a taxa de juros diminui.
              preco_inicial (float): Preço inicial do título.
              variacao_taxa (float): Variação na taxa de juros (em decimal).

          Returns:
              float: A convexidade do título.
          """
          convexidade = (preco_aumento + preco_reducao - 2 * preco_inicial) / (2 * preco_inicial * (variacao_taxa ** 2))
          return convexidade

        # Exemplo de uso
        preco_inicial = 134.42
        preco_aumento = 132.99
        preco_reducao = 135.85
        variacao_taxa = 0.01  # 1% de variação (0.01 em decimal)

        convexidade = calcular_convexidade(preco_aumento, preco_reducao, preco_inicial, variacao_taxa)
        print(f"A convexidade do título é: {convexidade:.4f}")
        ```

16. **Variação no Preço do Título com Convexidade e Duration**[cite: 317, 318, 319, 320, 321]:

    * Fórmula: $Variação\ no\ preço\ do\ Título = -Duration(Δy) + 0,5 * Convexidade(Δy)^2$
    * Código Python:

        ```python
        def calcular_variacao_preco_com_convexidade(duration, convexidade, variacao_taxa):
          """
          Calcula a variação no preço de um título usando Duration e Convexidade.

          Args:
              duration (float): A Duration do título.
              convexidade (float): A Convexidade do título.
              variacao_taxa (float): Variação na taxa de juros (em decimal).

          Returns:
              float: A variação no preço do título.
          """
          variacao_preco = -duration * variacao_taxa + 0.5 * convexidade * (variacao_taxa ** 2)
          return variacao_preco

        # Exemplo de uso
        duration = 11.2477
        convexidade = 6.0795
        variacao_taxa = 0.01  # 1% de variação na taxa de juros

        variacao_no_preco = calcular_variacao_preco_com_convexidade(duration, convexidade, variacao_taxa)
        print(f"Variação no preço do título: {variacao_no_preco:.2f}")
        ```

Este conjunto de códigos Python implementa as fórmulas financeiras encontradas no documento, permitindo calcular métricas importantes para análise de títulos de renda fixa.






Com certeza! A apostila apresenta diversas fórmulas financeiras importantes no contexto da renda fixa. Vamos organizar essas fórmulas em funções Python para facilitar o uso e a criação da sua biblioteca.

**1. Prefixado (Bullet)**

* **Conceito:** Títulos prefixados têm sua rentabilidade definida no momento da compra. O investidor recebe o valor investido mais a rentabilidade no vencimento. [cite: 102, 103, 104]

* **Fórmulas:**

    * Cálculo da Taxa Efetiva Anual:  
    
    $Taxa=([\frac{VN}{PU}]^{\frac{252}{du}}-1)x~100$
    
    * Cálculo do PU (Preço Unitário):  
    
    $PU=\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{du}{252}}}$
    
    * Onde:
    
        * $VN$ = Valor Nominal do título
        * $PU$ = Preço Unitário do título
        * $Taxa$ = Taxa Efetiva anual
        * $du$ = dias úteis [cite: 106, 107]
* **Funções Python:**

    ```python
    import numpy as np
    
    def taxa_efetiva_anual(valor_nominal, preco_unitario, dias_uteis):
        """
        Calcula a taxa efetiva anual de um título prefixado (bullet).
    
        Args:
            valor_nominal (float): Valor nominal do título.
            preco_unitario (float): Preço unitário do título.
            dias_uteis (int): Número de dias úteis até o vencimento.
    
        Returns:
            float: Taxa efetiva anual (em %).
        """
        taxa = ((valor_nominal / preco_unitario) ** (252 / dias_uteis) - 1) * 100
        return taxa
    
    def preco_unitario(valor_nominal, taxa_anual, dias_uteis):
        """
        Calcula o preço unitário de um título prefixado (bullet).
    
        Args:
            valor_nominal (float): Valor nominal do título.
            taxa_anual (float): Taxa efetiva anual (em %).
            dias_uteis (int): Número de dias úteis até o vencimento.
    
        Returns:
            float: Preço unitário do título.
        """
        taxa_decimal = taxa_anual / 100
        pu = valor_nominal / ((1 + taxa_decimal) ** (dias_uteis / 252))
        return pu
    
    # Exemplos de uso:
    valor_nominal = 1000
    preco = 883
    dias = 252
    
    taxa = taxa_efetiva_anual(valor_nominal, preco, dias)
    print(f"Taxa efetiva anual: {taxa:.2f}%")  # Saída: 13.25%
    
    pu = preco_unitario(valor_nominal, 13.25, dias)
    print(f"Preço unitário: {pu:.2f}")  # Saída: 883.00
    
    
    ```

**2. Pré-fixado com Cupom**

* **Conceito:** Similar ao prefixado, mas com pagamentos periódicos de juros (cupons) antes do vencimento. [cite: 115, 116, 117]

* **Fórmula:**

    * Cálculo do PU:
    
    $PU=\sum_{t=1}^{T}\frac{Ct}{[\frac{Taxa}{100}+1]^{\frac{t}{252}}}+\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{T}{252}}}$
    
    * Conversão da Taxa:
    
    De Taxa periodom para taxa periodo₁ $=(1+i\%)^{\frac{n}{m}}-1$
    
    * Onde:
    
        * $PU$ = Preço unitário do ativo.
        * $VN$ = Valor Nominal do título.
        * $Ct$ = Pagamento de principal, cupom ou ambos no período t
        * $t$ = cada um dos períodos (anual, semestral ou outro) para cada pagamento.
        * $T$ = Quantidade de Períodos até o último vencimento.
        * Taxa = Taxa de retorno do Título até o vencimento
        * $d.u.$ = dias úteis
        * $i$ = Taxa de Juros em um determinado período (ex. ano)
        * $m$ = Número de dias referente aos juros (exemplo 252)
        * $n$ = Número de dias referente ao período que se deseja calcular a taxa (exemplo semestre ou 126 dias) [cite: 119, 120, 121, 122, 126]
* **Funções Python:**

    ```python
    import numpy as np
    import pandas as pd
    
    def taxa_periodo(taxa_base, dias_base, dias_novo_periodo):
        """
        Converte uma taxa de um período para outro.
    
        Args:
            taxa_base (float): Taxa de juros no período base (ex: anual em %).
            dias_base (int): Número de dias no período base (ex: 252 para ano).
            dias_novo_periodo (int): Número de dias no novo período.
    
        Returns:
            float: Taxa no novo período (em %).
        """
        taxa_decimal = taxa_base / 100
        taxa_convertida = (1 + taxa_decimal) ** (dias_novo_periodo / dias_base) - 1
        return taxa_convertida * 100
    
    def preco_unitario_cupom(valor_nominal, taxa_anual, cupons, datas_cupons, data_vencimento):
        """
        Calcula o preço unitário de um título pré-fixado com cupons.
    
        Args:
            valor_nominal (float): Valor nominal do título.
            taxa_anual (float): Taxa de retorno anual do título (em %).
            cupons (list): Lista com os valores dos cupons.
            datas_cupons (list): Lista com as datas de pagamento dos cupons.
            data_vencimento (datetime): Data de vencimento do título.
    
        Returns:
            float: Preço unitário do título.
        """
        taxa_decimal = taxa_anual / 100
        pu = 0
        data_inicio = pd.to_datetime('today')  # Data de hoje
    
        for i, cupom in enumerate(cupons):
            dias_uteis = np.busday_count(data_inicio.date(), pd.to_datetime(datas_cupons[i]).date())
            pu += cupom / ((1 + taxa_decimal) ** (dias_uteis / 252))
    
        dias_uteis_vencimento = np.busday_count(data_inicio.date(), data_vencimento.date())
        pu += valor_nominal / ((1 + taxa_decimal) ** (dias_uteis_vencimento / 252))
    
        return pu
    
    # Exemplo de uso:
    valor_nominal = 1000
    taxa_anual = 11
    cupons = [48.80885, 48.80885, 1048.80885]  # Cupons e valor nominal no vencimento
    datas_cupons = ['2024-01-02', '2024-07-01', '2025-01-02']
    data_vencimento = pd.to_datetime('2025-01-02')
    
    pu_com_cupom = preco_unitario_cupom(valor_nominal, taxa_anual, cupons, datas_cupons, data_vencimento)
    print(f"Preço unitário com cupons: {pu_com_cupom:.2f}")
    
    taxa_semestral = taxa_periodo(10, 252, 126)
    print(f"Taxa semestral: {taxa_semestral:.2f}%")
    
    
    ```

**3. IPCA + Taxa**

* **Conceito:** Títulos pós-fixados com rentabilidade atrelada à inflação (IPCA) mais uma taxa prefixada. [cite: 160, 161]

* **Fórmulas:**

    * VNA (Valor Nominal Atualizado):
    
    $VNA=1.000~x\prod_{-1}^{n-1}1+\frac{Indice~Mensal_{n}}{100}$
    
    * VNA (com projeção):
    
    $VNA=1.000~x\prod_{1}^{n-1}(1+\frac{Indice~Mensal_{n}}{100})x(1+\frac{Proje\zeta\tilde{a}o~Mensal}{100})^{\frac{du~dia}{du_{mes}}}$
    
    * PU (Preço Unitário):
    
    $PU=\frac{VNA}{[\frac{Taxa}{100}+1]^{\frac{du}{252}}}$
    
    * Onde:
    
        * $VNA$ = Valor Nominal Atualizado
        * $Indice~Mensal_n$ = Índice de inflação do mês n
        * $Projeção~Mensal$ = Projeção do IPCA para o próximo mês
        * $du~dia$ = número de dias úteis entre a última divulgação do índice e a data de cálculo;
        * $du~Mês$ = número de dias uteis entre a última e a próxima divulgação do índice. [cite: 162, 163, 164, 165, 166, 167]
* **Funções Python:**

    ```python
    import numpy as np
    from datetime import date
    
    def calcular_vna(indices_mensais):
        """
        Calcula o Valor Nominal Atualizado (VNA) de um título IPCA+.
    
        Args:
            indices_mensais (list): Lista com os índices de inflação mensais (em %).
    
        Returns:
            float: Valor Nominal Atualizado (VNA).
        """
        vna = 1000
        for indice in indices_mensais:
            vna *= (1 + indice / 100)
        return vna
    
    def calcular_vna_projecao(indices_anteriores, projecao_mensal, dias_uteis_decorridos, dias_uteis_mes):
        """
        Calcula o VNA com projeção do IPCA para o mês atual.
    
        Args:
            indices_anteriores (list): Lista com os índices de inflação mensais anteriores (em %).
            projecao_mensal (float): Projeção do IPCA para o mês atual (em %).
            dias_uteis_decorridos (int): Dias úteis decorridos desde a última divulgação do IPCA.
            dias_uteis_mes (int): Total de dias úteis no mês.
    
        Returns:
             float: Valor Nominal Atualizado (VNA) com projeção.
        """
        vna = 1000
        for indice in indices_anteriores:
            vna *= (1 + indice / 100)
        vna *= (1 + projecao_mensal / 100) ** (dias_uteis_decorridos / dias_uteis_mes)
        return vna
    
    def calcular_pu_ipca(vna, taxa_anual, dias_uteis):
        """
        Calcula o Preço Unitário (PU) de um título IPCA+.
    
        Args:
            vna (float): Valor Nominal Atualizado.
            taxa_anual (float): Taxa de juros anual do título (em %).
            dias_uteis (int): Dias úteis até o vencimento.
    
        Returns:
            float: Preço Unitário (PU).
        """
        taxa_decimal = taxa_anual / 100
        pu = vna / ((1 + taxa_decimal) ** (dias_uteis / 252))
        return pu
    
    # Exemplo de uso
    indices = [0.5, 0.6, 0.4]  # Índices de inflação dos meses anteriores
    vna_calculado = calcular_vna(indices)
    print(f"VNA: {vna_calculado:.2f}")
    
    projecao = 0.7
    dias_decorridos = 15
    dias_no_mes = 22
    vna_projetado = calcular_vna_projecao(indices, projecao, dias_decorridos, dias_no_mes)
    print(f"VNA com projeção: {vna_projetado:.2f}")
    
    pu = calcular_pu_ipca(vna_calculado, 5.5, 223)
    print(f"PU: {pu:.2f}")
    ```

**4. % do DI**

* **Conceito:** Títulos que remuneram o investidor com um percentual da taxa DI. [cite: 203, 204]

* **Fórmulas:**

    * Taxa diária:
    
    $=(1+Taxa~Anual\%)^{\frac{1}{252}}-1$
    
    * Capitalização diária:
    
    $Capitalização~diária = DI~diario * \% do ~DI$
    
    * Valor Nominal diário:
    
    $VN~de~hoje = VN~de~ontem * (1 + Cap. Diária)$ [cite: 209, 210, 211, 212]
* **Funções Python:**

    ```python
    def taxa_diaria(taxa_anual):
        """
        Calcula a taxa diária equivalente à taxa anual.
    
        Args:
            taxa_anual (float): Taxa anual (em %).
    
        Returns:
            float: Taxa diária (em %).
        """
        taxa_decimal = taxa_anual / 100
        taxa_diaria = (1 + taxa_decimal) ** (1 / 252) - 1
        return taxa_diaria * 100
    
    def valor_nominal_cdi(valor_nominal_anterior, taxa_diaria, percentual_di):
        """
        Calcula o valor nominal atualizado de um título que rende % do DI.
    
        Args:
            valor_nominal_anterior (float): Valor nominal do dia anterior.
            taxa_diaria (float): Taxa DI diária (em %).
            percentual_di (float): Percentual do DI que o título paga (ex: 120).
    
        Returns:
            float: Valor nominal atualizado.
        """
        capitalizacao_diaria = (taxa_diaria / 100) * (percentual_di / 100)
        valor_nominal_hoje = valor_nominal_anterior * (1 + capitalizacao_diaria)
        return valor_nominal_hoje
    
    # Exemplo de uso:
    taxa_anual_di = 13.15
    taxa_diaria_calculada = taxa_diaria(taxa_anual_di)
    print(f"Taxa DI diária: {taxa_diaria_calculada:.5f}%")
    
    valor_nominal = 1000
    percentual = 120
    for _ in range(10):  # Calcula para 10 dias
        valor_nominal = valor_nominal_cdi(valor_nominal, taxa_diaria_calculada, percentual)
    print(f"Valor nominal após 10 dias: {valor_nominal:.2f}")
    ```

**5. DI + Taxa Pré**

* **Conceito:** Títulos que remuneram o investidor com a variação do DI mais uma taxa prefixada. [cite: 216, 217]

* **Fórmula:**

    * Valor Nominal Atualizado:
    
    $VN_{t}=VN_{t-1}*(1+Taxa~Pre~a.a.)^{\frac{n}{252}}*(1+Taxa~Pos~a.a.)^{\frac{n}{252}}$
    
    * Onde:
    
        * $VN_t$ = Valor Nominal no período t
        * $Taxa~Pre~a.a.$ = Taxa pré-fixada anual
        * $Taxa~Pos~a.a.$ = Taxa pós-fixada anual (DI)
        * $n$ = Número de dias do período [cite: 217]
* **Funções Python:**

    ```python
    def valor_nominal_di_prefixado(valor_nominal_anterior, taxa_pre, taxa_pos, dias):
        """
        Calcula o valor nominal atualizado de um título que rende DI + taxa pré.
    
        Args:
            valor_nominal_anterior (float): Valor nominal do dia anterior.
            taxa_pre (float): Taxa pré-fixada anual (em %).
            taxa_pos (float): Taxa pós-fixada anual (DI) (em %).
            dias (int): Número de dias do período.
    
        Returns:
            float: Valor nominal atualizado.
        """
        taxa_pre_decimal = taxa_pre / 100
        taxa_pos_decimal = taxa_pos / 100
        valor_nominal_atual = valor_nominal_anterior * (1 + taxa_pre_decimal) ** (dias / 252) * (
            1 + taxa_pos_decimal) ** (dias / 252)
        return valor_nominal_atual
    
    # Exemplo de uso:
    valor_nominal_inicial = 1000
    taxa_pre_fixada = 2
    taxa_diaria = 12.65
    valor_nominal_final = valor_nominal_di_prefixado(valor_nominal_inicial, taxa_pre_fixada, taxa_diaria, 10)
    print(f"Valor nominal após 10 dias: {valor_nominal_final:.2f}")
    
    
    ```

**6. Duration**

* **Conceito:** Mede a sensibilidade do preço de um título a mudanças nas taxas de juros. [cite: 290, 291]

* **Fórmula:**

    $Duration = \frac{\sum_{t=1}^{N} t \cdot \frac{CF_t}{(1 + i)^t}}{\sum_{t=1}^{N} \frac{CF_t}{(1 + i)^t}}$
    
    * Onde:
    
        * N = número de períodos até o vencimento.
        * CFt = é o fluxo de caixa no período t.
        * ti = é o prazo até o recebimento do fluxo
        * i = é a taxa de desconto. [cite: 294, 295, 296]
* **Função Python:**

    ```python
    def calcular_duration(fluxos_de_caixa, taxas_de_juros):
        """
        Calcula a Duration de um título de renda fixa.
    
        Args:
            fluxos_de_caixa (list): Lista de tuplas, onde cada tupla contém o período
                                  e o fluxo de caixa correspondente (ex: [(1, 100), (2, 100), (3, 1100)]).
            taxas_de_juros (float): A taxa de juros utilizada para descontar os fluxos de caixa.
    
        Returns:
            float: A Duration do título.
        """
    
        numerador = sum(t * (CFt / (1 + taxas_de_juros) ** t) for t, CFt in fluxos_de_caixa)
        denominador = sum(CFt / (1 + taxas_de_juros) ** t for t, CFt in fluxos_de_caixa)
    
        return numerador / denominador if denominador else 0
    
    # Exemplo de uso:
    fluxos_de_caixa_exemplo = [(1, 40), (2, 40), (3, 1040)]  # Período, Fluxo de Caixa
    taxa_de_juros_exemplo = 0.04  # 4%
    
    duration_exemplo = calcular_duration(fluxos_de_caixa_exemplo, taxa_de_juros_exemplo)
    print(f"A Duration do título é aproximadamente: {duration_exemplo:.2f}")
    
    ```

**7. Convexidade**

* **Conceito:** Medida da curvatura da relação entre o preço do título e as taxas de juros. [cite: 316, 317, 318]

* **Fórmula:**

    $Convexidade = \frac{V_+ + V_- - 2V_0}{2V_0(\Delta y)^2}$
    
    * Onde:
    
        * V+ = Preço quando os juros caem y%
        * V- = Preço quando os juros sobem y%
        * V₀ = Preço Inicial
        * Δy = variação das taxas de juros
    * Variação do preço do título dado a convexidade:
    
    $Variação~no~preço~do~Título = -Duration(Δy) + 0,5 * Convexidade(Δy)^2$ [cite: 317, 318]
* **Função Python:**

    ```python
    def calcular_convexidade(preco_aumento, preco_queda, preco_inicial, variacao_taxa):
        """
        Calcula a convexidade de um título de renda fixa.
    
        Args:
            preco_aumento (float): Preço do título quando a taxa de juros aumenta.
            preco_queda (float): Preço do título quando a taxa de juros diminui.
            preco_inicial (float): Preço inicial do título.
            variacao_taxa (float): Variação na taxa de juros (em decimal, ex: 0.01 para 1%).
    
        Returns:
            float: A convexidade do título.
        """
        convexidade = (preco_aumento + preco_queda - 2 * preco_inicial) / (2 * preco_inicial * (variacao_taxa ** 2))
        return convexidade
    
    def variacao_preco_com_convexidade(duration, convexidade, variacao_taxa):
        """
        Estima a variação no preço de um título usando Duration e Convexidade.
    
        Args:
            duration (float): Duration do título.
            convexidade (float): Convexidade do título.
            variacao_taxa (float): Variação na taxa de juros (em decimal, ex: 0.01 para 1%).
    
        Returns:
            float: A variação percentual estimada no preço do título.
        """
        variacao_preco = -duration * variacao_taxa + 0.5 * convexidade * (variacao_taxa ** 2)
        return variacao_preco
    
    # Exemplo de uso:
    preco_aumento_exemplo = 1050  # Preço quando a taxa de juros aumenta
    preco_queda_exemplo = 950    # Preço quando a taxa de juros diminui
    preco_inicial_exemplo = 1000  # Preço inicial do título
    variacao_taxa_exemplo = 0.01  # Variação de 1% (0.01 em decimal)
    duration_exemplo = 5  # Duration do título (exemplo)
    
    convexidade_calculada = calcular_convexidade(preco_aumento_exemplo, preco_queda_exemplo, preco_inicial_exemplo, variacao_taxa_exemplo)
    print(f"A convexidade do título é: {convexidade_calculada:.4f}")
    
    variacao_preco_estimada = variacao_preco_com_convexidade(duration_exemplo, convexidade_calculada, variacao_taxa_exemplo)
    print(f"Variação percentual estimada no preço: {variacao_preco_estimada:.4f}")
    
    ```

Este conjunto de funções cobre as principais fórmulas financeiras da apostila. Com elas, você pode construir uma biblioteca robusta para análise de renda fixa em Python.