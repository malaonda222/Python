'''1. livello 1 (unico endpoint, POST usato anche per leggere dati, azione definita 
nel body e payload separato);

2. Livello 2/1 (endpoint separato per prenotazioni e usa POST per creare una risorsa; 
endpoint separato per utenti, usa GET ma l server legge client_id dal body e non dai parametri di query;

3. Livello 3 (endpoint separati per le risorse, utilizzo dei verbi HTTP, utilizzo 
degli HATEOAS -link, href, method, body_schema-

4. Livello 1 (endpoint separai per risorse, uso sempre di POST, "action" nel body: 
usata per indicare appunto l'azione, tutti i dati passando nel JSON del body(payload))
'''