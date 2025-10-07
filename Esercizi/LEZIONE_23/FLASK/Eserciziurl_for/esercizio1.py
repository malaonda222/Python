'''Generazione link interni:
Usare url_for per creare automaticamente i link alle route definite,
ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.)'''

from flask import Flask, url_for 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return ""

@app.route('/about')
def about() -> str:
    return "Benvenuto nella prima web app di Flask!"

@app.route('/square/<int:n>')
def square(n:int) -> int:
    return f"Il quadrato di {n} è: {n**2}"

@app.route('/user/<string:username>')
def greet(username: str) -> str:
    return f"<h3> Benvenuto {username} </h3>"

@app.route('/show-urls')
def show_urls():
    home_url = url_for('home')
    about_url = url_for('about')
    square_url = url_for('square', n=12)
    greet_url = url_for('greet', username='Lisssa')
    return f"""
<p>Home: {home_url}</p>
<p>About: {about_url}</p>
<p>Square: {square_url}</p>
<p>Greet: {greet_url}</p>
"""

with app.test_request_context():
    print(url_for('home'))
    print(url_for('about'))
    print(url_for('square', n=12))
    print(url_for('greet', username='Lisssa Bannndi'))