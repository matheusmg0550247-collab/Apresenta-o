import streamlit as st
import plotly.graph_objects as go

# Configura o layout da página para ser "largo" (wide)
st.set_page_config(
    page_title="Apresentação Interativa",
    layout="wide"
)

st.title("🌍 Minha Apresentação Interativa")
st.write("Bem-vindo! Use o menu na barra lateral para navegar para as outras telas.")

# --- O Globo Giratório com Plotly ---
st.header("Globo Interativo")

# Criamos uma figura do Plotly
fig = go.Figure(go.Scattergeo(
    lat=[0], # Usamos um ponto simbólico no centro
    lon=[0],
    mode='markers',
    marker=dict(size=1, color='rgba(0,0,0,0)') # Marcador invisível
))

# Atualizamos o layout para mostrar um globo 3D (ortográfico)
fig.update_layout(
    title="Clique e arraste o globo para girar!",
    geo=dict(
        projection_type='orthographic', # Tipo de projeção que parece um globo
        showland=True,                   # Mostrar continentes
        landcolor='rgb(217, 217, 217)',
        showocean=True,                  # Mostrar oceanos
        oceancolor='rgb(100, 149, 237)',
        showcountries=True,
        countrycolor='rgb(60, 60, 60)',
        showcoastlines=True,
        coastlinecolor='rgb(80, 80, 80)',
    ),
    height=600, # Altura do globo
    margin={"r":0,"t":50,"l":0,"b":0} # Ajustar margens
)

# Exibe o gráfico Plotly no Streamlit
st.plotly_chart(fig, use_container_width=True)
