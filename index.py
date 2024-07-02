import streamlit as st
st.set_page_config("Projeto Modernização", layout="wide")
st.header(":green[Sebo do Marcão]", divider="orange")
st.markdown("Aqui será possivel encontrar coisas com nexo e também totalmente sem nexo :musical_note:")
st.image("doris.PNG")
consultora=st.sidebar.button("CONSULTORA")
if consultora:
    st.write("Aqui teremos a foto da consultora")

