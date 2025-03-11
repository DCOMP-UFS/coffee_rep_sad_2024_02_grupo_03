import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer


pg = st.navigation([st.Page("pages/home.py", title="Introdução"),
                    st.Page("pages/pontuacoes.py", title="Pontuações"),
                    st.Page("pages/faltas.py", title="Faltas"),
                    st.Page("pages/trocas.py", title="Trocas"),
                    st.Page("pages/eficacia.py", title="Eficácia dos Times"),
                    st.Page("pages/cestinhas.py", title="Cestinhas")])
pg.run()