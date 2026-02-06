import streamlit as st

if not st.session_state.get("logado", False):
    st.warning("Faça login para acessar esta página")
    st.switch_page("main.py")

st.title("Tela 2 – Resultado")

if "dados" not in st.session_state:
    st.info("Preencha os dados na Tela 1 antes")
    st.stop()

dados = st.session_state.dados

st.write(f"**Nome:** {dados['nome']}")
st.write(f"**Idade:** {dados['idade']}")
st.write(f"**Comentário:** {dados['comentario']}")

st.success("Fluxo concluído com sucesso")
