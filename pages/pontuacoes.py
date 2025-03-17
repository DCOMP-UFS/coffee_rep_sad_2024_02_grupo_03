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

st.divider()

st.subheader("Média de Pontos, Assistências e Rebotes por Jogador")

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

st.divider()

st.subheader("Média de Cestas de 2 pontos das equipes Top 8")

data["2P"] = data["FG"] - data["3P"]

media_cestas = data.groupby("Tm")[["2P"]].mean()

media_cestas_ordenado = media_cestas.sort_values(by="2P", ascending=False).head(8).reset_index()

media_cestas_ordenado = media_cestas_ordenado.rename(columns={
    "Tm": "Time",
    "2P": "Média de cestas de 2 pontos"
})
st.dataframe(media_cestas_ordenado)

st.divider()

st.subheader("📊 Média de Lances e Pontos Feitos por Lances Livres das Equipes")
# Análise da Média de FTA e Pontos Feitos a Partir de FT por Equipe
md_fta_ft_equipes = data_main_stats.groupby("Tm")[["FTA", "FT"]].mean().sort_values(by="FTA", ascending=False).reset_index()
# Renomeando as colunas
md_fta_ft_equipes = md_fta_ft_equipes.rename(columns={
        "Tm": "Equipe",
        "FTA": "Média de Lances Livres - FTA",
        "FT": "Média de  Pontos Feitos por Lances Livres - FT"
})
# Exibindo a tabela
st.dataframe(md_fta_ft_equipes.style.format({"Média de Lances Livres - FTA": "{:.2f}", "Média de  Pontos Feitos por Lances Livres - FT": "{:.2f}"}), use_container_width=True)


st.divider()
st.subheader("Gráficos")
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


teams_stats = data.groupby("Tm")[["FG%", "FT%", "3P", "PTS", "AST", "TRB"]].mean().reset_index()


top8_3p = teams_stats.sort_values(by="3P", ascending=False).head(8)

top5_pts = teams_stats.sort_values(by="PTS", ascending=False).head(5)
top5_ast = teams_stats.sort_values(by="AST", ascending=False).head(5)
top5_trb = teams_stats.sort_values(by="TRB", ascending=False).head(5)

with st.expander("Top 8 Equipes em 3P% (Three-Point Percentage)"):
    fig_3p, ax_3p = plt.subplots(figsize=(10, 6))
    bars_3p = ax_3p.bar(top8_3p["Tm"], top8_3p["3P"], color='darkorange', edgecolor='black')
    ax_3p.set_title("Top 8 Equipes - 3P%", fontsize=14, fontweight='bold')
    ax_3p.set_ylabel("3P%", fontsize=12)
    ax_3p.set_xlabel("Equipe", fontsize=12)
    ax_3p.set_xticklabels(top8_3p["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_3p:
        ax_3p.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                   f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_3p)

with st.expander("Top 5 Equipes em Média de Pontos"):
    fig_pts, ax_pts = plt.subplots(figsize=(10, 6))
    bars_pts = ax_pts.bar(top5_pts["Tm"], top5_pts["PTS"], color='purple', edgecolor='black')
    ax_pts.set_title("Top 5 Equipes - Média de Pontos", fontsize=14, fontweight='bold')
    ax_pts.set_ylabel("Média de Pontos", fontsize=12)
    ax_pts.set_xlabel("Equipe", fontsize=12)
    ax_pts.set_xticklabels(top5_pts["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_pts:
        ax_pts.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_pts)

with st.expander("Top 5 Equipes em Média de Assistências"):
    fig_ast, ax_ast = plt.subplots(figsize=(10, 6))
    bars_ast = ax_ast.bar(top5_ast["Tm"], top5_ast["AST"], color='teal', edgecolor='black')
    ax_ast.set_title("Top 5 Equipes - Média de Assistências", fontsize=14, fontweight='bold')
    ax_ast.set_ylabel("Média de Assistências", fontsize=12)
    ax_ast.set_xlabel("Equipe", fontsize=12)
    ax_ast.set_xticklabels(top5_ast["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_ast:
        ax_ast.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_ast)

with st.expander("Top 5 Equipes em Média de Rebotes"):
    fig_trb, ax_trb = plt.subplots(figsize=(10, 6))
    bars_trb = ax_trb.bar(top5_trb["Tm"], top5_trb["TRB"], color='brown', edgecolor='black')
    ax_trb.set_title("Top 5 Equipes - Média de Rebotes", fontsize=14, fontweight='bold')
    ax_trb.set_ylabel("Média de Rebotes", fontsize=12)
    ax_trb.set_xlabel("Equipe", fontsize=12)
    ax_trb.set_xticklabels(top5_trb["Tm"], rotation=45, fontsize=10)
    
    for bar in bars_trb:
        ax_trb.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f"{bar.get_height():.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')
    st.pyplot(fig_trb)
#rodapé

st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()