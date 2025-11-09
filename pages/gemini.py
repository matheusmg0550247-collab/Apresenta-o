import streamlit as st
from pathlib import Path

# --- Carregar CSS (Precisa ser feito em TODA página) ---
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: Arquivo CSS não encontrado em {file_path}")

# Aponta para a pasta raiz (fora de /pages)
THIS_DIR = Path(__file__).parent.parent 
CSS_FILE = THIS_DIR / "static" / "style_v3.css"
load_css(CSS_FILE)

# --- Conteúdo da Nova Página ---

# Container para a "transição bacana" (fade-in)
st.markdown('<div class="content-container">', unsafe_allow_html=True) 

# 1. O Título que você pediu
st.markdown("<h1 style='text-align: center; color: white;'>Gemini - Utilizando a inteligência artificial nos emails</h1>", unsafe_allow_html=True)

# 2. O Botão VOLTAR (corrigido)
if st.button("⬅️ Voltar ao Início"):
    st.switch_page("app.py") # Comando para navegar para a página principal

st.markdown("<hr>", unsafe_allow_html=True)

# 3. O Player Futurista
st.markdown('<div class="futuristic-player">', unsafe_allow_html=True)
# Lembre-se de trocar esta URL pelo seu vídeo (ex: "static/robo.mp4")
st.video("https://www.youtube.com/watch?v=SSdJ-Oa_n-c", autoplay=True)
st.markdown('</div>', unsafe_allow_html=True) # Fim do futuristic-player
    
st.markdown('</div>', unsafe_allow_html=True) # Fim do content-container
