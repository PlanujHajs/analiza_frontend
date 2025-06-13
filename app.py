import streamlit as st
from components.auth_forms import registration_form, login_form
from components.layout import hide_sidebar_style

# Inicjalizacja domyślnych wartości w session_state
defaults = {
    "current_user": "",
    "jwt_token": "",
    "registration_success": False,
}
for key, val in defaults.items():
    st.session_state.setdefault(key, val)

st.set_page_config(
    page_title="Projekt python",
    page_icon=":bar_chart:",
    layout="wide"
)

if not (st.session_state.current_user and st.session_state.jwt_token):
    # ukrycie sidbear dla niezalogowanych użytkowników
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

    tabs = st.tabs(["Zaloguj się", "Rejestracja"])
    forms = [login_form, registration_form]

    for tab, form in zip(tabs, forms):
        with tab:
            cols = st.columns([1, 1, 1])
            with cols[1]:
                form()

    st.stop()

col_left, col_right = st.columns([9, 1])
with col_left:
    st.title("Projekt python")
with col_right:
    if st.button("Wyloguj", key="logout_button"):
        st.session_state.current_user = ""
        st.session_state.jwt_token = ""
        st.rerun()

navigation_tree = {
    "Main": [
        st.Page("app_pages/home.py", title="Strona główna",
                icon=":material/home:"),
        st.Page("app_pages/change_password.py",
                title="Zmień hasło", icon=":material/key:"),
    ],
}

nav = st.navigation(navigation_tree, position="sidebar")
nav.run()
