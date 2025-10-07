'''Definire un route/about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.'''

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "" 

@app.route('/about')
def about() -> str:
    return "Benvenuto nella prima web app di Flask!"



