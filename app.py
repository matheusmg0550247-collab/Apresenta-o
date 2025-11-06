import streamlit as st
import base64

# Configurações da página
st.set_page_config(
    page_title="Apresentação Futurista",
    layout="centered", # Centered para focar na imagem e menus
    initial_sidebar_state="collapsed" # Esconder a barra lateral padrão se não for usar as pages/
)

# --- Carregar CSS Customizado ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("static/style.css")


# --- Conteúdo Principal: Imagem do Computador e Menus ---

st.markdown("<h1 style='text-align: center; color: white;'>🧠💻 Apresentação Futurista 🌐</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #CCCCCC;'>Selecione uma opção abaixo para navegar.</p>", unsafe_allow_html=True)

# Centralizar a imagem do computador
col1, col2, col3 = st.columns([1, 2, 1]) # Usar colunas para centralizar
with col2:
    # Exibir a imagem do computador
    st.image("static/computer.png", width=300, caption="Sistema Principal")

st.markdown("---") # Separador visual

# --- Menus "Giratórios" (Botões Estilizados) ---
# Vamos criar botões que simulam a navegação.
# Para navegar entre páginas (`pages/`), o usuário ainda usaria a sidebar ou links diretos.
# Mas aqui, vamos simular um menu *dentro* da página principal.

st.markdown("<h2 style='text-align: center; color: white;'>Navegação Rápida</h2>", unsafe_allow_html=True)

# Usar colunas para dispor os botões horizontalmente e dar um senso de "órbita"
menu_cols = st.columns(3)

if menu_cols[0].button("Apresentação Detalhada"):
    st.session_state.current_page = "detalhes"

if menu_cols[1].button("Módulos Interativos"):
    st.session_state.current_page = "modulos"

if menu_cols[2].button("Configurações Avançadas"):
    st.session_state.current_page = "configuracoes"

st.markdown("---") # Separador visual

# --- Área de Conteúdo Dinâmico ---
# O conteúdo abaixo mudará com base no botão clicado

if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

if st.session_state.current_page == "home":
    st.markdown("<h3 style='text-align: center; color: #00FFFF;'>Bem-vindo ao Sistema!</h3>", unsafe_allow_html=True)
    st.write("Esta é a sua tela inicial com o computador central. Explore as opções acima!")
    st.write("Você pode adicionar mais informações ou um texto introdutório aqui.")

elif st.session_state.current_page == "detalhes":
    st.markdown("<h3 style='text-align: center; color: #00FFFF;'>Seção de Detalhes da Apresentação</h3>", unsafe_allow_html=True)
    st.write("Aqui você pode colocar gráficos, textos e informações aprofundadas sobre o seu projeto.")
    st.write("Exemplo de conteúdo:")
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

# Para retornar à página "01_Outra_Tela.py" via sidebar, você precisaria do sidebar.
# Se você *realmente* quiser desativar a sidebar para esse look,
# terá que fazer a navegação entre as páginas do *app.py* e *01_Outra_Tela.py* via `st.link_button` ou similar.
# Por enquanto, vou manter as `pages/` mas com a sidebar "colapsada" (escondida por padrão).
