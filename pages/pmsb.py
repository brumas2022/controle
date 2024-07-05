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
tabelas=st.sidebar.button("Tabelas")
if lider:
   st.header(":green[Marcos Brumatti]", divider="orange")
   col=st.columns((1,1,1))
   col[0].image("20240416_165809.jpg")
if equipe:
   st.header(":green[Equipe PMSB]", divider="orange")
   col = st.columns((1,1,1,1))
   col[0].write(":green[Abastecimento de água]")
   col[1].write(":blue[Esgotamento sanitário]")
   col[2].write(":red[Residuos sólidos]")
   col[3].write(":orange[Drenagem urbana]") 
   col[0].write("Dalton Monteiro")
   col[0].write("Érika Carvalho")
   col[0].write("Denise Sodré")
   col[0].write("Gláucia Valadão")
   col[0].write("Fabíola Bertinetti")
   col[1].write("Vilma Mundim")
   col[1].write("João Couto")
   col[2].write("Daniel Lobo")
   col[2].write("Letícia Lazzare")
   col[2].write("Ivone")
   col[3].write("Hermes Ávila") 

if tabelas:
   #st.markdown(relatorio_p816.pdf) 
   st.markdown("5. PROGRAMAS, PROJETOS E AÇÕES .......................................................... 801")
   st.write("5.2.1. Abastecimento de Água ...........................................................................[807](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMDIwNjc4MiwiZXhwIjoxNzIwODExNTgyfQ.DFMnAMcxIZfkYskKbAf5NQn2UHCmfVYXm5LajvcGqg8&t=2024-07-05T19%3A13%3A02.773Z)")
   st.write("Tabela 5-2 [item 01](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMDIwNjc4MiwiZXhwIjoxNzIwODExNTgyfQ.DFMnAMcxIZfkYskKbAf5NQn2UHCmfVYXm5LajvcGqg8&t=2024-07-05T19%3A13%3A02.773Z)")      
   st.write("Tabela 5-2 [item 02 a 04](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p810.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEwLnBkZiIsImlhdCI6MTcyMDIwNzA5NSwiZXhwIjoxNzIwODExODk1fQ.el2noOaEib7glfyyRixqSuFuFcIujwDj1D_gH40Jh7M&t=2024-07-05T19%3A18%3A15.565Z)")
   st.write("Tabela 5-2 [item 05 a 08](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p811.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODExLnBkZiIsImlhdCI6MTcyMDIwNzE2OCwiZXhwIjoxNzIwODExOTY4fQ.7oX0qP5zi-3XNSoplu9wSmSeszDuQ2bUWs6TgcJXo6c&t=2024-07-05T19%3A19%3A28.897Z)") 
   st.write("Tabela 5-2 [item 09 e 10](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p812.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEyLnBkZiIsImlhdCI6MTcyMDIwNzM2NiwiZXhwIjoxNzIwODEyMTY2fQ.w5myMIMAPtsG6NTZuZfXnHEJBs_t7tmNMrurUClRjNw&t=2024-07-05T19%3A22%3A46.775Z)") 
   st.write("Tabela 5-2 [item 11 e 12](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p813.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEzLnBkZiIsImlhdCI6MTcyMDIwNzc4NSwiZXhwIjoxNzIwODEyNTg1fQ.evwyeOyVJfwsmz13doEJrO768tE5UTjCEJermqB-A0E&t=2024-07-05T19%3A29%3A45.605Z)") 
   st.write("Tabela 5-2 [item 13 e 14](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p814.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE0LnBkZiIsImlhdCI6MTcyMDIwNzgxOSwiZXhwIjoxNzIwODEyNjE5fQ.r4pJ4V_zI8bSbZKZulEMzmjrZ6hEWJCDBnxkERdgC7E&t=2024-07-05T19%3A30%3A19.842Z)")
   st.write("Tabela 5-2 [item 15 a 17](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p815.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE1LnBkZiIsImlhdCI6MTcyMDIwNzg0MCwiZXhwIjoxNzIwODEyNjQwfQ.LK2l60AKEZnu6yG1ZgHHp8aZLVbc0N54X5qI6KHI8dc&t=2024-07-05T19%3A30%3A41.020Z)")
   st.write("Tabela 5-2 [item 18 a 20](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p816.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE2LnBkZiIsImlhdCI6MTcyMDIwNzg2NiwiZXhwIjoxNzIwODEyNjY2fQ.FjI9jBuBYH7oxeyhefTixmVWU7nKPIrSZMY4cX8T3pE&t=2024-07-05T19%3A31%3A06.866Z)")
if lider==False and equipe==False and tabelas==False:            
   plano()
   
