import streamlit as st
st.set_page_config("PMSB", layout="wide")
lider=st.sidebar.button("Lider")
equipe=st.sidebar.button("Equipe")
reunioes=st.sidebar.button("Reunioes")
objetivos=st.sidebar.button("Objetivos")
calendario=st.sidebar.button("Calendario")
if lider:
   st.markdown("Marcos Brumatti")
   col=st.columms((1,1,1))
   col.image("20240416_165809.jpg")
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
