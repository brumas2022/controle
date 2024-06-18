import streamlit as st
st.set_page_config("Regulamento", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
if lider:
   st.markdown("Simone Cavalcanti / Daniel Lobo")
   
   st.image("simone.PNG")
if equipe:
   st.markdown("Equipe")
   st.image("equipe_png.png")
