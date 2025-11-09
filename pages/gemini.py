import streamlit as st
from pathlib import Path

# --- Definindo as funções primeiro (sem executar nada) ---

def load_css(file_path):
    """Função para carregar o CSS"""
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: Arquivo CSS não encontrado em {file_path}")

def show_gemini_page():
    """Função principal que desenha TUDO da página"""
    
    # 1. Carrega o CSS (AGORA de forma segura, dentro da função)
    THIS_DIR = Path(__file__).parent.parent 
    CSS_FILE = THIS_DIR / "static" / "style_v3.css"
    load_css(CSS_FILE)

    # 2. Container para a "transição bacana" (fade-in)
    st.markdown('<div class="content-container">', unsafe_allow_html=True) 

    # 3. O Título que você pediu
    st.markdown("<h1 style='text-align: center; color: white;'>Gemini - Utilizando a inteligência artificial nos emails</h1>", unsafe_allow_html=True)

    # 4. O Botão VOLTAR (correto)
    if st.button("⬅️ Voltar ao Início"):
        st.switch_page("app") 

    st.markdown("<hr>", unsafe_allow_html=True)

    # 5. O Player Futurista
    st.markdown('<div class="futuristic-player">', unsafe_allow_html=True)
    # Lembre-se de trocar esta URL pelo seu vídeo (ex: "static/robo.mp4")
    st.video("https://www.youtube.com/watch?v=SSdJ-Oa_n-c", autoplay=True)
    st.markdown('</div>', unsafe_allow_html=True) # Fim do futuristic-player
        
    st.markdown('</div>', unsafe_allow_html=True) # Fim do content-container

# --- PONTO DE ENTRADA ---
# Esta é a única linha "solta". O Streamlit vai chamar isso
# DEPOIS que a página for registrada e o usuário navegar para cá.
show_gemini_page()
