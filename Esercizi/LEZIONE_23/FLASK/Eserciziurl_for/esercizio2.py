'''Navigazione dinamica:
Creare una pagina con elenco utenti fittizi e i relativi link ai 
loro profili generati con url_for.'''

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "" 

@app.route('/userprofile/<string:username>/<int:eta>')
def userprofile(username:str, eta: int) -> str:
    return f"Profilo di {username} - Età: {eta}"

@app.route('/users')
def users() -> list:

    url_lisa = url_for('userprofile', username="Lisa", eta=55)
    url_marco = url_for('userprofile', username="Marco", eta=10)
    url_mario = url_for('userprofile', username="Mario", eta=28)
    url_giada = url_for('userprofile', username="Giada", eta=46)

    risposta = "<h3>Elenco dei nomi degli utenti e dei loro link:</h3><br>"
    risposta += f"<h4>Lisa - {url_lisa}</h4><br>"
    risposta += f"<h4>Marco - {url_marco}</h4><br>"
    risposta += f"<h4>Mario - {url_mario}</h4><br>"
    risposta += f"<h4>Giada - {url_giada}</h4>"

    return risposta 