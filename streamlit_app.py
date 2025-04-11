import streamlit as st


st.title("Outros métodos")

st.write(
    
    '''
    ## MODEL SELECTION

    - Model Evaluation and Refinement
    
    '''
 
)


import streamlit as st

# Título da aplicação
st.title("Formulário com Streamlit")

# Input de texto
nome = st.text_input("Digite seu nome:")

# Input de número
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120)

# Caixa de seleção
sexo = st.selectbox("Selecione seu sexo:", ["Masculino", "Feminino", "Outro"])

# Slider
nota = st.slider("Dê uma nota para o nosso app:", 0, 10, 5)

# Checkbox
aceita = st.checkbox("Aceita os termos e condições?")

# Botão para processar os dados
if st.button("Enviar"):
    if aceita:
        st.success(f"Obrigado, {nome}! Você tem {idade} anos, se identificou como {sexo}, e deu nota {nota}.")
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
