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
    ## Funções de Renda Fixa:
    '''
 
)



valor_nominal   = st.number_input("Valor nominal:", min_value=0.0)
preco_unitario  = st.number_input("Preço Unitário:", min_value=0.0)
dias_uteis      = st.number_input("Dias úteis até o vencimento:", min_value=0)

# Cálculo da taxa efetiva anual
if st.button("Calcular Taxa Efetiva Anual"):
    taxa = fr.taxa_efetiva_anual(valor_nominal, preco_unitario, dias_uteis)
    st.success(f"A taxa efetiva anual é: {taxa:.2f}%")    


st.write(
    
    '''
    ## Próximas funcionalidades:
    # 1. Cálculo da taxas, retornos e preços unitários de títulos prefixados
    # 2. Cálculo da taxa de retorno de títulos pós-fixados 
    # 3. Webscrapping de índices financeiros
    1) Pesquisar e criar no Python uma lista de sites para a coleta destes
    indicadores. (Célula de Texto)
    OBS.: com minhas sugestões ou outros de sua preferência.
    2) Criar um código Python que interaja com o usuário coletando os valores
    dos índices indicados neste documento. Devem ser salvos em uma lista
        e exibidos no final para verificação.
    
    '''
 
)
