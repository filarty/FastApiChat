import eel
import requests

eel.init('static')


@eel.expose
def hello():
    print("hello")


@eel.expose
def send_login_form(login: str, password: str):
    response = requests.post("http://127.0.0.1:1000/login",
                             headers={'Content-type': 'application/x-www-form-urlencoded'},
                             data={"username": login, "password": password})
    return response.json()


eel.start('main_page.html', size=(800, 800), geometry={"size": (800, 800)}, jinja_templates="main_page.html")
