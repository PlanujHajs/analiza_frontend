import streamlit as st
from api_client import change_password

if "jwt_token" not in st.session_state or not st.session_state.jwt_token:
    st.warning("Musisz być zalogowany, aby zmienić hasło.")
    st.stop()

st.title("Zmiana hasła")

old_password = st.text_input(
    "Aktualne hasło",
    type="password",
    placeholder="Wpisz swoje obecne hasło",
    key="cp_old_password"
)

new_password = st.text_input(
    "Nowe hasło",
    type="password",
    placeholder="Wpisz nowe hasło",
    key="cp_new_password"
)

new_password_repeat = st.text_input(
    "Powtórz nowe hasło",
    type="password",
    placeholder="Powtórz nowe hasło",
    key="cp_new_password_repeat"
)

if st.button("Zmień hasło", key="cp_submit_button"):
    if not old_password or not new_password or not new_password_repeat:
        st.error("Proszę wypełnić wszystkie pola.")

    elif new_password != new_password_repeat:
        st.error("Nowe hasła nie są identyczne.")
        st.session_state.cp_new_password_repeat = ""

    elif new_password == old_password:
        st.error("Nowe hasło musi różnić się od starego.")
    else:
        with st.spinner("Zmiana hasła, proszę czekać..."):
            success, message = change_password(old_password, new_password)

            if success:
                st.success(message)
                st.session_state.current_user = ""
                st.session_state.jwt_token = ""
                st.info("Zaloguj się ponownie, używając nowego hasła.")
            else:
                st.error(f"Błąd zmiany hasła: {message}")
