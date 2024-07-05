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
   st.write("
            5. PROGRAMAS, PROJETOS E AÇÕES .......................................................... 801
5.1. PROGRAMAS DE AÇÕES IMEDIATAS DO MUNICÍPIO............................801
5.2. PROGRAMAS DE AÇÕES DO PMSB.........................................................807
5.2.1. Abastecimento de Água ...........................................................................807
5.2.2. Esgotamento Sanitário .............................................................................827
5.2.3. Limpeza pública e Manejo de Resíduos Sólidos. .....................................842
5.2.3.1. Procedimentos Operacionais e Especificações Mínimas a Serem
Adotados nos Serviços de Limpeza pública e Manejo de Resíduos Sólidos.860
5.2.3.1.1. Resíduos Domésticos e Comerciais...........................................861
5.2.3.1.2. Coleta Seletiva ...........................................................................867
5.2.3.1.3. Resíduos de Limpeza Pública....................................................871
5.2.3.2. Regras para o Transporte e Outras Etapas do Gerenciamento de
Resíduos Sólidos...........................................................................................876
5.2.3.3. Definição das Responsabilidades ....................................................883
5.2.3.4. Programas e Ações de Capacitação Técnica ..................................885
5.2.3.5. Programas e Ações de Educação Ambiental...................................887
5.2.3.6. Programas e Ações para a Participação dos Grupos Interessados, em
Especial das Cooperativas e Outras Formas de Associação de Catadores de
Materiais Reutilizáveis e Recicláveis.............................................................889
5.2.3.7. Mecanismos para a Criação de Fontes de Negócios, Emprego e Renda
......................................................................................................................891
5.2.3.8. Descrição das Formas e dos Limites da Participação do Poder Público
Local na Coleta Seletiva e na Logística Reversa ..........................................893
5.2.3.9. Meios a Serem Utilizados para o Controle e a Fiscalização da
Implementação e Operacionalização dos Planos de Gerenciamento de
Resíduos Sólidos e dos Sistemas de Logística Reversa...............................896
5.2.3.10. Ações Preventivas e Corretivas .....................................................899
5.2.4. Drenagem Urbana e Manejo de Águas Pluviais .......................................899
5.2.5. Institucionalização. ...................................................................................917
5.2.6. Planilha de ações gerais do PMSB. .........................................................922
5.2.7. Procedimentos para Subsídio de Custos das Ações................................935
5.2.8. Considerações Finais das Ações .............................................................940
5.3. HIERARQUIZAÇÃO E PRIORIZAÇÃO DOS PROGRAMAS, PROJETOS E
AÇÕES ...................................................................................................................947
5.4. PLANOS DE RACIONAMENTO E ATENDIMENTO A AUMENTOS DE
DEMANDA TEMPORÁRIA.....................................................................................961
5.4.1. Diretrizes para o Plano de Segurança da Água e Plano Local de Risco ..967
5.4.2. Mapeamento de Risco..............................................................................970
5.5. REGRAS DE ATENDIMENTO E FUNCIONAMENTO OPERACIONAL PARA
SITUAÇÃO CRÍTICA NA PRESTAÇÃO DE SERVIÇOS PÚBLICOS DE
SANEAMENTO BÁSICO........................................................................................973
5.5.1. Órgãos Responsáveis pelas Ações..........................................................974
5.5.1.1. Órgãos Públicos Estaduais..............................................................974
5.5.1.2. Órgãos Públicos Municipais.............................................................974
5.5.2. Contexto Institucional das Responsabilidades .........................................976
5.6. MECANISMOS PARA EMERGÊNCIA E CONTINGÊNCIA.........................978
5.6.1. Diretrizes de Emergência e Contingência para Abastecimento de Água .982
5.6.2. Diretrizes de Emergência e Contingência para Esgotamento Sanitário ...996
5.6.3. Diretrizes de Emergência e Contingência para Limpeza pública e Manejo de
Resíduos Sólidos ................................................................................................1003
5.6.4. Diretrizes de Emergência e Contingência para Drenagem Urbana e Manejo
de Águas Pluviais................................................................................................1011
5.6.5. Síntese das Ações e Mecanismos Tarifários de Contingência...............1015
5.7. DIRETRIZES PARA A ARTICULAÇÃO COM OS PLANOS LOCAIS DE
RISCO E PARA A FORMULAÇÃO DO PLANO DE SEGURANÇA DA ÁGUA...1017
5.7.1. Objetivos da Implantação do PSA..........................................................1019
5.7.2. Implantação do PSA...............................................................................1021
5.8. DIRETRIZES PARA O PLANO MUNICIPAL DE REDUÇÃO DE RISCOS1024
5.8.1. Identificação das Áreas de Risco ...........................................................1025
5.8.2. Metodologia e Procedimentos ................................................................1028
5.9. CONSIDERAÇÕES FINAIS .......................................................................1030
")
    
if lider==False and equipe==False and reunioes==False and objetivos==False and calendario==False and conteudo==False and tabelas==False:
    plano()
   
