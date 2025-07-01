# Slide 24
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name} {self.age}"

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Eta di Bob: {bob.age}")
      

if alice.age > bob.age:
    print(f"La persona più grande è: {alice.age}")
else: 
    print(f"La persona più grande è: {bob.age}")
    
lisa = Person("Lisa B.", 26)
nico = Person("Nico V.", 36)
gianni = Person("Gianni L.", 30)


lista1 = [alice, bob, nico, gianni, lisa]
min_age = lista1[0]
for item in lista1: 

    if item.age < min_age.age:
        min_age = item
    
print(f"La persona più giovane è: {min_age}")






