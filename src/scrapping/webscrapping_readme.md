
# Còdigo para reaproveitar:


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


# Caixa de seleção
indiceSelect = st.selectbox("O índice a ser coletado:", list(indicesFinanceiros.keys()))

# Botão para processar os dados
if st.button("Enviar"):
    st.success(f"O índice selecionado foi {indiceSelect}.")
    st.write(f"Link para coleta: {indicesFinanceiros[indiceSelect]}")
    st.write(f"Índices financeiros disponíveis: {list(indicesFinanceiros.keys())}")