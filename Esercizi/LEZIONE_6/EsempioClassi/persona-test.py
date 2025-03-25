# dal file persona.py importa la classe Persona
from persona import Persona

# creare un oggetto di tipo persona
lb:Persona = Persona("Lisa", "Bandinelli", 26) # chiamata al costruttore (si comporta come una funzione)

print(lb)

print(lb.name, lb.lastname, lb.age, sep=", ")

# dal file persona2.py importa la classe Persona
from persona2 import Persona

lb:Persona = Persona() 

# voglio richiamare la funzione displayData della classe Persona per stampare in output le informazioni relative alla persona lb
lb.displayData()

# impostare il nome della persona lb
lb.setName("Lisa")

print("-----------------")
lb.displayData()

# impostare il cognome della persona lb
lb.setLastname("Bandinelli")

# impostare il valore della nostrà età
lb.setAge(26)
print("-----------------")

lb.displayData()

print(lb.getName(), lb.getLastname(), lb.getAge())
