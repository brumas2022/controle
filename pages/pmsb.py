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
tabelas=st.sidebar.button("Tabelas")
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
if tabelas:
   #st.markdown(relatorio_p816.pdf) 
   st.markdown("5. PROGRAMAS, PROJETOS E AÇÕES .......................................................... 801")
   st.write("5.2.1. Abastecimento de Água ...........................................................................[807](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMDIwNjc4MiwiZXhwIjoxNzIwODExNTgyfQ.DFMnAMcxIZfkYskKbAf5NQn2UHCmfVYXm5LajvcGqg8&t=2024-07-05T19%3A13%3A02.773Z)")
   st.write("Tabela 5-2 [item 01](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p810.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEwLnBkZiIsImlhdCI6MTcyMDIwNzA5NSwiZXhwIjoxNzIwODExODk1fQ.el2noOaEib7glfyyRixqSuFuFcIujwDj1D_gH40Jh7M&t=2024-07-05T19%3A18%3A15.565Z)")      
   st.write("Tabela 5-2 [item 02 a 04](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p811.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODExLnBkZiIsImlhdCI6MTcyMDIwNzE2OCwiZXhwIjoxNzIwODExOTY4fQ.7oX0qP5zi-3XNSoplu9wSmSeszDuQ2bUWs6TgcJXo6c&t=2024-07-05T19%3A19%3A28.897Z)")
   st.write("Tabela 5-2 [item 05 a 08](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p811.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODExLnBkZiIsImlhdCI6MTcyMDIwNzE2OCwiZXhwIjoxNzIwODExOTY4fQ.7oX0qP5zi-3XNSoplu9wSmSeszDuQ2bUWs6TgcJXo6c&t=2024-07-05T19%3A19%3A28.897Z)") 
   st.write("Tabela 5-2 [item 09 e 10](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p812.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEyLnBkZiIsImlhdCI6MTcyMDIwNzM2NiwiZXhwIjoxNzIwODEyMTY2fQ.w5myMIMAPtsG6NTZuZfXnHEJBs_t7tmNMrurUClRjNw&t=2024-07-05T19%3A22%3A46.775Z)") 
if lider==False and equipe==False and reunioes==False and objetivos==False and calendario==False and conteudo==False and tabelas==False:
    plano()
   
