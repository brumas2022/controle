import streamlit as st
st.set_page_config("PMSB", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
if lider:
   st.markdown("Marcos Brumatti")
   st.image("flocos.jpg")
if equipe:
   st.markdown("Equipe")
   st.image("equipe_png.png")
