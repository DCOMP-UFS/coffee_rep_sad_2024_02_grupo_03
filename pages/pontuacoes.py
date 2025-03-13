import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Pontuações")
st.divider()

st.header("Líderes de rebotes em cada time")
df = pd.read_csv("./dados/2023-2024_NBA_Player_Stats_Regular.csv", delimiter=';', encoding="ISO-8859-1")

lider_rebotes_por_time = df.loc[df.groupby('TRB')['Tm'].idxmax()]
lider_rebotes_por_time_ordenado = lider_rebotes_por_time.sort_values(by="TRB",ascending=False)
filter_df = dataframe_explorer(lider_rebotes_por_time_ordenado)
st.dataframe(filter_df[['Player','Tm','ORB','DRB','TRB']])



#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()