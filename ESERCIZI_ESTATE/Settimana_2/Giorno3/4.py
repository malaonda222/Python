'''Scrivi una funzione sono_anagrammi(s1: str, s2: str) -> bool che restituisce True 
se le due stringhe sono anagrammi (contengono gli stessi caratteri con la stessa frequenza), altrimenti False.'''

def sono_anagrammi(s1: str, s2: str) -> bool:
   s1 = s1.replace(" ", "").lower()
   s2 = s2.replace(" ", "").lower()

   frequenza1 = {}
   frequenza2 = {}
   for element in s1:
      if element not in frequenza1:
         frequenza1[element] = 1
      else:
         frequenza1[element] += 1
   
   for element in s2:
      if element not in frequenza2:
         frequenza2[element] = 1
      else:
         frequenza2[element] += 1
   
   if frequenza1 == frequenza2:
      return True
   else:
      return False
        
    
print(sono_anagrammi("roma", "amor"))


def sono_anagrammi2(s1: str, s2: str) -> bool:
   s1 = s1.replace(" ", "")
   s2 = s2.replace(" ", "")

   frequenza1 = {carattere: s1.count(carattere) for carattere in set(s1)}
   frequenza2 = {carattere: s2.count(carattere) for carattere in set(s2)}

   return frequenza1 == frequenza2

print(sono_anagrammi2("amor", "roma"))


      