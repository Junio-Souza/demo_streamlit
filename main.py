import streamlit as st

st.set_page_config(page_title="Demo Web", layout="centered")

st.title("Login")

# Inicializa estado
if "logado" not in st.session_state:
    st.session_state.logado = False

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario == "admin" and senha == "123":
        st.session_state.logado = True
        st.success("Login realizado com sucesso")
    else:
        st.error("Usuário ou senha inválidos")

if st.session_state.logado:
    st.info("Use o menu lateral para navegar")
else:
    st.warning("Faça login para acessar as telas")
    st.stop()
