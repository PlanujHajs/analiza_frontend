import re
import streamlit as st
from api_client import register_user, login_user

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def registration_form():
    if st.session_state.get("registration_success", False) and st.session_state.get("_clear_reg_fields", False):
        st.session_state["reg_email"] = ""
        st.session_state["reg_password"] = ""
        st.session_state["reg_password_repeat"] = ""
        st.session_state["_clear_reg_fields"] = False

    st.header("Rejestracja")
    with st.form("registration_form", clear_on_submit=True):
        email = st.text_input(
            "Email",
            value="",
            placeholder="Podaj e-mail",
            key="reg_email"
        )
        password = st.text_input(
            "Hasło",
            type="password",
            value="",
            placeholder="Podaj hasło",
            key="reg_password"
        )
        submit = st.form_submit_button("Zarejestruj")

    if submit:
        with st.spinner("Wysyłanie danych..."):
            success, message = register_user(email, password)
            if success:
                st.success(message + " Możesz się teraz zalogować.")
                st.session_state["registration_success"] = True
                st.session_state["_clear_reg_fields"] = True
            else:
                st.error(f"Błąd rejestracji. {message}")


def login_form():
    st.header("Logowanie")
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input(
            "Email",
            value="",
            placeholder="Podaj e-mail",
            key="login_email"
        )
        password = st.text_input(
            "Hasło",
            type="password",
            value="",
            placeholder="Podaj hasło",
            key="login_password"
        )
        submit = st.form_submit_button("Zaloguj")

    if submit:
        if not email or not password:
            st.error("Wypełnij oba pola.")
            return

        with st.spinner("Logowanie, proszę czekać..."):
            success, token, message = login_user(email, password)
            if success:
                st.session_state.current_user = email
                st.session_state.jwt_token = token
                st.rerun()
            else:
                st.error(f"Błąd logowania. {message}")
