import streamlit as st
from src.finance import fixedrate as fr


# Planejamento do App
# 1) COlocar todas as formulas ensinadas no módulo 1
    # 1.1) Criar uma função para cada uma das fórmulas
    # 1.2) Criar uma função para cada um dos índices financeiros
    # 1.3) Usar banco de dados paraguardar índices financeiros
# 2) Exercitar as orientações de linguagem de programação
# 3) Disponibilizar Bibliotecas para uso no projeto final
# 4) Criar um projeto final com o streamlit



st.title("Crystall Ball - Que investimento dará maior resultado?")



st.write(
    
    '''
    ## 1. Renda Fixa:
    ### 1.1. Títulos Prefixados (Bullet)
    #### 1.1.1. Cálculo da Taxa Efetiva Anual
    A taxa efetiva anual é a taxa de retorno que um investidor pode esperar ao manter um título prefixado até o vencimento. Ela é calculada com base no valor nominal do título, no preço unitário e no número de dias úteis até o vencimento.
    '''
 
)

# Cálculo da taxa efetiva anual
valor_nominal   = st.number_input("Valor nominal:", min_value=0.0)
preco_unitario  = st.number_input("Preço Unitário:", min_value=0.0)
dias_uteis      = st.number_input("Dias úteis até o vencimento:", min_value=0)

if st.button("Calcular Valor Nominal"):
    taxa = fr.taxa_efetiva_anual(valor_nominal, preco_unitario, dias_uteis)
    st.success(f"A taxa efetiva anual é: {taxa:.2f}%")    



# Campos de cálculo de preço unitario

st.write(
    
    '''
    #### 1.1.1. Cálculo do Preço Unitário
    O preço unitário é o valor que um investidor paga por um título prefixado. Ele é calculado com base no valor nominal do título, na taxa efetiva anual e no número de dias úteis até o vencimento.
    A fórmula para calcular o preço unitário é a seguinte:
    $PU=\frac{VN}{[\frac{Taxa}{100}+1]^{\frac{du}{252}}}$
    '''
 
)

valor_nominal   = st.number_input("Valor nominal:", min_value=0.0)
taxa_anual      = st.number_input("Taxa Anual:", min_value=0.0)
dias_uteis      = st.number_input("Dias úteis até o vencimento:", min_value=0)

if st.button("Calcular Preço Unitário"):
    pu = fr.preco_unitario(valor_nominal, taxa_anual, dias_uteis)
    st.success(f"O preço unitário é : {pu:.2f}")    





st.write(
    
    '''
    ## Próximas funcionalidades:\n
    I. Cálculo da taxas, retornos e preços unitários de títulos prefixados\n
    II. Cálculo da taxa de retorno de títulos pós-fixados\n
    III. Webscrapping de índices financeiros\n
        1) Pesquisar e criar no Python uma lista de sites para a coleta destes\n
        indicadores. (Célula de Texto)\n
        OBS.: com minhas sugestões ou outros de sua preferência.\n
        2) Criar um código Python que interaja com o usuário coletando os valores\n
        dos índices indicados neste documento. Devem ser salvos em uma lista\n
            e exibidos no final para verificação.\n
        
    '''
 
)
