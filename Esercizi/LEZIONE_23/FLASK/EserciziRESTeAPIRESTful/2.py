from flask import Flask, request, jsonify 

'''2. Metodi HTTP e CRUD
Per ciascuna operazione indica il metodo HTTP e il codice di stato corretto:

# Creare un nuovo corso
# Aggiornare i dati di un istruttore
# Eliminare un iscritto
# Ottenere l’elenco dei corsi
# Tentare di accedere a un corso inesistente'''

app = Flask(__name__)

courses = []
@app.route('/courses', methods=['POST'])
def add_course():
    #ottenere dati JSON dalla request 
    #la request serve per leggere dati in arrivo al tuo server Flask
    dati = request.get_json()
    if not dati or 'nome' not in dati:
        return jsonify({'Errore': 'Nome obbligatorio'}), 400
    nuovo_corso = {
        'id': len(courses) + 1,
        'nome': dati['nome'],
        'tipologia': dati.get('tipologia', 'Sconosciuto')
    }

    courses.append(nuovo_corso)
    return jsonify(nuovo_corso), 201 


instructors = []

@app.route('/instructors/<string:instructor_id>', methods=['PATCH'])
def aggiorna_dati_istruttore(instructor_id: str):
    dati = request.get_json()
    if not dati:
        return jsonify({"Errore": "Nessun dato fornito"}), 400
    #inizializzo la variabile 
    instructor_found = None 
    
    for instructor in instructors:
        if instructor['id'] == instructor_id:
            instructor_found = instructor
            break 
    
    if instructor_found is None:
        return jsonify({"Errore": "Istruttore non trovato"}), 404
    
    fields = ["nome", "cognome", "email", "telefono", "specializzazione"]

    for field in fields:
        if field in dati:
            instructor_found[field] = dati[field]
    
    return jsonify(instructor_found), 200


registered = []

@app.route('/registered/<string:client_id>', methods=['DELETE'])
def elimina_iscritto(client_id: str):
    cliente_found = None 

    for client in registered:
        if client['id'] == client_id:
            cliente_found = client 
            break 

    if cliente_found is None:
        return jsonify({"Errore": "Cliente non trovato"}), 404
    
    registered.remove(cliente_found)
    return jsonify({"Conferma": "Cliente eliminato correttamente"}), 200


@app.route('/courses', methods=['GET'])
def elenco_corsi():
    return jsonify(courses), 200


@app.route('/courses/<string:course_id>', methods=['GET'])
def accedi_corso(course_id: str):    
    for course in courses:
        if course['id'] == course_id:
            return jsonify(course), 200
    return jsonify({"Errore": "Corso non presente"}), 404 
        

    