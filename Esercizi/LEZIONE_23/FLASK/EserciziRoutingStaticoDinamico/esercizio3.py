'''Parametri multipli:
Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.'''

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "" 

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int, b:int) -> int:
    return f"La somma dei numeri {a} e {b} è: {a+b}" 

