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
   
   st.markdown("5. PROGRAMAS, PROJETOS E AÇÕES...801")
   tab1, tab2, tab3, tab4 = st.tabs(["**Abastecimento de Água", "**Esgotamento Sanitário", "Resíduos Sólidos", "Drenagem Urbana"])
   with tab1:
       col_tab=st.columns((1,1,1,1,1))
       col_tab[0].link_button("Tabela 5-2 item 01", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMTk5ODAyMSwiZXhwIjoxNzUzNTM0MDIxfQ.KeBfSdiJ2rCWzAJI5HCnqL5UwkiXcngoAynhaUZGfaY&t=2024-07-26T12%3A47%3A01.621Z")      
       col_tab[0].link_button("Tabela 5-2 item 02 a 04", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p810.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEwLnBkZiIsImlhdCI6MTcyMjAwMTM5OCwiZXhwIjoxNzUzNTM3Mzk4fQ.MKpKAvutpXEJg4oJ58pKyyrh7anPv06atnTbtW0jI_M&t=2024-07-26T13%3A43%3A18.393Z")
       col_tab[0].link_button("Tabela 5-2 item 05 a 08", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p811.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODExLnBkZiIsImlhdCI6MTcyMjAwMTUzMiwiZXhwIjoxNzUzNTM3NTMyfQ.klJPm9mVZfMDQX3NUM1syc17RDCywKDj7ZFvTY6MbHg&t=2024-07-26T13%3A45%3A33.053Z")
       col_tab[0].link_button("Tabela 5-2 item 09 e 10", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p812.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEyLnBkZiIsImlhdCI6MTcyMjAwMTYwNywiZXhwIjoxNzUzNTM3NjA3fQ.LY_ztXPg5RZFs5DuEzDYyJ2DrJoRkO5CLw7Ua1kzzL0&t=2024-07-26T13%3A46%3A48.151Z")
       col_tab[0].link_button("Tabela 5-2 item 11 e 12", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p813.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEzLnBkZiIsImlhdCI6MTcyMjAwMTc0NywiZXhwIjoxNzUzNTM3NzQ3fQ.wVBUIVGDmp87SAK1KJ19KlR_25uTV5DJ0ulN9aWtAZE&t=2024-07-26T13%3A49%3A08.111Z")
       col_tab[0].link_button("Tabela 5-2 item 13 e 14", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p814.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE0LnBkZiIsImlhdCI6MTcyMjAwMTc3NiwiZXhwIjoxNzUzNTM3Nzc2fQ.rckDaHPQST8sZlCd_yuouEdzQrJobMkes2pGEJD3p9Q&t=2024-07-26T13%3A49%3A36.382Z")
       col_tab[0].link_button("Tabela 5-2 item 15 a 17", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p815.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE1LnBkZiIsImlhdCI6MTcyMjAwMTg1MywiZXhwIjoxNzUzNTM3ODUzfQ.Of76X_6dlxWnwY-Klxp5scrpx2vI0LyLCKib6NXjCFI&t=2024-07-26T13%3A50%3A53.480Z")
       col_tab[0].link_button("Tabela 5-2 item 18 a 20", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p816.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE2LnBkZiIsImlhdCI6MTcyMjAwMTg3NCwiZXhwIjoxNzUzNTM3ODc0fQ._q_GNacLbhtH4E0vNSri__XWPCrovJUYP5dg02kDeAg&t=2024-07-26T13%3A51%3A14.818Z")

       col_tab[1].link_button("Tabela 5-3 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p817.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE3LnBkZiIsImlhdCI6MTcyMjAxNTYyMSwiZXhwIjoxNzUzNTUxNjIxfQ.gDYkSDsHcEqoCCeoyD4eioqgdLJyfNXLJk6-4srKt0s&t=2024-07-26T17%3A40%3A21.665Z")
       col_tab[1].link_button("Tabela 5-3 item 3 a 5", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p818.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE4LnBkZiIsImlhdCI6MTcyMjAxNTY2MywiZXhwIjoxNzUzNTUxNjYzfQ.9JKVuYH8vyQ32Tn3UEKxqH8zyE_Ao1Ar3Ka7abyNSOA&t=2024-07-26T17%3A41%3A03.948Z")
       col_tab[1].link_button("Tabela 5-3 item 6 e 7", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p819.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE5LnBkZiIsImlhdCI6MTcyMjAxNTY5OSwiZXhwIjoxNzUzNTUxNjk5fQ.d7GtaENiKjkZ0UePsiDgp2mS_JIEMBIstHd45WkPnNI&t=2024-07-26T17%3A41%3A39.433Z")

       col_tab[2].link_button("Tabela 5-4 item 1 a 3", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p820.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIwLnBkZiIsImlhdCI6MTcyMjAxNTc2MSwiZXhwIjoxNzUzNTUxNzYxfQ.4toUJJif25rOK38Dbpeo2h7xEUMsQe2i4xw5hF5PDh4&t=2024-07-26T17%3A42%3A41.383Z")
       col_tab[2].link_button("Tabela 5-4 item 4 e 5", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p821.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIxLnBkZiIsImlhdCI6MTcyMzEyNTUzOCwiZXhwIjoxNzU0NjYxNTM4fQ.rAsYiySE6Uorqax1pbkPBo8tqgkJfYbnAFYbrMXJlXg&t=2024-08-08T13%3A58%3A59.786Z")
       col_tab[2].link_button("Tabela 5-4 item 6 a 8", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p822.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIyLnBkZiIsImlhdCI6MTcyMjAxNTgxOCwiZXhwIjoxNzUzNTUxODE4fQ.a5tkeWsYdQx7JVr1WqpMhAHYIDdyBPsyVZSeEiJDujQ&t=2024-07-26T17%3A43%3A38.677Z")
       col_tab[2].link_button("Tabela 5-4 item 9 e 10",url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p823.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIzLnBkZiIsImlhdCI6MTcyMjAxNTg0NCwiZXhwIjoxNzUzNTUxODQ0fQ.JaxteMOq4ozTHlYnnwcM98YXQjajcGPMjUYWq68zM7I&t=2024-07-26T17%3A44%3A04.255Z")

       col_tab[3].link_button("Tabela 5-5 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-5/relatorio_p824.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS01L3JlbGF0b3Jpb19wODI0LnBkZiIsImlhdCI6MTcyMzEyNTY1MSwiZXhwIjoxNzU0NjYxNjUxfQ.zgMCYGBiVM7tkMSyGNID1FkDK481aI6uwNbumGfWhEs&t=2024-08-08T14%3A00%3A52.968Z")

       col_tab[4].link_button("Tabela 5-6 item 1", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-6/relatorio_p825.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS02L3JlbGF0b3Jpb19wODI1LnBkZiIsImlhdCI6MTcyMjAxNTkzOSwiZXhwIjoxNzUzNTUxOTM5fQ.G46HT1oiOSctSuui-6iFW7-ZevyPw7QuGdny2b4Djos&t=2024-07-26T17%3A45%3A39.961Z")



   with tab2: 
   
       col_tab1=st.columns((1,1,1,1,1)) 
       col_tab1[0].link_button("Tabela 5-8 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p829.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODI5LnBkZiIsImlhdCI6MTcyMDcyODY3NCwiZXhwIjoxNzIzMzIwNjc0fQ.5ErWVjeMmlD7XyQ57l9F6PUgGx7i9Vai2hwOtYmo-1U&t=2024-07-11T20%3A11%3A15.222Z")
       col_tab1[0].link_button("Tabela 5-8 item 3 a 5", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p830.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMwLnBkZiIsImlhdCI6MTcyMDcyODY5OCwiZXhwIjoxNzUyMjY0Njk4fQ.52h6qQRFmZv23FdZydTjQ_d6areZC8wC2szHwpLdagw&t=2024-07-11T20%3A11%3A39.871Z")
       col_tab1[0].link_button("Tabela 5-8 item 6 a 8", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p831.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMxLnBkZiIsImlhdCI6MTcyMDcyODcyMiwiZXhwIjoxNzUyMjY0NzIyfQ.Fq5oPM0-zLTdHReiHIm-go0wyYB7vFkfmYto7HtbJyw&t=2024-07-11T20%3A12%3A03.547Z")
       col_tab1[0].link_button("Tabela 5-8 item 9 a 12", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p832.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMyLnBkZiIsImlhdCI6MTcyMDcyODc1MSwiZXhwIjoxNzUyMjY0NzUxfQ.XtsEOkuwxi45QHoUjcYqC3xoPoR7gu6CRnfyWdu_tWM&t=2024-07-11T20%3A12%3A32.463Z")
    
       col_tab1[1].link_button("Tabela 5-9 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-9/relatorio_p833.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS05L3JlbGF0b3Jpb19wODMzLnBkZiIsImlhdCI6MTcyMDcyODc3MiwiZXhwIjoxNzUyMjY0NzcyfQ.Cptn-y7vq05yLx8LUbBTL-YoKY4SKEz8hWpBAiVkLMQ&t=2024-07-11T20%3A12%3A53.565Z") 
       col_tab1[1].link_button("Tabela 5-9 item 3", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-9/relatorio_p834.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS05L3JlbGF0b3Jpb19wODM0LnBkZiIsImlhdCI6MTcyMDcyODc5MSwiZXhwIjoxNzUyMjY0NzkxfQ.nXZ4eveMSw-HEUAF0bqg2ir2Nc20oto7r1sGYdBJ0yM&t=2024-07-11T20%3A13%3A12.222Z") 

       col_tab1[2].link_button("Tabela 5-10 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/relatorio_p835.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC9yZWxhdG9yaW9fcDgzNS5wZGYiLCJpYXQiOjE3MjA3Mjg4MTcsImV4cCI6MTc1MjI2NDgxN30.MbNlJdPHP_39xqEHpcWJBKUf6CAK9GXrk9qolll8RFc&t=2024-07-11T20%3A13%3A38.233Z")

       col_tab1[3].link_button("Tabela 5-11 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p836.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzNi5wZGYiLCJpYXQiOjE3MjA3Mjg4MzIsImV4cCI6MTc1MjI2NDgzMn0._TCKOAgmF8e11zfpo-KjFwQbWexo7cEvMNv2jyYxIoI&t=2024-07-11T20%3A13%3A53.399Z")
       col_tab1[3].link_button("Tabela 5-11 item 3 e 4", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p837.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzNy5wZGYiLCJpYXQiOjE3MjA3Mjg4NDQsImV4cCI6MTc1MjI2NDg0NH0.WJTHWXw2RFaUipTX9TCZAvFjt09AobT8FvJ-Ia3nLi8&t=2024-07-11T20%3A14%3A05.278Z")
       col_tab1[3].link_button("Tabela 5-11 item 5 e 6", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p838.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzOC5wZGYiLCJpYXQiOjE3MjA3Mjg4NjQsImV4cCI6MTc1MjI2NDg2NH0.g-eYs45hvogxq9dJXvpR7SCiCcXqZhwtk_7zEjFWkwI&t=2024-07-11T20%3A14%3A25.397Z")
       col_tab1[3].link_button("Tabela 5-11 item 7", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p839.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzOS5wZGYiLCJpYXQiOjE3MjA3Mjg4NzksImV4cCI6MTc1MjI2NDg3OX0.5_44SoQJslI4iENs32r571jqSmKunNoAvJt5kWsV1zs&t=2024-07-11T20%3A14%3A39.968Z")

       col_tab1[4].link_button("Tabela 5-12 item 1 e 2", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-12/relatorio_p840.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMi9yZWxhdG9yaW9fcDg0MC5wZGYiLCJpYXQiOjE3MjA3Mjg4OTcsImV4cCI6MTc1MjI2NDg5N30.LVJJCeUiUgVuHeEgwYDFNdbFeXvGi_NhzWNt-Gr8YVk&t=2024-07-11T20%3A14%3A58.665Z")
       col_tab1[4].link_button("Tabela 5-13 item 1", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-13/relatorio_p841.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMy9yZWxhdG9yaW9fcDg0MS5wZGYiLCJpYXQiOjE3MjA3Mjg5MTQsImV4cCI6MTc1MjI2NDkxNH0.N8dlzCeoBIbjVtSo9nxdHSER-OfxDfhpmnBN7KGvR0g&t=2024-07-11T20%3A15%3A14.895Z") 

    

   with tab3:
       st.write("5.2.3. Limpeza pública e Manejo de Resíduos Sólidos..842")

   with tab4:
       st.write("5.2.4. Drenagem Urbana e Manejo de Águas Pluviais ..899")
 


if lider==False and equipe==False and tabelas==False:            
   plano()
   
