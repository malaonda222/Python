# Sending Messages

messages = ["How are you?", "Someone", "Always"]
sent_messages = []

def send_messages():
    while messages:
        messaggio = messages.pop(0)
        print(f"Sto inviando il messaggio: {messaggio}")

        sent_messages.append(messaggio)

send_messages()

print(f"Lista dei messaggi originali: {messages}")
print(f"Lista dei messaggi inviati: {sent_messages}")
