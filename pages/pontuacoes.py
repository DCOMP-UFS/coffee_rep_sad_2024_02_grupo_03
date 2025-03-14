import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Pontuações")
st.divider()

@st.cache_data  
def load_data():
    return pd.read_csv("dados/2023-2024_NBA_Player_Stats_Regular.csv", sep=";",encoding='iso-8859-1')
data = load_data()

st.subheader("Média de Pontos, Assistências e Rebotes por Posição")

st.markdown("##### Explicação das posições")
st.markdown("* PG (Point Guard) - armador de jogadas e pontuadores")
st.markdown("* PF (Power Forward) - defensores")
st.markdown("* SG (Shooting Guard) - grandes pontuadores e defensores")
st.markdown("* C (Center) - defensores com fortes rebotes")
st.markdown("* SF (Small Forward) - versáteis")

data_main_stats = data[['Player', "Tm", 'Pos', 'PTS', 'AST', 'TRB']]
#eliminando linhas que juntam estatísticas de times distintos Tm=TOT (Two+ Other Teams)
data_main_stats = data_main_stats[data_main_stats.Tm!="TOT"]
leaders_pts = data_main_stats.groupby('Pos')[['PTS', 'AST', 'TRB']].mean()
leaders_pts = leaders_pts.sort_values(by=['PTS', 'AST', 'TRB'], ascending=False)
leaders_pts.insert(0, "Pos", leaders_pts.index)
st.dataframe(leaders_pts[['Pos', 'PTS', 'AST', 'TRB']].reset_index(drop=True).round(2))

#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()