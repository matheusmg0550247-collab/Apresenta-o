import streamlit as st
import base64
from pathlib import Path

# --- Configurações de Página e Caminhos ---
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "static" / "style_v3.css"
VIDEO_FILE = THIS_DIR / "static" / "Computador.mp4" 

st.set_page_config(
    page_title="IA nos Cartórios",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- Carregar CSS Customizado ---
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: Arquivo CSS não encontrado em {file_path}")

load_css(CSS_FILE)

# --- Função para carregar vídeo (só precisa ser definida uma vez) ---
def get_video_as_base64(video_file):
    try:
        with open(video_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except FileNotFoundError:
        st.error(f"Arquivo de vídeo não encontrado: {video_file}")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar o vídeo: {e}")
        return None

# --- Controle de Página (O CÉREBRO DA SUA IDEIA) ---
if "page" not in st.session_state:
    st.session_state.page = "home" # Começa na 'home'

# --- RENDERIZAÇÃO CONDICIONAL ---

# ==========================================================
# PÁGINA "HOME" (O que você vê primeiro)
# ==========================================================
if st.session_state.page == "home":
    
    # Adicionamos o wrapper de animação em TUDO
    st.markdown('<div class="content-container">', unsafe_allow_html=True) 

    # --- TÍTULO ---
    st.markdown("<h1 style='text-align: center; color: white;'>🧠💻 Integrando a IA e programas do convênio Google no dia a dia dos cartórios 🌐</h1>", unsafe_allow_html=True)

    # --- Layout Principal (Vídeo na Esquerda, Texto na Direita) ---
    col_media, col_texto = st.columns([3, 2], gap="small")

    with col_media:
        video_b64 = get_video_as_base64(VIDEO_FILE)
        if video_b64:
            video_html = f"""
            <div class="video-container">
                <video controlslist="nodownload" autoplay loop muted playsinline style="width: 100%; border-radius: 10px; object-fit: cover;">
                    <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
                </video>
            </div>
            """
            st.markdown(video_html, unsafe_allow_html=True)

    with col_texto:
        texto_para_animar = """
        <div class="animated-text-right">
            <p>A rotina de um cartório é marcada por um <b>alto volume de informações</b>, processos repetitivos e a necessidade de <b>precisão absoluta</b>.</p>
            <p>No entanto, a era digital oferece uma oportunidade sem precedentes para transformar essa reality.</p>
            <p>Ao integrar a <b>inteligência artificial (IA)</b> e as <b>ferramentas do Google</b> no dia a dia, os cartórios podem não apenas otimizar suas atividades, mas também revolucionar a forma como operam.</p>
        </div>
        """
        st.markdown(texto_para_animar, unsafe_allow_html=True)

    # --- Menus "Giratórios" (Botões Estilizados) ---
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    menu_cols = st.columns(3)

    if menu_cols[0].button("Gemini no Email"):
        st.session_state.page = "gemini" # Manda para a página 'gemini'
        st.rerun() # Recarrega o script imediatamente

    if menu_cols[1].button("Módulos Interativos"):
        st.session_state.page = "modulos" # Manda para a página 'modulos'
        st.rerun() 

    if menu_cols[2].button("Configurações Avançadas"):
        st.session_state.page = "config" # Manda para a página 'config'
        st.rerun() 

    st.markdown('</div>', unsafe_allow_html=True) # Fim do button-container
    st.markdown('</div>', unsafe_allow_html=True) # Fim do content-container

# ==========================================================
# PÁGINA "GEMINI NO EMAIL"
# ==========================================================
elif st.session_state.page == "gemini":

    # Adicionamos o wrapper de animação em TUDO
    st.markdown('<div class="content-container">', unsafe_allow_html=True) 

    # 1. O Título que você pediu
    st.markdown("<h1 style='text-align: center; color: white;'>Gemini - Utilizando a inteligência artificial nos emails</h1>", unsafe_allow_html=True)

    # 2. O Botão VOLTAR que você pediu
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.page = "home" # Manda de volta para 'home'
        st.rerun() # Recarrega o script imediatamente

    st.markdown("<hr>", unsafe_allow_html=True)

    # 3. O resto do conteúdo (texto da direita, vídeo, etc.)
    st.write("Aqui vai o texto da direita...")
    if st.button("▶️ Assistir Demonstração"):
        st.video("https://www.youtube.com/watch?v=SSdJ-Oa_n-c")

    st.markdown('</div>', unsafe_allow_html=True) # Fim do content-container

# ==========================================================
# PÁGINA "MÓDULOS" (Exemplo)
# ==========================================================
elif st.session_state.page == "modulos":
    st.markdown('<div class="content-container">', unsafe_allow_html=True) 
    st.markdown("<h1 style='text-align: center; color: white;'>Módulos Interativos</h1>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar ao Início"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("<hr>", unsafe_allow_html=True)
    st.slider("Exemplo de Módulo", 0, 100, 50)
    st.markdown('</div>', unsafe_allow_html=True)

# ... (e assim por diante para as outras páginas) ...
