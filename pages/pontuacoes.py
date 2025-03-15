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

data_main_stats = data[['Player', "Tm", 'Pos', 'PTS', 'AST', 'TRB', 'FT', 'FTA']]
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

    # Exibe o gráfico
    st.pyplot(fig)
# Análise da Média de FTA e Pontos Feitos a Partir de FT por Equipe
with st.expander("📊 Média de Lances e Pontos Feitos por Lances Livres das Equipes"):

    # Calculando a média de FTA e FT por equipe
    md_fta_ft_equipes = data_main_stats.groupby("Tm")[["FTA", "FT"]].mean().sort_values(by="FTA", ascending=False).reset_index()

    # Renomeando as colunas
    md_fta_ft_equipes = md_fta_ft_equipes.rename(columns={
        "Tm": "Equipe",
        "FTA": "Média de Lances Livres - FTA",
        "FT": "Média de  Pontos Feitos por Lances Livres - FT"
    })

    # Exibindo a tabela
    st.dataframe(md_fta_ft_equipes.style.format({"Média de Lances Livres - FTA": "{:.2f}", "Média de  Pontos Feitos por Lances Livres - FT": "{:.2f}"}), use_container_width=True)


st.subheader("Média de pontos, assistências e rebotes dos jogadores")

data_leaders_pts = data.groupby(["Player", "Tm"])[['FG', 'TRB', 'AST']].mean()
leaders_pts = data_leaders_pts.sort_values(by=['FG'], ascending=False)
leaders_pts = leaders_pts.reset_index()
leaders_pts = leaders_pts.rename(columns={
    "Player": "Jogador",
    "Tm": "Time",
    "FG": "Pontos através de cestas (2 ou 3 pontos)",
    "TRB": "Rebotes",
    "AST": "Assistências"
})
st.dataframe(leaders_pts)


st.subheader("Média de cestas de 2 pontos das equipes Top 8")


data["2P"] = data["FG"] - data["3P"]

media_cestas = data.groupby("Tm")[["2P"]].mean()

media_cestas_ordenado = media_cestas.sort_values(by="2P", ascending=False).head(8).reset_index()

media_cestas_ordenado = media_cestas_ordenado.rename(columns={
    "Tm": "Time",
    "2P": "Média de cestas de 2 pontos"
})

st.dataframe(media_cestas_ordenado)

#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()