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
   st.header(":green[Equipe Procedimentos]", divider="orange")
   col = st.columns((1,1,1))
   col[0].write(":green[Sistema de Abastecimento de Água - Operação]")
   col[1].write(":blue[Sistema de Esgotamento sanitário - Operação]")
   col[2].write(":red[Sistema Comercial/Frotas/Almoxarifado]")
   col[0].write("Yara")
   col[0].write("Érika Carvalho")
   col[0].write("Jane Sizenandes")
   col[0].write("Herotsan")
   col[1].write("Samara")
   col[1].write("Ellen")
   col[1].write("Denise Sodré")
   col[1].write("Neire")
   col[1].write("Alberto")
   col[2].write("Simone Cavalcante")
   col[2].write("Carlos")
   col[2].write("Thiago")
   col[2].write("Salete")
   col[2].write("Alisson")
   
if reunioes:
   st.markdown("Aqui teremos as reunioes realizadas")
if objetivos:
   st.markdown("Este espaço pode ser ocupado com diversas coisas")
