# Escopo atendido: Renda fixa - Mercado de capitais
# 1) COlocar todas as formulas/funções ensinadas nos módulos ensinados 
#    Criar uma função para cada uma das fórmulas; Criar módulos para funções ensinadas; Usar banco de dados paraguardar índices financeiros. Todos devem ser como MVP, ou seja, não precisa pensar muito na interface, mas sim na informação.
#    1.1) bootcamp 1, módulo 2: Mercado de capitais - renda fixa

import numpy as np
import pandas as pd

# 1. Prefixado (Bullet)

# Conceito: Títulos prefixados têm sua rentabilidade definida no momento da compra. O investidor recebe o valor investido mais a rentabilidade no vencimento. [cite: 102, 103, 104]
# Fórmulas:
# Cálculo da Taxa Efetiva Anual:  
#    $Taxa=([\frac{VN}{PU}]^{\frac{252}{du}}-1)x~100$
#    * Cálculo do PU (Preço Unitário):  
#    $PU=\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{du}{252}}}$    
#   Onde:
#       * $VN$ = Valor Nominal do título
#       * $PU$ = Preço Unitário do título
#       * $Taxa$ = Taxa Efetiva anual
#       * $du$ = dias úteis [cite: 106, 107]

#   Funções Python:
    
def taxa_efetiva_anual(valor_nominal, preco_unitario, dias_uteis):
    """
    Calcula a taxa efetiva anual de um título prefixado (bullet).

    Args:
        valor_nominal (float):  Valor nominal do título.
        preco_unitario (float): Preço unitário do título.
        dias_uteis (int):       Número de dias úteis até o vencimento.

    Returns:
        float: Taxa efetiva anual (em %).
    """
    taxa = ((valor_nominal / preco_unitario) ** (252 / dias_uteis) - 1) * 100
    return taxa

def preco_unitario(valor_nominal, taxa_anual, dias_uteis):
    """
    Calcula o preço unitário de um título prefixado (bullet).

    Args:
        valor_nominal (float):  Valor nominal do título.
        taxa_anual (float):     Taxa efetiva anual (em %).
        dias_uteis (int):       Número de dias úteis até o vencimento.

    Returns:
        float: Preço unitário do título.
    """
    taxa_decimal = taxa_anual / 100
    pu = valor_nominal / ((1 + taxa_decimal) ** (dias_uteis / 252))
    return pu
    
# Exemplos de uso:
#    valor_nominal = 1000
#    preco = 883
#    dias = 252
#   
#    taxa = taxa_efetiva_anual(valor_nominal, preco, dias)
#    print(f"Taxa efetiva anual: {taxa:.2f}%")  # Saída: 13.25%
#    
#    pu = preco_unitario(valor_nominal, 13.25, dias)
#    print(f"Preço unitário: {pu:.2f}")  # Saída: 883.00


#   2. Pré-fixado com Cupom**
#   Conceito: Similar ao prefixado, mas com pagamentos periódicos de juros (cupons) antes do vencimento. [cite: 115, 116, 117]
#   Fórmula:
#   Cálculo do PU:    
#   $PU=\sum_{t=1}^{T}\frac{Ct}{[\frac{Taxa}{100}+1]^{\frac{t}{252}}}+\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{T}{252}}}$   
#   Conversão da Taxa:
#   De Taxa periodom para taxa periodo₁ $=(1+i\%)^{\frac{n}{m}}-1$
#   Onde:
#        * $PU$ = Preço unitário do ativo.
#        * $VN$ = Valor Nominal do título.
#        * $Ct$ = Pagamento de principal, cupom ou ambos no período t
#        * $t$ = cada um dos períodos (anual, semestral ou outro) para cada pagamento.
#        * $T$ = Quantidade de Períodos até o último vencimento.
#        * Taxa = Taxa de retorno do Título até o vencimento
#        * $d.u.$ = dias úteis
#        * $i$ = Taxa de Juros em um determinado período (ex. ano)
#        * $m$ = Número de dias referente aos juros (exemplo 252)
#        * $n$ = Número de dias referente ao período que se deseja calcular a taxa (exemplo semestre ou 126 dias) [cite: 119, 120, 121, 122, 126]
#   Funções Python:**
    
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
        valor_nominal (float):      Valor nominal do título.
        taxa_anual (float):         Taxa de retorno anual do título (em %).
        cupons (list):              Lista com os valores dos cupons.
        datas_cupons (list):        Lista com as datas de pagamento dos cupons.
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
#    valor_nominal = 1000
#    taxa_anual = 11
#    cupons = [48.80885, 48.80885, 1048.80885]  # Cupons e valor nominal no vencimento
#    datas_cupons = ['2024-01-02', '2024-07-01', '2025-01-02']
#    data_vencimento = pd.to_datetime('2025-01-02')
#    
#    pu_com_cupom = preco_unitario_cupom(valor_nominal, taxa_anual, cupons, datas_cupons, data_vencimento)
#    print(f"Preço unitário com cupons: {pu_com_cupom:.2f}")
#    
#    taxa_semestral = taxa_periodo(10, 252, 126)
#    print(f"Taxa semestral: {taxa_semestral:.2f}%")