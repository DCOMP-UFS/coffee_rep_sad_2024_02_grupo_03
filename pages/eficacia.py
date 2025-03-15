import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card

st.title("Eficácia dos Times")
st.divider()

@st.cache_data  
def load_data():
    return pd.read_csv("dados/2023-2024_NBA_Player_Stats_Regular.csv", sep=";",encoding='iso-8859-1')
data = load_data()


st.subheader("Eficácia dos cinco principais jogadores")

st.markdown("* Player - nome do jogador")
st.markdown("* Age - idade do jogador")
st.markdown("* Tm (Team) - sigla do time ")
st.markdown("* FG (Field goals) - pontos através de cestas (2 ou 3 pontos) por jogo")
st.markdown("* FG% - porcentagem de acertos dos arremessos")

st.markdown("* FT (free trow) - lances livres por jogo")
st.markdown("* FT% - porcentagem de lances livres convertidos")

data_leaders_pts = data[['Player','Tm','FT', 'FG', 'FT%','FG%']]
data_leaders_pts_ordenado = data_leaders_pts[data_leaders_pts.Tm != "TOT"]
leaders_pts = data_leaders_pts.sort_values(by=['FG%','FT%'], ascending=False).head(5)
st.dataframe(leaders_pts[['Player','Tm','FT', 'FG', 'FG%','FT%']].reset_index(drop=True))






#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()