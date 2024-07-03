import streamlit as st
st.set_page_config("PMSB", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
calendario=st.sidebar.button("Calendario")
conteudo=st.sidebar.button("Conteudo")
if lider:
   st.header(":green[Marcos Brumatti]", divider="orange")
   col=st.columns((1,1,1))
   col[0].image("20240416_165809.jpg")
if equipe:
   st.markdown("Equipe pmsb")
   st.image("equipe_png.png")
if reunioes:
   st.markdown("Aqui teremos as reunioes realizadas")
if objetivos:
   st.markdown("Este espaço pode ser ocupado com diversas coisas")
if calendario:
    from streamlit_calendar import calendar
    calendario=calendar()
    st.write(calendario)
if conteudo:
   st.markdown("TAbula nova tentativa")
   import tabula
   lista_tabelas=tabula.read_pdf("_Cartilha BNCC 2021.pdf", pages="all")
   st.write(len(lista_tabelas))
   
