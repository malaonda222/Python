'''Mini blog:
Definire route /post/<int:id> che restituisca un articolo fittizio.
Creare una pagina /posts con un elenco di post e i relativi link agli 
articoli generati tramite url_for.'''

from flask import Flask, url_for 

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return ""

@app.route('/post/<int:id>')
def post(id:int) -> int:
    return f"Post: {id}"

@app.route('/posts')
def posts() -> list:
    
