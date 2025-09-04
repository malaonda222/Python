'''Usa la classe Libreria che hai appena creato.
Crea tre istanze diverse della classe, con nomi e generi differenti.
Chiama il metodo descrivi_libreria() per ciascuna istanza.'''

from esercizio1_libreria import *

libreria1 = Libreria("Binario10", "Fantasy")
libreria2 = Libreria("NottiMagiche", "Fantascienza")
libreria3 = Libreria("Sognando", "Poetica")

libreria1.descrivi_libreria()
libreria2.descrivi_libreria()
libreria3.descrivi_libreria()
