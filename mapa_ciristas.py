import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
import plotly.io as pio
pio.renderers.default='browser'

ciro_novo = pd.read_csv('Ciro_Novo_Com_Coordenadas.csv')
ceps_validos_long = ciro_novo['zipcode'][ciro_novo['Longitude'].notna()]

df_mapa = ciro_novo.dropna(subset=["Latitude", "Longitude"])
fig = px.scatter_mapbox(
    df_mapa,
    lat="Latitude",
    lon="Longitude",
    hover_name="name",  # Nome da pessoa para aparecer no hover
    hover_data=["zipcode", "Logradouro", "Bairro"],  # Informações extras ao passar o mouse
    zoom=4,  # Nível de zoom inicial
    mapbox_style="open-street-map"  # Estilo do mapa (pode usar "carto-positron" ou outros)
)

# Mostrando o mapa
st.plotly_chart(fig)
