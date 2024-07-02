import streamlit as st
st.set_page_config("Projeto Modernização", layout="wide")
st.header(":green[Projeto Modernização - SANEAR]", divider="orange")
st.markdown("Projeto que visa atualizar e sistematizar o PMSB, alem de melhorar os procedimentos e o regulamentp")
st.image("doris.PNG")
consultora=st.sidebar.button("CONSULTORA")
if consultora:
    st.sidebar.write("DORIS GARISTO LINS")

