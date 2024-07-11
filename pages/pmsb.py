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
   col_tab[0].write("Tabela 5-2 [item 01](https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-2/relatorio_p809.pdf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0yL3JlbGF0b3Jpb19wODA5LnBkZiIsImlhdCI6MTcyMDIwNjc4MiwiZXhwIjoxNzIwODExNTgyfQ.DFMnAMcxIZfkYskKbAf5NQn2UHCmfVYXm5LajvcGqg8&t=2024-07-05T19%3A13%3A02.773Z)")      
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



    
   col_tab[0].write("5.2.2. Esgotamento Sanitário ...827")
   col_tab[0].write("Tabela 5-8 [item 1 e 2]")
   col_tab[0].write("Tabela 5-8 [item 3 a 5]")
   col_tab[0].write("Tabela 5-8 [item 6 a 8]")
   col_tab[0].write("Tabela 5-8 [item 9 a 12]]")
    
   col_tab[1].write("Tabela 5-9 [item 1 e 2]") 
   col_tab[1].write("Tabela 5-9 [item 3]") 

   col_tab[2].write("Tabela 5-10 [item 1 e 2]")

   col_tab[3].write("Tabela 5-11 [item 1 e 2]")
   col_tab[3].write("Tabela 5-11 [item 3 e 4]")
   col_tab[3].write("Tabela 5-11 [item 5 e 6]")
   col_tab[3].write("Tabela 5-11 [item 7]")

   col_tab[4].write("Tabela 5-12 [item 1 e 2]")
   col_tab[4].write("Tabela 5-13 [item 1]") 

    

   col_tab[0].write("5.2.3. Limpeza pública e Manejo de Resíduos Sólidos..842")

   col_tab[0].write("5.2.4. Drenagem Urbana e Manejo de Águas Pluviais ..899")
 


if lider==False and equipe==False and tabelas==False:            
   plano()
   
