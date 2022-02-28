import json

import eel
import requests

eel.init('static')

auth = None


@eel.expose
def send_login_form(login: str, password: str) -> dict:
    """Send request with form to server for login"""
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {"username": login, "password": password}
    try:
        response = requests.post("http://127.0.0.1:1000/login", headers=headers, data=data)
        return response.json()
    except requests.exceptions.ConnectionError:
        return {'connection': 'failed'}


@eel.expose
def send_register_form(login: str, password: str):
    """Send request for register"""
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {"username": login, "password": password}
    try:
        response = requests.post("http://127.0.0.1:1000/register", headers=headers, data=data)
        return response.json()
    except requests.exceptions.ConnectionError:
        return {'connection': 'failed'}


@eel.expose
def get_contacts() -> json:
    res = requests.get("http://127.0.0.1:1000/getUsers")
    return res.json()['users']


@eel.expose
def set_username(username: str):
    global auth
    auth = username


@eel.expose
def get_username():
    return auth


eel.start('login.html', size=(800, 800), position=(550, 150))
