import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card


st.title("Cestinhas")
st.divider()


st.title("Líderes de Assistências por Time")
st.divider()
@st.cache_data  
def load_data():
    return pd.read_csv("dados/2023-2024_NBA_Player_Stats_Regular.csv", sep=";",encoding='iso-8859-1')
data = load_data()
data = data[['Player', 'Tm', 'AST']]
leaders = data.loc[data.groupby('Tm')['AST'].idxmax()]
leaders = leaders.sort_values(by='AST', ascending=False)
st.dataframe(leaders[['Player', 'Tm', 'AST']].reset_index(drop=True))















#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()
