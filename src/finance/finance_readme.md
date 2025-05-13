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