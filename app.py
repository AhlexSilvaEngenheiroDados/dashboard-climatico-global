import streamlit as st
import pandas as pd
import plotly.express as px
from data_fetcher import get_all_cities_data

# Configuração da página
st.set_page_config(page_title="Dashboard Climático Global", layout="wide")

# Título e Introdução
st.title("🌍 Dashboard Climático Global")
st.markdown("""
Este dashboard apresenta dados climáticos reais coletados via API da **Open-Meteo**. 
Como um Engenheiro de Dados, este projeto demonstra o ciclo de:
1. **Extração** (API) 
2. **Transformação** (Pandas) 
3. **Visualização** (Streamlit/Plotly).
""")

# Botão para atualizar dados
if st.button('🔄 Atualizar Dados'):
    st.cache_data.clear()

# Coleta de dados (com cache para performance)
@st.cache_data
def load_data():
    return get_all_cities_data()

df = load_data()

# Métricas principais em colunas
st.subheader("📊 Resumo Atual")
cols = st.columns(len(df))
for i, row in df.iterrows():
    cols[i].metric(row['Cidade'], f"{row['Temperatura']}°C", f"{row['Vento']} km/h vento")

# Gráficos interativos
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🌡️ Comparativo de Temperatura")
    fig_temp = px.bar(df, x='Cidade', y='Temperatura', 
                     color='Temperatura', 
                     color_continuous_scale='RdYlBu_r',
                     text_auto=True)
    st.plotly_chart(fig_temp, use_container_width=True)

with col_right:
    st.subheader("💨 Velocidade do Vento")
    fig_wind = px.line(df, x='Cidade', y='Vento', 
                      markers=True,
                      labels={'Vento': 'Velocidade (km/h)'})
    st.plotly_chart(fig_wind, use_container_width=True)

# Tabela de dados brutos
st.divider()
st.subheader("📂 Dados Brutos")
st.dataframe(df, use_container_width=True)

# Rodapé
st.markdown("---")
st.caption("Desenvolvido para portfólio de Engenharia de Dados. Dados reais fornecidos por Open-Meteo.")
