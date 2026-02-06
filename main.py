import streamlit as st

st.set_page_config(page_title="Demo Web", layout="centered")

st.title("Login")

if "logado" not in st.session_state:
    st.session_state.logado = False

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario == "admin" and senha == "123":
        st.session_state.logado = True
        st.success("Login realizado com sucesso")
        st.info("Acesse as telas pelo menu lateral")
    else:
        st.error("Usuário ou senha inválidos")

if not st.session_state.logado:
    st.stop()
