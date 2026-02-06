import streamlit as st

# Proteção
if not st.session_state.get("logado", False):
    st.switch_page("main.py")

st.title("Simulação de Processo Corporativo")

st.markdown(
    """
    Este processo **normalmente seria executado em uma VM com Power Automate Desktop**.
    
    Aqui ele é executado **sem interface gráfica**, baseado apenas em dados.
    """
)

tipo_processo = st.selectbox(
    "Tipo de processo",
    ["Atualização cadastral", "Processamento de arquivos", "Integração de dados"]
)

origem = st.selectbox(
    "Origem dos dados",
    ["API", "SharePoint", "Banco de Dados", "Arquivo CSV"]
)

volume = st.number_input(
    "Quantidade de registros",
    min_value=1,
    max_value=100000,
    value=1000
)

if st.button("Executar processo"):
    st.session_state.processo = {
        "tipo": tipo_processo,
        "origem": origem,
        "volume": volume
    }
    st.success("Processo enviado para execução")
