'''Route dinamica per profilo utente:
Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.
Testare con nomi diversi nell’URL.'''

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return ""

@app.route('/user/<string:username>')
def greet(username: str) -> str:
    return f"<h3> Benvenuto {username} </h3>"