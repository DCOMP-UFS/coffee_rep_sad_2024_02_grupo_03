import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card

st.title("Faltas")
st.divider()

# Função para carregar os dados com cache
@st.cache_data  
def load_data():
    return pd.read_csv("./dados/2023-2024_NBA_Player_Stats_Regular.csv", delimiter=';', encoding="ISO-8859-1")

df = load_data()

st.subheader("🏀 Média de Faltas Cometidas (PF) - TOP 5 Equipes")

# Seleciona as top 5 equipes com mais faltas cometidas (PF)
top_5_equipes = df.groupby('Tm')['PF'].sum().nlargest(5).reset_index()

# Calcula a média de faltas das 5 equipes
media_faltas_equipes = top_5_equipes['PF'].mean()

# Exibe a tabela com as 5 equipes com mais faltas cometidas
st.dataframe(top_5_equipes)

# Exibe a métrica da média de faltas cometidas pelas TOP 5 equipes
st.metric("Média de Faltas Cometidas (TOP 5 Equipes)", round(media_faltas_equipes, 2))

st.divider()

st.subheader("⛹🏾‍♂️  Média de faltas cometidas (PF) - TOP 5 Jogadores")

# Seleciona os top 5 jogadores com mais faltas cometidas (PF)
top_5 = df.nlargest(5, 'PF')[['Player', 'Tm', 'PF']]

# Calcula a média de faltas dos 5 jogadores
media_faltas = top_5['PF'].mean()

# Exibe a tabela com os 5 jogadores com mais faltas cometidas
st.dataframe(top_5)

# Exibe a métrica da média de faltas cometidas pelos TOP 5
st.metric("Média de Faltas Cometidas (TOP 5)", round(media_faltas, 2))

st.divider()
# Expansão para os 10 jogadores com mais faltas cometidas


with st.expander("📉⛹🏾‍♂️  Tabela com Top 10 jogadores com mais faltas 🔎"):
    # Calcular o total de faltas por jogador
    top_jogadores_faltas = df.groupby('Player')['PF'].sum().sort_values(ascending=False).head(10)

    # Exibir os dados em formato de tabela
    st.write("📉⛹🏾‍♂️  Top 10 jogadores com mais faltas totais e suas quantidades de faltas:")
    st.dataframe(top_jogadores_faltas)

with st.expander("📉⛹🏾‍♂️  Top 5 jogadores com mais faltas totais 📊"):
    # Calcular o total de faltas por jogador
    top_jogadores_faltas = df.groupby('Player')['PF'].sum().sort_values(ascending=False).head(5)

    # Gráfico de barras vertical
    plt.figure(figsize=(10, 6))
    ax = top_jogadores_faltas.plot(kind='bar', color='lightcoral', edgecolor='black')
    plt.title(" Gráfico com o Top 5 Jogadores com Mais Faltas")
    plt.ylabel("Quantidade de Faltas")
    plt.xlabel("Jogadores")
    
    # Alinhamento do gráfico
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(top_jogadores_faltas.index, rotation=0, ha='center', fontsize=7)  # Nomes dos jogadores alinhados horizontalmente
    
    # Adicionando os valores nas barras (mais próximos das barras)
    for i in ax.patches:
        ax.text(i.get_x() + i.get_width() /  2, i.get_height(),  # Ajustando a posição dos valores
                str(int(i.get_height())),
                ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Exibe o gráfico
    st.pyplot(plt)

with st.expander("📉🏀 Tabela com Top 10 Equipes com mais Faltas 🔎"):
    # Calcular o total de faltas por equipe
    top_equipes_faltas = df.groupby('Tm')['PF'].sum().sort_values(ascending=False).head(10)

    # Exibir os dados em formato de tabela
    st.write("📉🏀 Top 10 equipes com mais faltas totais e suas quantidades de faltas:")
    st.dataframe(top_equipes_faltas)

with st.expander("📉🏀 Top 5 Equipes com mais Faltas Totais 📊"):
    # Calcular o total de faltas por equipe
    top_equipes_faltas = df.groupby('Tm')['PF'].sum().sort_values(ascending=False).head(5)

    # Gráfico de barras vertical
    plt.figure(figsize=(10, 6))
    ax = top_equipes_faltas.plot(kind='bar', color='lightcoral', edgecolor='black')
    plt.title("Gráfico com o Top 5 Equipes com Mais Faltas")
    plt.ylabel("Quantidade de Faltas")
    plt.xlabel("Equipes")
    
    # Alinhamento do gráfico
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(top_equipes_faltas.index, rotation=0, ha='center', fontsize=7)  # Nomes das equipes alinhados horizontalmente
    
    # Adicionando os valores nas barras (mais próximos das barras)
    for i in ax.patches:
        ax.text(i.get_x() + i.get_width() /  2, i.get_height(),  # Ajustando a posição dos valores
                str(int(i.get_height())),
                ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Exibe o gráfico
    st.pyplot(plt)



#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()

