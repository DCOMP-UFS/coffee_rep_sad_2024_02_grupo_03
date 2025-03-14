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


# Análise da Média de Pontos das Equipes TOP 5
with st.expander("🏅📈 Média de Pontos das Equipes TOP 5"):

    # Calculando a média de pontos por equipe (TOP 5)
    md_pts_maior = data_main_stats.groupby("Tm")["PTS"].mean().sort_values(ascending=False).head(5)

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(md_pts_maior.index, md_pts_maior.values, color='royalblue', edgecolor='black')

    # Título e rótulos
    ax.set_title("Média de Pontos das Equipes TOP 5", fontsize=14, fontweight='bold')
    ax.set_xlabel("Equipes", fontsize=12)
    ax.set_ylabel("Média de Pontos", fontsize=12)
    ax.set_xticks(range(len(md_pts_maior.index)))
    ax.set_xticklabels(md_pts_maior.index, fontsize=10)

    # Adicionando os valores nas barras
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                f"{bar.get_height():.2f}",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Exibe o gráfico no Streamlit
    st.pyplot(fig)


# Análise da Média de Pontos das Equipes Menor Desempenho
with st.expander("📉🚨 Média de Pontos das 5 Equipes com Menor Desempenho"):

    # Calculando a média de pontos por equipe
    md_pts_menor = data_main_stats.groupby("Tm")["PTS"].mean().sort_values(ascending=True).head(5)

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(md_pts_menor.index, md_pts_menor.values, color='crimson', edgecolor='black')

    # Título e rótulos
    ax.set_title("Média de Pontos das 5 Equipes com Menor Desempenho", fontsize=14, fontweight='bold')
    ax.set_xlabel("Equipes", fontsize=12)
    ax.set_ylabel("Média de Pontos", fontsize=12)
    ax.set_xticks(range(len(md_pts_menor.index)))
    ax.set_xticklabels(md_pts_menor.index, fontsize=10)

    # Adicionando os valores nas barras
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                f"{bar.get_height():.2f}",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Exibe o gráfico no Streamlit
    st.pyplot(fig)



#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()