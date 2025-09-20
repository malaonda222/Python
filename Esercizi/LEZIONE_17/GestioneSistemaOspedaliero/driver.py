from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.persona import Persona
from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.dottore import Dottore 
from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.paziente import Paziente 
from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.fatture import Fattura 

urologo = Dottore("Nicola", "Buio", "urologo", 152.3)
cardiologo = Dottore("Simone", "Ricci", "cardiologo", 100.30)
ginecologo = Dottore("Stefano", "Gui", "ginecologo", 160.50)

paziente1 = Paziente("Riccardo", "Emi", "kid90")
paziente2 = Paziente("Elena", "Sarni", "fhrytu")
paziente3 = Paziente("Tommaso", "Rossi", "erthg57")
paziente4 = Paziente("Maria", "Viviani", "gfhrl01")
paziente5 = Paziente("Bianca", "Tuti", "rgh76")

lista1 = [paziente1, paziente2, paziente3]
lista2 = [paziente4]
lista3 = [paziente5]

urologo.setAge(45)
cardiologo.setAge(60)
ginecologo.setAge(80)
urologo.doctorGreet()
cardiologo.doctorGreet()
ginecologo.doctorGreet()

fattura1 = Fattura(lista1, urologo)
fattura2 = Fattura(lista2, cardiologo)
fattura3 = Fattura(lista3, ginecologo)
salario_urologo = fattura1.getSalary()
print(f"Salario urologo: {salario_urologo:.2f} euro!")
salario_cardiologo = fattura2.getSalary()
print(f"Salario cardiologo: {salario_cardiologo:.2f} euro!")
salario_ginecologo = fattura3.getSalary()
print(f"Salario ginecologo: {salario_ginecologo:.2f} euro!")

fattura1.removePatient("kid90")
fattura2.addPatient(paziente1)
fattura1.removePatient("erthg57")
fattura3.addPatient(paziente3)

fatture = [fattura1, fattura2, fattura3]
for fattura in fatture:
    salario = fattura.getSalary()
    print(salario)

guadagno_totale = 0 
for fattura in fatture:
    salario = fattura.getSalary()
    guadagno_totale += salario 
print(f"In totale, l'ospedale ha incassato: {guadagno_totale:.2f} euro!") 