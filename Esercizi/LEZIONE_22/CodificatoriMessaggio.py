from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass 

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass 

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave = chiave 
    
    def _spostacarattere(self, c: str, direzione: int) -> str:
        if c in ascii_lowercase:
            alfabeth = ascii_lowercase
        if c in ascii_uppercase:
            alfabeth = ascii_uppercase
        else:
            return c 
        
        indice_element = alfabeth.index(c)
        nuovo_indice = (indice_element + direzione * self.chiave) % 26
        return alfabeth[nuovo_indice]
    
    def _decodifica_carattere(self, c: str, direzione: int) -> str:
        if c in ascii_lowercase:
            alfabeth = ascii_lowercase
        if c in ascii_uppercase:
            alfabeth = ascii_uppercase
        else:
            return c 
        
        indice_element = alfabeth.index(c)
        nuovo_indice = (indice_element - direzione * self.chiave) % 26
        return alfabeth[nuovo_indice]

    def codifica(self, testoInChiaro: str) -> str:
        testo_cifrato = ""
        for c in testoInChiaro:
            testo_cifrato += self._spostacarattere(c, 1) 
        return testo_cifrato 

    def decodifica(self, testoCodificato: str) -> str:
        testo_decodificato = ""
        for c in testoCodificato:
            testo_decodificato += self._spostacarattere(c, -1)
        return testo_decodificato
    
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n = n 

    def _combinazione(self, testo: str) -> str:
        meta = (len(testo) + 1) // 2
        prima_meta = testo[:meta]
        seconda_meta = testo[meta:]
        mex_combinato = []
        for i in range(len(prima_meta)):
            mex_combinato.append(prima_meta[i])
            if i < len(seconda_meta[i]):
                mex_combinato.append(seconda_meta[i])
        return ''.join(mex_combinato)
    
    def decodifica_combinazione(self, testo: str) -> str:
        prima = []
        seconda = []
        meta = (len(testo + 1)) // 2
        for i in range(len(testo)):
            if i % 2 == 0:
                prima.append(testo[i])
            else:
                seconda.append(testo[i])
        return ''.hin(prima + seconda)

    def codifica(self, testoInChiaro: str) -> str:
        mex_combinato = testoInChiaro
        i = 0
        while i < self.n:
            mex_combinato = self._combinazione(mex_combinato)
            i += 1
        return mex_combinato
    
    def decodifica(self, testoCodificato: str) -> str:
        mex_combinato = testoCodificato
        i = 0
        while i < self.n:
            mex_combinato = self._decombinazione(mex_combinato)
            i += 1
        return mex_combinato
    
