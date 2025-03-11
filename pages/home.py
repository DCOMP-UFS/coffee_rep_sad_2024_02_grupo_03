import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Basks&Stats🏀")
st.markdown(" 📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.markdown("Dados disponíveis em: https://www.kaggle.com/datasets/vivovinco/2023-2024-nba-player-stats")

st.divider()

st.header("Sobre os dados")
st.write("A NBA é a liga estadunidense de basquete e é considerada a principal liga de basquete do mundo. A temporada regular da NBA tem 82 partidas para cada um de seus times, que são divididos em duas conferências, Leste e Oeste, referentes a sua posição geográfica no continente.")
st.write("Os dados referem-se as estatísticas gerais do jogadores na temporada regular 2023-2024.")
st.write("Ao total são 735 observações.")
st.markdown("### Colunas:")
st.markdown("* Rk (Rank) - identificador")
st.markdown("* Player - nome do jogador")
st.markdown("* Age - idade do jogador")
st.markdown("* Tm (Team) - sigla do time ")
st.markdown("* G (Games played) - jogos que participou")
st.markdown("* Gs (Games started) - jogos em que foi titular")
st.markdown("* MP - minutos jogados por jogo")
st.markdown("* FG (Field goals) - pontos através de cestas (2 ou 3 pontos) por jogo")
st.markdown("* FGA (Fields goals attempts) - tentativa de arremessos a cesta")
st.markdown("* FG% - porcentagem de acertos dos arremessos")
st.markdown("* 3P - cestas de 3 pontos por jogos")
st.markdown("* 3PA - tentativa de arremessos de 3 pontos")
st.markdown("* 3P% - porcentagem de acertos dos arremessos de 3 pontos")
st.markdown("* eFG% - eficácia do arremesso, levando em conta que um arremesso de 3 pontos vale mais do que um de 2 ponto")
st.markdown("* FT (free trow) - lances livres por jogo")
st.markdown("* FTA - tentativas de lances livres por jogo")
st.markdown("* FT% - porcentagem de lances livres convertidos")
st.markdown("* ORB (offensive rebounds) - rebotes ofensivos por jogo")
st.markdown("* DRB (defensive rebounds) - rebotes defensivos por jogo")
st.markdown("* TRB (total rebounds) - rebotes por jogo")
st.markdown("* AST (assists) - assistência por jogo")
st.markdown("* STL (steal) - roubos de bola por jogo")
st.markdown("* BLK (block) - bloqueios a cestas adversárias por jogo")
st.markdown("* TOV (turnover) - perda da posse da bola por jogo")
st.markdown("* PF (persounal fouls) - faltas pessoais por jogo")
st.markdown("* PTS (points) - total de pontos por jogo, considera-se cestas e lances livres")

st.write("Obs: Na coluna Tm, a sigla TOT significa que o jogador esteve em dois ou mais times.")

st.divider()

st.header("O tomador de decisão")
st.write("Nosso intuito é apoiar a tomada de decisão de apostadores. Além de entender as estatísticas referentes ao jogo, o apostador tem em mãos a performance e o impacto dos jogadores em seus respectivos times.")
st.write("Além de apostas do time vencedor da partida, é possível apostar sobre o volume de pontos, assistência, rebotes e combinação de estatísticas.")

st.markdown("### Tipos de Apostas no Basquete")
st.markdown("##### Over/Under")
st.markdown("* Se a soma dos pontos marcados por ambas as equipes será acima (over) ou abaixo (under) de um valor determinado pelo site de apostas")
st.markdown("* Análise do desempenho ofensivo e defensivo das equipes, bem como fatores que podem influenciar a pontuação, como lesões ou estratégias de jogo.")
st.markdown("##### Total de pontos")
st.markdown("* Total de pontos de uma equipe específica em vez da soma dos pontos das duas equipes.")
st.markdown("* Análise do desempenho individual das equipes.")
st.markdown("#### Primeiro a Marcar")
st.markdown("* Prever se determinado jogador ou equipe irá atingir determinada pontuação primeiro.")
st.markdown("* Exemplo, em uma partida Bulls X Lakers, Bulls serão o primeiro a atingur a marca de 20 pontos no jogo.")
st.markdown("#### Apostas em Jogadores")
st.markdown("* Aposta em desempenho individual. Se determinado jogador irá pontuar, por exemplo, 15+ pontos.")
st.markdown("#### Combinação de estatísticas")
st.markdown("* Se determinado jogador irá pontuar em mais de uma estatística. Por exemplo, pontuação de 15+ pontos e 5+ assistências.")
st.markdown("* Incluem os famosos double-double ou triple-double, ou seja, duas a três estatísticas na casa dos dois dígitos.")
st.markdown("* Análise do volume de jogo individual.")

st.markdown("### Dicas Gerais")
st.markdown("* Analise a influência do time jogar em casa.")
st.markdown("* Impacto das cestas de 3 pontos. Times que dependem muito de arremessos de longa distância podem ter uma variação maior na pontuação.")
st.markdown("* Identifique times com jogadores decisivos, os famosos cestinhas. O impacto desse tipo de jogador no time é positivamente grande, mas uma troca ou lesão do jogador pode alterar a performance do time.")


st.divider()

st.subheader("Explore os dados")
st.write("Você pode selecionar uma ou mais colunas para filtrar abaixo:") 
df = pd.read_csv("./dados/2023-2024_NBA_Player_Stats_Regular.csv", delimiter=';', encoding="ISO-8859-1")
filter_df = dataframe_explorer(df)
st.dataframe(filter_df)


#rodapé
st.divider()
st.markdown("#### Basks&Stats🏀")
st.markdown("📊 Sistema de Apoio à Decisão: Basquete para Apostadores")
st.text("Unidade 03 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")
st.divider()