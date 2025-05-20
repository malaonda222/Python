from persona import Persona 
from alieno import Alieno 

# creare un oggetto p della classe Persona 
p: Persona = Persona("Lisa", "Bandinelli", 26)
#visualizzare le informazioni relative alla Persona p
print(p)

#creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")
#visualizza le informazioni relative all'alieno et
print(et)

#oggetto p invoca il metodo speak (Persona)
p.speak()
#oggetto et invoca il metodo speak (Alieno)
et.speak()




