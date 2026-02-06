import streamlit as st

st.title("Tela 2 – Resultado")

# Proteção
if "logado" not in st.session_state or not st.session_state.logado:
    st.warning("Acesso não autorizado")
    st.stop()

if "dados" not in st.session_state:
    st.info("Nenhum dado preenchido ainda")
    st.stop()

dados = st.session_state.dados

st.subheader("Resumo dos dados informados")

st.write(f"**Nome:** {dados['nome']}")
st.write(f"**Idade:** {dados['idade']}")
st.write(f"**Comentário:** {dados['comentario']}")

st.success("Fluxo concluído com sucesso")
