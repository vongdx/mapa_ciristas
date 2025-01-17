import streamlit as st
import plotly.express as px
import pandas as pd

# Verificando se o arquivo CSV existe
csv_file = "Ciro_Novo_Com_Coordenadas.csv"

try:
    # Tenta carregar o CSV
    df_mapa = pd.read_csv(csv_file)
    st.write("✅ DataFrame carregado com sucesso!")
except FileNotFoundError:
    st.error("❌ Erro: Arquivo CSV não encontrado! Verifique se o arquivo foi enviado para o GitHub.")
    st.stop()  # Para a execução se o CSV não for encontrado

# Removendo linhas sem Latitude e Longitude
df_mapa = df_mapa.dropna(subset=["Latitude", "Longitude"])

# Verificando se as colunas existem
if "Latitude" not in df_mapa.columns or "Longitude" not in df_mapa.columns:
    st.error("❌ Erro: O DataFrame não contém colunas de Latitude e Longitude!")
    st.write("🔍 Colunas encontradas:", df_mapa.columns)
    st.stop()

# Criando o mapa com Plotly
fig = px.scatter_mapbox(
    df_mapa,
    lat="Latitude",
    lon="Longitude",
    hover_name="name",
    hover_data=["zipcode", "Logradouro", "Bairro"],
    zoom=4,
    mapbox_style="open-street-map",
    color_discrete_sequence=["red"],  # Cor vermelha para os pontos
    size_max=12 
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
