import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card


st.title("Cestinhas")
st.divider()

@st.cache_data  
def load_data():
    return pd.read_csv("dados/2023-2024_NBA_Player_Stats_Regular.csv", sep=";",encoding='iso-8859-1')
data = load_data()

st.subheader("Líderes de Pontos por Time")
data_leaders_pts = data[['Player', 'Tm', 'PTS']]
#eliminando linhas que juntam estatísticas de times distintos Tm=TOT (Two+ Other Teams)
data_leaders_pts = data_leaders_pts[data_leaders_pts.Tm!="TOT"]
leaders_pts = data_leaders_pts.loc[data_leaders_pts.groupby('Tm')['PTS'].idxmax()]
leaders_pts = leaders_pts.sort_values(by='PTS', ascending=False)
st.dataframe(leaders_pts[['Player', 'Tm', 'PTS']].reset_index(drop=True))

st.metric("Média de Pontos considerando os maiores pontuadores", round(leaders_pts.PTS.mean(), 1))

st.divider()

st.subheader("Líderes de Assistências por Time")
data_leaders = data[['Player', 'Tm', 'AST']]
#eliminando linhas que juntam estatísticas de times distintos Tm=TOT (Two+ Other Teams)
data_leaders = data_leaders[data_leaders.Tm!="TOT"]
leaders = data_leaders.loc[data_leaders.groupby('Tm')['AST'].idxmax()]
leaders = leaders.sort_values(by='AST', ascending=False)
st.dataframe(leaders[['Player', 'Tm', 'AST']].reset_index(drop=True))

st.divider()
st.subheader("Líderes de Rebotes por Time")
lider_rebotes_por_time = data.loc[data.groupby('Tm')['TRB'].idxmax()]
#eliminando linhas que juntam estatísticas de times distintos Tm=TOT (Two+ Other Teams)
lider_rebotes_por_time = lider_rebotes_por_time[lider_rebotes_por_time.Tm!="TOT"]
lider_rebotes_por_time_ordenado = lider_rebotes_por_time.sort_values(by="TRB",ascending=False)
#filter_df = dataframe_explorer(lider_rebotes_por_time_ordenado)
st.dataframe(lider_rebotes_por_time_ordenado[['Player','Tm','ORB','DRB','TRB']].reset_index(drop=True))

















#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()
