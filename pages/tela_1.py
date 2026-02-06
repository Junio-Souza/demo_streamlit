import streamlit as st

if not st.session_state.get("logado", False):
    st.warning("Faça login para acessar esta página")
    st.switch_page("main.py")

st.title("Tela 1 – Preenchimento de dados")

nome = st.text_input("Nome")
idade = st.number_input("Idade", min_value=0, max_value=120)
comentario = st.text_area("Comentário")

if st.button("Salvar dados"):
    st.session_state.dados = {
        "nome": nome,
        "idade": idade,
        "comentario": comentario
    }
    st.success("Dados salvos com sucesso")
