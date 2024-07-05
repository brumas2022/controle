import streamlit as st
import tabula
#import execjs
import pandas as pd
#from tabula.io import read_pdf
st.set_page_config("PMSB", layout="wide")
def plano():
    st.header(":green[Plano Municipal de Saneamento Basico -  SANEAR]", divider="orange")
    st.write("Aqui você terá informações sobre o Plano Municipal de Saneamento Básico do município de Rondonópolis-MT")
    st.write("[Acesse o plano aqui](https://drive.google.com/file/d/1yDofmyFtOFxvmvhrWFx-ql-Odxt5Mdho/view)")
    #st.page_link("https://drive.google.com/file/d/1yDofmyFtOFxvmvhrWFx-ql-Odxt5Mdho/view", label="Clique aqui para acessar PMSB")
    st.image("pages/plano.PNG")    
    

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
   st.markdown("Equipe PMSB")
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
   st.markdown("Tabula ainda nao deu certo")
   lista_tabelas=tabula.read_pdf("https://www.seplag.mt.gov.br/images/files/BOLETIMDEINDICADORESDEPESSOAL202210022023190437.pdf", pages="all")
   st.write(len(lista_tabelas))
elif
    plano()
   
