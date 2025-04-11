import streamlit as st


st.title("Juntando Coursera com Desafio da pós")

st.write(
    
    '''
    ## Atividades
    1) Pesquisar e criar no Python uma lista de sites para a coleta destes
    indicadores. (Célula de Texto)
    OBS.: com minhas sugestões ou outros de sua preferência.
    2) Criar um código Python que interaja com o usuário coletando os valores
    dos índices indicados neste documento. Devem ser salvos em uma lista
    e exibidos no final para verificação.

    - Model Evaluation and Refinement
    
    '''
 
)

indicesFinanceiros = {
    "CDI": "https://www.bcb.gov.br/htms/SELIC/SELICdiarios.asp?frame=1",
    "Taxa Selic": "https://www.bcb.gov.br/",
    "IPCA": "https://www.bcb.gov.br/",
    "IFIX": "https://br.investing.com/indices/bm-fbovespa-real-estate-ifix",
    "IBOV": "https://br.investing.com/indices/bovespa",
    "S&P500": "https://br.investing.com/indices/us-spx-500",
    "Nasdaq": "https://br.investing.com/indices/nasdaq-composite",
    "Nasdaq-100": "https://br.investing.com/indices/nq-100"
}


# Input de número
#idade = st.number_input("Digite sua idade:", min_value=0, max_value=120)

# Caixa de seleção
indiceSelect = st.selectbox("O índice a ser coletado:", list(indicesFinanceiros.keys()))

# Slider
#nota = st.slider("Dê uma nota para o nosso app:", 0, 10, 5)

# Checkbox
aceita = st.checkbox("Aceita os termos e condições?")

# Botão para processar os dados
if st.button("Enviar"):
    if aceita:
        st.success(f"O índice selecionado foi {indiceSelect}.")
        st.write(f"Link para coleta: {indicesFinanceiros[indiceSelect]}")
        st.write(f"Abaixo estão os índices financeiros disponíveis: {indicesFinanceiros.keys()}")    
    else:
        st.warning("Você precisa aceitar os termos e condições para prosseguir.")



def interest_rate(face_value, present_value, time):
    FV = face_value
    PV = present_value
    T = time
    r = (FV / PV) ** (1 / T) - 1
    return r/100

def present_value(face_value, interest_rate, time):
    FV = face_value
    r = interest_rate
    T = time
    PV = FV / (1 + r/100) ** T
    return PV

def face_value(present_value, interest_rate, time):
    PV = present_value
    r = interest_rate
    T = time
    FV = PV * (1 + r/100) ** T
    return FV
