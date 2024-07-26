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
   st.write("5.2.1. Abastecimento de Água")
   col_tab=st.columns((1,1,1,1,1))
   col_tab[0].link_button("Teste", url="https://uol.com.br") 
   col_tab[0].link_button("Tabela 5-2 item 01", url="https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMDIwNjc4MiwiZXhwIjoxNzIwODExNTgyfQ.DFMnAMcxIZfkYskKbAf5NQn2UHCmfVYXm5LajvcGqg8&t=2024-07-05T19%3A13%3A02.773Z")      
   col_tab[0].write("Tabela 5-2 [item 02 a 04](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p810.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEwLnBkZiIsImlhdCI6MTcyMDIwNzA5NSwiZXhwIjoxNzIwODExODk1fQ.el2noOaEib7glfyyRixqSuFuFcIujwDj1D_gH40Jh7M&t=2024-07-05T19%3A18%3A15.565Z)")
   col_tab[0].write("Tabela 5-2 [item 05 a 08](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p811.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODExLnBkZiIsImlhdCI6MTcyMDIwNzE2OCwiZXhwIjoxNzIwODExOTY4fQ.7oX0qP5zi-3XNSoplu9wSmSeszDuQ2bUWs6TgcJXo6c&t=2024-07-05T19%3A19%3A28.897Z)") 
   col_tab[0].write("Tabela 5-2 [item 09 e 10](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p812.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEyLnBkZiIsImlhdCI6MTcyMDIwNzM2NiwiZXhwIjoxNzIwODEyMTY2fQ.w5myMIMAPtsG6NTZuZfXnHEJBs_t7tmNMrurUClRjNw&t=2024-07-05T19%3A22%3A46.775Z)") 
   col_tab[0].write("Tabela 5-2 [item 11 e 12](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p813.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODEzLnBkZiIsImlhdCI6MTcyMDIwNzc4NSwiZXhwIjoxNzIwODEyNTg1fQ.evwyeOyVJfwsmz13doEJrO768tE5UTjCEJermqB-A0E&t=2024-07-05T19%3A29%3A45.605Z)") 
   col_tab[0].write("Tabela 5-2 [item 13 e 14](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p814.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE0LnBkZiIsImlhdCI6MTcyMDIwNzgxOSwiZXhwIjoxNzIwODEyNjE5fQ.r4pJ4V_zI8bSbZKZulEMzmjrZ6hEWJCDBnxkERdgC7E&t=2024-07-05T19%3A30%3A19.842Z)")
   col_tab[0].write("Tabela 5-2 [item 15 a 17](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p815.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE1LnBkZiIsImlhdCI6MTcyMDIwNzg0MCwiZXhwIjoxNzIwODEyNjQwfQ.LK2l60AKEZnu6yG1ZgHHp8aZLVbc0N54X5qI6KHI8dc&t=2024-07-05T19%3A30%3A41.020Z)")
   col_tab[0].write("Tabela 5-2 [item 18 a 20](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p816.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODE2LnBkZiIsImlhdCI6MTcyMDIwNzg2NiwiZXhwIjoxNzIwODEyNjY2fQ.FjI9jBuBYH7oxeyhefTixmVWU7nKPIrSZMY4cX8T3pE&t=2024-07-05T19%3A31%3A06.866Z)")

   col_tab[1].write("Tabela 5-3 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p817.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE3LnBkZiIsImlhdCI6MTcyMDQ2ODEyNywiZXhwIjoxNzIxMDcyOTI3fQ.UlpPE77CZrBbh8tN_rgD07KWi4mmE4V3Oh7SWwO64pU&t=2024-07-08T19%3A48%3A47.944Z)")
   col_tab[1].write("Tabela 5-3 [item 3 a 5](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p818.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE4LnBkZiIsImlhdCI6MTcyMDQ2ODE1MSwiZXhwIjoxNzIxMDcyOTUxfQ.7ByJkIIue_GktF1Nqf3IP94dK-rKsW3U_DOa7XB0wZ8&t=2024-07-08T19%3A49%3A11.288Z)") 
   col_tab[1].write("Tabela 5-3 [item 6 e 7](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-3/relatorio_p819.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0zL3JlbGF0b3Jpb19wODE5LnBkZiIsImlhdCI6MTcyMDQ2ODE2OSwiZXhwIjoxNzIxMDcyOTY5fQ.rLTJBTEGkyFQhFRsFn88Ul-uXErBsdKgqF99Opuip1c&t=2024-07-08T19%3A49%3A29.273Z)")

   col_tab[2].write("Tabela 5-4 [item 1 a 3](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p820.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIwLnBkZiIsImlhdCI6MTcyMDQ2ODkxNSwiZXhwIjoxNzIxMDczNzE1fQ.dk9ldYKWkpebavzFT1ZryF-J06oJ8AwPqnA25oT8-Gw&t=2024-07-08T20%3A01%3A55.731Z)")
   col_tab[2].write("Tabela 5-4 [item 4 e 5](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p821.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIxLnBkZiIsImlhdCI6MTcyMDQ2ODkzNiwiZXhwIjoxNzIxMDczNzM2fQ.yhgUVDaLkN7Q2bVBFpp4goQR5XiFk9MbdJuiOv6FLtg&t=2024-07-08T20%3A02%3A16.478Z)")
   col_tab[2].write("Tabela 5-4 [item 6 a 8](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p822.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIyLnBkZiIsImlhdCI6MTcyMDQ2ODk1MSwiZXhwIjoxNzIxMDczNzUxfQ.pbUyu4Z1fxZl62ZheBDwV8DTOkO-H99Ywhowq1As-gs&t=2024-07-08T20%3A02%3A32.016Z)")
   col_tab[2].write("Tabela 5-4 [item 9 e 10](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-4/relatorio_p822.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS00L3JlbGF0b3Jpb19wODIyLnBkZiIsImlhdCI6MTcyMDQ2ODk1MSwiZXhwIjoxNzIxMDczNzUxfQ.pbUyu4Z1fxZl62ZheBDwV8DTOkO-H99Ywhowq1As-gs&t=2024-07-08T20%3A02%3A32.016Z)")                 

   col_tab[3].write("Tabela 5-5 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-5/relatorio_p824.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS01L3JlbGF0b3Jpb19wODI0LnBkZiIsImlhdCI6MTcyMDQ2OTk1MiwiZXhwIjoxNzIxMDc0NzUyfQ.2Gl5UlcniBuT8e3h8kpFetRGbjoBCiLBH8yI3nJanMI&t=2024-07-08T20%3A19%3A12.764Z)") 

   col_tab[4].write("Tabela 5-6 [item 1](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-6/relatorio_p825.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS02L3JlbGF0b3Jpb19wODI1LnBkZiIsImlhdCI6MTcyMDQ2OTk3NCwiZXhwIjoxNzIxMDc0Nzc0fQ.ksxvV8h7bdAQfg6t7MiKwUCfxEJSqfpCw23tvwhXiic&t=2024-07-08T20%3A19%3A35.081Z)")



    
   st.write("5.2.2. Esgotamento Sanitário ...827")
   col_tab1=st.columns((1,1,1,1,1)) 
   col_tab1[0].write("Tabela 5-8 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p829.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODI5LnBkZiIsImlhdCI6MTcyMDcyODY3NCwiZXhwIjoxNzIzMzIwNjc0fQ.5ErWVjeMmlD7XyQ57l9F6PUgGx7i9Vai2hwOtYmo-1U&t=2024-07-11T20%3A11%3A15.222Z)")
   col_tab1[0].write("Tabela 5-8 [item 3 a 5](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p830.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMwLnBkZiIsImlhdCI6MTcyMDcyODY5OCwiZXhwIjoxNzUyMjY0Njk4fQ.52h6qQRFmZv23FdZydTjQ_d6areZC8wC2szHwpLdagw&t=2024-07-11T20%3A11%3A39.871Z)")
   col_tab1[0].write("Tabela 5-8 [item 6 a 8](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p831.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMxLnBkZiIsImlhdCI6MTcyMDcyODcyMiwiZXhwIjoxNzUyMjY0NzIyfQ.Fq5oPM0-zLTdHReiHIm-go0wyYB7vFkfmYto7HtbJyw&t=2024-07-11T20%3A12%3A03.547Z)")
   col_tab1[0].write("Tabela 5-8 [item 9 a 12](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-8/relatorio_p832.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS04L3JlbGF0b3Jpb19wODMyLnBkZiIsImlhdCI6MTcyMDcyODc1MSwiZXhwIjoxNzUyMjY0NzUxfQ.XtsEOkuwxi45QHoUjcYqC3xoPoR7gu6CRnfyWdu_tWM&t=2024-07-11T20%3A12%3A32.463Z)")
    
   col_tab1[1].write("Tabela 5-9 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-9/relatorio_p833.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS05L3JlbGF0b3Jpb19wODMzLnBkZiIsImlhdCI6MTcyMDcyODc3MiwiZXhwIjoxNzUyMjY0NzcyfQ.Cptn-y7vq05yLx8LUbBTL-YoKY4SKEz8hWpBAiVkLMQ&t=2024-07-11T20%3A12%3A53.565Z)") 
   col_tab1[1].write("Tabela 5-9 [item 3](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-9/relatorio_p834.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS05L3JlbGF0b3Jpb19wODM0LnBkZiIsImlhdCI6MTcyMDcyODc5MSwiZXhwIjoxNzUyMjY0NzkxfQ.nXZ4eveMSw-HEUAF0bqg2ir2Nc20oto7r1sGYdBJ0yM&t=2024-07-11T20%3A13%3A12.222Z)") 

   col_tab1[2].write("Tabela 5-10 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/relatorio_p835.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC9yZWxhdG9yaW9fcDgzNS5wZGYiLCJpYXQiOjE3MjA3Mjg4MTcsImV4cCI6MTc1MjI2NDgxN30.MbNlJdPHP_39xqEHpcWJBKUf6CAK9GXrk9qolll8RFc&t=2024-07-11T20%3A13%3A38.233Z)")

   col_tab1[3].write("Tabela 5-11 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p836.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzNi5wZGYiLCJpYXQiOjE3MjA3Mjg4MzIsImV4cCI6MTc1MjI2NDgzMn0._TCKOAgmF8e11zfpo-KjFwQbWexo7cEvMNv2jyYxIoI&t=2024-07-11T20%3A13%3A53.399Z)")
   col_tab1[3].write("Tabela 5-11 [item 3 e 4](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p837.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzNy5wZGYiLCJpYXQiOjE3MjA3Mjg4NDQsImV4cCI6MTc1MjI2NDg0NH0.WJTHWXw2RFaUipTX9TCZAvFjt09AobT8FvJ-Ia3nLi8&t=2024-07-11T20%3A14%3A05.278Z)")
   col_tab1[3].write("Tabela 5-11 [item 5 e 6](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p838.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzOC5wZGYiLCJpYXQiOjE3MjA3Mjg4NjQsImV4cCI6MTc1MjI2NDg2NH0.g-eYs45hvogxq9dJXvpR7SCiCcXqZhwtk_7zEjFWkwI&t=2024-07-11T20%3A14%3A25.397Z)")
   col_tab1[3].write("Tabela 5-11 [item 7](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-11/relatorio_p839.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMS9yZWxhdG9yaW9fcDgzOS5wZGYiLCJpYXQiOjE3MjA3Mjg4NzksImV4cCI6MTc1MjI2NDg3OX0.5_44SoQJslI4iENs32r571jqSmKunNoAvJt5kWsV1zs&t=2024-07-11T20%3A14%3A39.968Z)")

   col_tab1[4].write("Tabela 5-12 [item 1 e 2](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-12/relatorio_p840.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMi9yZWxhdG9yaW9fcDg0MC5wZGYiLCJpYXQiOjE3MjA3Mjg4OTcsImV4cCI6MTc1MjI2NDg5N30.LVJJCeUiUgVuHeEgwYDFNdbFeXvGi_NhzWNt-Gr8YVk&t=2024-07-11T20%3A14%3A58.665Z)")
   col_tab1[4].write("Tabela 5-13 [item 1](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-13/relatorio_p841.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMy9yZWxhdG9yaW9fcDg0MS5wZGYiLCJpYXQiOjE3MjA3Mjg5MTQsImV4cCI6MTc1MjI2NDkxNH0.N8dlzCeoBIbjVtSo9nxdHSER-OfxDfhpmnBN7KGvR0g&t=2024-07-11T20%3A15%3A14.895Z)") 

    

   st.write("5.2.3. Limpeza pública e Manejo de Resíduos Sólidos..842")

   st.write("5.2.4. Drenagem Urbana e Manejo de Águas Pluviais ..899")
 


if lider==False and equipe==False and tabelas==False:            
   plano()
   
