import streamlit as st

st.set_page_config(
    page_title="Demo Arquitetura – Execução sem VM",
    layout="centered"
)

# Estado inicial
if "logado" not in st.session_state:
    st.session_state.logado = False

# Esconde sidebar antes do login
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

st.title("Acesso ao Processo Automatizado")

st.caption(
    "Demonstração de execução de processo **sem dependência de máquina virtual**"
)

usuario = st.text_input("Usuário corporativo")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario == "admin" and senha == "123":
        st.session_state.logado = True
        st.success("Autenticação validada")
        st.rerun()
    else:
        st.error("Credenciais inválidas")
