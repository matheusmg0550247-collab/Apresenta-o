import streamlit as st
import base64
from pathlib import Path

# --- Configurações de Página e Caminhos ---
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "static" / "style_v3.css"
VIDEO_FILE = THIS_DIR / "static" / "Computador.mp4" 
ROBO_FILE = THIS_DIR / "static" / "Robô.mp4" # <--- O robô
GEMINI_VIDEO = THIS_DIR / "static" / "Gemini.mp4" # <--- O seu novo vídeo principal

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

# --- Função para carregar vídeo (reutilizável) ---
def get_video_as_base64(video_file):
    try:
        with open(video_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except FileNotFoundError:
        # Este aviso é útil para nós!
        st.warning(f"Aviso: Arquivo de vídeo não encontrado: {video_file}")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar o vídeo: {e}")
        return None

# --- Controle de Página ---
if "page" not in st.session_state:
    st.session_state.page = "home" 

# ==========================================================
# PÁGINA "HOME"
# ==========================================================
if st.session_state.page == "home":
    
    st.markdown('<div class="content-container">', unsafe_allow_html=True) 
    st.markdown("<h1 style='text-align: center; color: white;'>🧠💻 Integrando a IA e programas do convênio Google no dia a dia dos cartórios 🌐</h1>", unsafe_allow_html=True)

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

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    menu_cols = st.columns(3)

    if menu_cols[0].button("Gemini no Email"):
        st.session_state.page = "gemini" 
        st.rerun() 
    if menu_cols[1].button("Módulos Interativos"):
        st.session_state.page = "modulos" 
        st.rerun() 
    if menu_cols[2].button("Configurações Avançadas"):
        st.session_state.page = "config" 
        st.rerun() 
    st.markdown('</div>', unsafe_allow_html=True) 
    st.markdown('</div>', unsafe_allow_html=True) 

# ==========================================================
# PÁGINA "GEMINI NO EMAIL"
# ==========================================================
elif st.session_state.page == "gemini":

    st.markdown('<div class="content-container">', unsafe_allow_html=True) 

    st.markdown("<h1 style='text-align: center; color: white;'>Gemini - Utilizando a inteligência artificial nos emails</h1>", unsafe_allow_html=True)

    if st.button("⬅️ Voltar ao Início"):
        st.session_state.page = "home" 
        st.rerun() 
        
    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Layout de 2 Colunas ---
    col_video_principal, col_robo = st.columns([3, 1]) 

    with col_video_principal:
        # 1. O Player Futurista
        st.markdown('<div class="futuristic-player">', unsafe_allow_html=True)
        
        # MUDANÇA: Usando o arquivo local static/Gemini.mp4
        try:
            st.video(str(GEMINI_VIDEO), autoplay=True)
        except Exception as e:
            st.error(f"Erro ao carregar 'Gemini.mp4'. Verifique se ele existe na pasta 'static'.")
        
        st.markdown('</div>', unsafe_allow_html=True) # Fim do futuristic-player
    
    with col_robo:
        # 2. O Robô em Loop
        st.markdown('<div class="robot-container">', unsafe_allow_html=True)
        
        robo_b64 = get_video_as_base64(ROBO_FILE)
        if robo_b64:
            robo_html = f"""
            <video autoplay loop muted playsinline style="width: 100%; max-width: 250px; border-radius: 10px; border: 1px solid #00FFFF;">
                <source src="data:video/mp4;base64,{robo_b64}" type="video/mp4">
            </video>
            """
            st.markdown(robo_html, unsafe_allow_html=True)
        else:
            # O aviso de "não encontrado" aparecerá aqui
            st.warning("Robo.mp4 não encontrado.")
            
        st.markdown('</div>', unsafe_allow_html=True) # Fim do robot-container
    
    st.markdown('</div>', unsafe_allow_html=True) # Fim do content-container

# ... (resto do código para "modulos", etc.)
