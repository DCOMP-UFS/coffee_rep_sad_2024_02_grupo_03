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




teams_stats = data.groupby("Tm")[["FG%", "FT%"]].mean().reset_index()

top5_fg = teams_stats.sort_values(by="FG%", ascending=False).head(5)

top5_ft = teams_stats.sort_values(by="FT%", ascending=False).head(5)


with st.expander("Top 5 Equipes em FG% (Field Goal Percentage)"):
    fig_fg, ax_fg = plt.subplots(figsize=(10, 6))
    bars_fg = ax_fg.bar(top5_fg["Tm"], top5_fg["FG%"], color='royalblue', edgecolor='black')
    ax_fg.set_title("Top 5 Equipes - FG%", fontsize=14, fontweight='bold')
    ax_fg.set_ylabel("FG%", fontsize=12)
    ax_fg.set_xlabel("Equipe", fontsize=12)
    ax_fg.set_xticklabels(top5_fg["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_fg:
        ax_fg.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                   f"{bar.get_height():.2f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_fg)

with st.expander("Top 5 Equipes em FT% (Free Throw Percentage)"):
    fig_ft, ax_ft = plt.subplots(figsize=(10, 6))
    bars_ft = ax_ft.bar(top5_ft["Tm"], top5_ft["FT%"], color='seagreen', edgecolor='black')
    ax_ft.set_title("Top 5 Equipes - FT%", fontsize=14, fontweight='bold')
    ax_ft.set_ylabel("FT%", fontsize=12)
    ax_ft.set_xlabel("Equipe", fontsize=12)
    ax_ft.set_xticklabels(top5_ft["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_ft:
        ax_ft.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                   f"{bar.get_height():.2f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_ft)


#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()