import streamlit as st
from st_pages import show_pages_from_config, add_page_title

st.set_page_config("Procedimentos", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
if lider:
   st.header(":green[Maria da Conceição Gois]", divider="orange")
   col = st.columns((1,1,1))
   col[0].image("conceicao.PNG")
if equipe:
   st.markdown("Equipe")
   st.image("equipe_png.png")
if reunioes:
   st.markdown("Aqui teremos as reunioes realizadas")
if objetivos:
   st.markdown("Este espaço pode ser ocupado com diversas coisas")
