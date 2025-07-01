# Archived Messages
messages = ["How are you?", "Someone", "Always"]
sent_messages = []
messages_stored = messages [:]

def send_messages():
    while messages:
        messaggio = messages.pop(0)
        print(f"Sto inviando il messaggio: {messaggio}")

        sent_messages.append(messaggio)

send_messages()

print(f"Lista dei messaggi originali: {messages}")
print(f"Lista dei messaggi inviati: {sent_messages}")
print(f"Lista dei messaggi archiviati: {messages_stored}")



lista_messaggi = ["Finalmente insieme!", "Come stai?", "A presto, ci sentiamo."]
sent_messages = []
lista_messaggi_copy = lista_messaggi[:]

def send_messages():
      
    while lista_messaggi:
        messaggio = lista_messaggi.pop(0)
        print(f"Sto inviando il messaggio {messaggio}")

        sent_messages.append(messaggio)

send_messages()      
print(f"Messaggi originali: {lista_messaggi}")
print(f"Messaggi inviati: {sent_messages}")
print(f"I messaggi mandati sono: {lista_messaggi_copy}")