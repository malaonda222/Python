from animale import Animale

cane:Animale = Animale("cane", "Labrador", 4, "marrone")
print(cane)

print(cane.nome, cane.razza, cane.zampe, cane.colore, sep=", ")

from animale2 import Animale2
anl:Animale2 = Animale2()

anl.displayData()

print("------------")

anl.setName("cane")
anl.setRace("Pastore tedesco")
anl.setPaw(4)
anl.setColour("Nero")

anl.displayData()

print(anl.getName(), anl.getRace(), anl.getPaw(), anl.getColour(), sep= ", ")