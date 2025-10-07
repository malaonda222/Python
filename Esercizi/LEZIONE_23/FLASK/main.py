from flask import Flask , url_for

app = Flask(__name__)

# app.run(debug=True)

@app.route('/')
def home() -> str:
    return "<h3> Hello, World! </h3>"

@app.route('/datanalyst')
def data() -> str:
    return "<h3> Sei uno studente di Data Analyst </h3>"

# @app.route('/user/<string:username>')
# def show_user_profile(username: str) -> str:
#     return f"<h2> Profilo di {username} </h2>"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f"Post {post_id}"

@app.route('/user/<string:username>/<int:age>')
def show_user_profile(username: str, age: int) -> str:
    return f"Profilo di {username} con {age} anni"

@app.route('/user/<string:username>')
def saluto(username: str) -> str:
    return f"Ciao {username}, come stai?"

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('show_user_profile', username='John Doe'))
#     print(url_for('show_post', post_id=42))
