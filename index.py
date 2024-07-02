import streamlit as st
st.set_page_config("Projeto Modernização", layout="wide")
st.markdown("*****PROJETO MODERNIZAÇÃO - SANEAR*****")
st.write("---")
st.image("doris.PNG")
consultora=st.sidebar.button("CONSULTORA")
if consultora:
    st.write("Aqui teremos a foto da consultora")

