import streamlit as st
import time
import random

# Proteção
if not st.session_state.get("logado", False):
    st.switch_page("main.py")

st.title("Resultado da Execução")

if "processo" not in st.session_state:
    st.info("Execute um processo na Tela 1 antes")
    st.stop()

processo = st.session_state.processo

st.subheader("Resumo do Processo")
st.write(f"**Tipo:** {processo['tipo']}")
st.write(f"**Origem:** {processo['origem']}")
st.write(f"**Registros:** {processo['volume']}")

st.divider()

st.subheader("Execução")

with st.spinner("Processando dados..."):
    time.sleep(2)

tempo_execucao = round(random.uniform(1.5, 3.5), 2)

st.success("Processo concluído com sucesso")

st.metric("Tempo de execução (s)", tempo_execucao)
st.metric("Registros processados", processo["volume"])

st.divider()

st.subheader("Arquitetura Utilizada")

st.markdown(
    """
    ✅ Execução baseada em evento  
    ✅ Sem sessão gráfica  
    ✅ Sem usuário logado em SO  
    ✅ **Nenhuma máquina virtual dedicada**
    """
)

st.warning(
    "Este processo poderia ser orquestrado pelo Power Automate Cloud via HTTP, "
    "mantendo o PAD apenas para exceções técnicas."
)
