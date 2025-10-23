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
    url_id1 = url_for('post', id=1)
    url_id10 = url_for('post', id=10)
    url_id22 = url_for('post', id=22)
    url_id48 = url_for('post', id=48)

    risposta = "<h3>Elenco dei post con i relativi link:</h3>"
    risposta += f"<h4>Id1 - {url_id1}</h4><br>"
    risposta += f"<h4>Id10 - {url_id10}</h4><br>"
    risposta += f"<h4>Id22 - {url_id22}</h4><br>"
    risposta += f"<h4>Id48 - {url_id48}</h4>"

    return risposta 



#oppure 
app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "" 

@app.route('/id/<int:id>')
def mostra_id(id: int) -> str:
    return f"Id numero: {id}"

@app.route('/ids')
def ids() -> str:
    elenco_id = [
        1, 10, 22, 48
    ]

    result = "<h3>Elenco degli id</h3>"
    for id in elenco_id:
        url = url_for('mostra_id', id = id)
        result += f"<h4>{id} - <a href='{url}'>{url}</a></h4>"
    return result 