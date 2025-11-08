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

# 1. O Título que você pediu
st.markdown("<h1 style='text-align: center; color: white;'>Gemini - Utilizando a inteligência artificial nos emails</h1>", unsafe_allow_html=True)

# 2. Container para a "transição bacana"
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# 3. Botão para voltar para a página principal
if st.button("⬅️ Voltar ao Início"):
    st.switch_page("app") # Comando para navegar para a página principal (app.py)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. Aqui podemos adicionar o resto (o texto da direita e o botão do vídeo)
st.write("Aqui vai o texto da direita...")

if st.button("▶️ Assistir Demonstração"):
    # (A lógica do modal do vídeo virá aqui)
    st.warning("O modal do vídeo será implementado aqui!")

st.markdown('</div>', unsafe_allow_html=True)
