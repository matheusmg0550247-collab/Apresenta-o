import streamlit as st
import base64
from pathlib import Path

# --- Configurações de Página e Caminhos ---
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "static" / "style.css"
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

# --- Função para carregar vídeo como Base64 ---
def get_video_as_base64(video_file):
    try:
        with open(video_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except FileNotFoundError:
        st.error(f"Arquivo de vídeo não encontrado: {video_file}")
        st.warning("Por favor, faça o upload do 'Computador.mp4' para a pasta 'static' no seu GitHub.")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar o vídeo: {e}")
        return None

# --- TÍTULO ---
st.markdown("<h1 style='text-align: center; color: white;'>🧠💻 Integrando a IA e programas do convênio Google no dia a dia dos cartórios 🌐</h1>", unsafe_allow_html=True)

# --- Layout Principal (Vídeo na Esquerda, Texto na Direita) ---
col_media, col_texto = st.columns([3, 2], gap="small")

with col_media:
    # --- VÍDEO ---
    video_b64 = get_video_as_base64(VIDEO_FILE)
    if video_b64:
        video_html = f"""
        <div class="video-container">
            <video controlslist="nodownload" autoplay loop muted playsinline style="width: 100%; border-radius: 10px; object-fit: cover;">
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
                Seu navegador não suporta a tag de vídeo.
            </video>
        </div>
        """
        st.markdown(video_html, unsafe_allow_html=True)

with col_texto:
    # --- TEXTO ANIMADO (LADO DIREITO) ---
    texto_para_animar = """
    <div class="animated-text-right">
        <p>A rotina de um cartório é marcada por um <b>alto volume de informações</b>, processos repetitivos e a necessidade de <b>precisão absoluta</b>.</p>
        <p>No entanto, a era digital oferece uma oportunidade sem precedentes para transformar essa realidade.</p>
        <p>Ao integrar a <b>inteligência artificial (IA)</b> e as <b>ferramentas do Google</b> no dia a dia, os cartórios podem não apenas otimizar suas atividades, mas também revolucionar a forma como operam.</p>
    </div>
    """
    st.markdown(texto_para_animar, unsafe_allow_html=True)

# --- Menus "Giratórios" (Botões Estilizados) ---
st.markdown('<div class="button-container">', unsafe_allow_html=True)
menu_cols = st.columns(3)

if menu_cols[0].button("Apresentação Detalhada"):
    st.session_state.current_page = "detalhes"

if menu_cols[1].button("Módulos Interativos"):
    st.session_state.current_page = "modulos"

if menu_cols[2].button("Configurações Avançadas"):
    st.session_state.current_page = "configuracoes"
st.markdown('</div>', unsafe_allow_html=True)

# --- Área de Conteúdo Dinâmico ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

if st.session_state.current_page == "home":
    pass # Não mostra nada

# ... (o resto do seu app.py continua igual) ...

elif st.session_state.current_page == "detalhes":
    st.markdown("<h3 style='text-align: center; color: #00FFFF;'>Seção de Detalhes da Apresentação</h3>", unsafe_allow_html=True)
    st.write("Aqui você pode colocar gráficos, textos e informações aprofundadas sobre o seu projeto.")
    st.info("Informação importante sobre a apresentação.")

elif st.session_state.current_page == "modulos":
    st.markdown("<h3 style='text-align: center; color: #00FFFF;'>Módulos Interativos</h3>", unsafe_allow_html=True)
    st.write("Nesta seção, você pode adicionar funcionalidades interativas, como sliders, botões para acionar funções ou gráficos dinâmicos.")
    valor = st.slider("Selecione um valor:", 0, 100, 50)
    st.write(f"Você selecionou: {valor}")

elif st.session_state.current_page == "configuracoes":
    st.markdown("<h3 style='text-align: center; color: #00FFFF;'>Configurações Avançadas</h3>", unsafe_allow_html=True)
    st.write("Área para definir parâmetros, opções ou visualizar status do sistema.")
    st.checkbox("Habilitar modo escuro (já está, mas é um exemplo!)")
