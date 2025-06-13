import requests
from requests.exceptions import RequestException
import streamlit as st

BASE_URL = "http://localhost:8000"


def register_user(email: str, password: str):
    try:
        payload = {"email": email, "password": password}
        resp = requests.post(
            f"{BASE_URL}/auth/register",
            json=payload,
            timeout=5
        )
        if resp.status_code == 201:
            return True, "Rejestracja zakończona pomyślnie."
        else:
            try:
                error_json = resp.json()
                message = error_json.get("detail", resp.text)
            except ValueError:
                message = resp.text
            return False, message
    except RequestException as e:
        return False, f"Błąd połączenia z serwerem: {e}"


def login_user(email: str, password: str):
    try:
        form_data = {"username": email, "password": password}
        resp = requests.post(
            f"{BASE_URL}/auth/token",
            data=form_data,
            timeout=5
        )
        if resp.status_code == 200:
            token_obj = resp.json()
            access_token = token_obj.get("access_token")
            if not access_token:
                return False, None, "Brak tokenu w odpowiedzi serwera."
            return True, access_token, ""
        else:
            try:
                error_json = resp.json()
                message = error_json.get("detail", resp.text)
            except ValueError:
                message = resp.text
            return False, None, message
    except RequestException as e:
        return False, None, f"Błąd połączenia z serwerem: {e}"


def get_auth_headers():
    token = st.session_state.get("jwt_token", "")
    if token:
        return {"Authorization": f"Bearer {token}"}
    else:
        return {}


def change_password(old_password: str, new_password: str):
    try:
        payload = {"old_password": old_password, "new_password": new_password}
        headers = get_auth_headers()
        resp = requests.post(
            f"{BASE_URL}/auth/change-password",
            json=payload,
            headers=headers,
            timeout=5
        )
        if resp.status_code == 204:
            return True, "Hasło zmienione pomyślnie."
        else:
            try:
                error_json = resp.json()
                message = error_json.get("detail", resp.text)
            except ValueError:
                message = resp.text
            return False, message
    except RequestException as e:
        return False, f"Błąd połączenia z serwerem: {e}"


def get_charts_data():
    try:
        headers = get_auth_headers()
        resp = requests.get(
            f"{BASE_URL}/charts/",
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            return True, resp.json()
        else:
            try:
                error_json = resp.json()
                message = error_json.get("detail", resp.text)
            except ValueError:
                message = resp.text
            return False, message
    except RequestException as e:
        return False, f"Błąd połączenia z serwerem: {e}"
