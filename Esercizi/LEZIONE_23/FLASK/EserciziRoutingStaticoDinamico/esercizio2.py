'''Route con parametri numerici:
Definire /square/<int:n> che ritorni il quadrato di n.'''

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "" 

@app.route('/square/<int:n>')
def square(n:int) -> int:
    return f"Il quadrato di {n} è: {n**2}"