import streamlit as st
st.set_page_config("Procedimentos", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
if lider:
   st.markdown("Maria da Conceição Gois")
   st.image("conceicao.PNG")
if equipe:
   st.markdown("Equipe")
   st.image("equipe_png.png")
