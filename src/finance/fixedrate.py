# Escopo atendido: Renda fixa - Mercado de capitais
# 1) COlocar todas as formulas/funções ensinadas nos módulos ensinados 
#    Criar uma função para cada uma das fórmulas; Criar módulos para funções ensinadas; Usar banco de dados paraguardar índices financeiros. Todos devem ser como MVP, ou seja, não precisa pensar muito na interface, mas sim na informação.
#    1.1) bootcamp 1, módulo 2: Mercado de capitais - renda fixa
 

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
