import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card

st.title("Trocas")
st.write("Durante a temporada regular, ocorre uma janela de transferências, em que é permitido que os times troquem seus jogadores.")
st.divider()


@st.cache_data  
def load_data():
    return pd.read_csv("dados/2023-2024_NBA_Player_Stats_Regular.csv", sep=";",encoding='iso-8859-1')
data = load_data()

st.markdown("### Lista de Jogadores trocados")
data_trocas = data[['Player', 'Tm']]
trocas = data_trocas[data_trocas['Tm']=="TOT"]
st.dataframe(trocas[['Player']].reset_index(drop=True))

st.divider()

st.markdown("### Lista de Times que sofreram trocas")
st.write("Times que sofreram alterações em seu elenco, seja na entrada ou saída de jogadores.")
st.write("Por exemplo, o jogador Precious Achiuwa saiu do time Toronto Raptors (TOR) e entrou no time New Rork Knicks (NYK). Participa tanto da estatística do TOR (saída) quanto do Knicks (entrada).")
lista_jogadores = trocas['Player'].to_list()
data_jogadores = data[data.Player.isin(lista_jogadores)]
data_jogadores_filter = data_jogadores[data_jogadores.Tm!="TOT"]
contagem_trocas_por_time = data_jogadores_filter[["Tm"]].groupby("Tm").value_counts().sort_values(ascending=False).to_frame("Quantidade de Trocas").reset_index()
st.dataframe(contagem_trocas_por_time)

st.write("Gráfico de barras - Quantidade de trocas por time")
st.bar_chart(contagem_trocas_por_time[["Tm", "Quantidade de Trocas"]], x="Tm", y="Quantidade de Trocas", x_label="Time")


#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()