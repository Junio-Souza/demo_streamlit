import streamlit as st

st.set_page_config(page_title="Demo Web", layout="centered")

# Inicializa estado
if "logado" not in st.session_state:
    st.session_state.logado = False

# 🔒 ESCONDER MENU LATERAL ANTES DO LOGIN
if not st.session_state.logado:
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Login")

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario == "admin" and senha == "123":
        st.session_state.logado = True
        st.success("Login realizado com sucesso")
        st.info("Menu lateral liberado")
        st.rerun()
    else:
        st.error("Usuário ou senha inválidos")
