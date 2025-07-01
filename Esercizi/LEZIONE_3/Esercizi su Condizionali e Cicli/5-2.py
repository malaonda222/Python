# More Conditional Tests

#Test for equality and inequality with strings

print("TEST FOR EQUALITY AND INEQUALITY WITH STRINGS:")
dog = "Teo"
print("Is dog == Teo? I predict is True.")
print(dog == "Teo")

print("Is dog == Tobia? I predict is False.")
print(dog == "Tobia")

print("Is dog != Otto? I predict is True.")
print(dog != "Otto")

#Tests using the lower() method

print("TEST USING THE LOWER() METHOD:")
name = "Lisa"
print("Is name.lower() == Lisa? I predict is False.")
print(name.lower() == "Lisa")

print("Is name.lower() == lisa? I predict is True.")
print(name.lower() == "lisa")

print("Is name.lower() != Mario? I predict is True.")
print(name.lower() != "Mario")

#Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to

print("NUMERICAL TESTS")

x = 10
y = 25

print("Is x == y? I predict is False.")
print(x == y)

print("Is x != y? I predict is True.")
print(x != y)

print("Is x > y? I predict is False.")
print(x > y)

print("Is x < y? I predict is True.")
print(x < y)

a = 100
b = 99

print("Is a >= b? I predict is True.")
print(a >= b)

print("Is a <= b? I predict is False.")
print(a >= b)

print("Is a != b? I predict is True.")
print(a != b)

# Tests using the and keyword and the or keyword
print("TEST USING THE AND KEYWORD AND THE OR KEYWORD:")

age_Lisa = 26
age_Marco = 36
age_Miriam = 18

print("Is age_Lisa < age_Marco and age_Lisa > age_Miriam? I predict is True.")
print(age_Lisa < age_Marco and age_Lisa > age_Miriam)

print("Is age_Marco < age_Miriam or age_Marco > age_Lisa? I predict is True.")
print(age_Marco < age_Miriam or age_Marco > age_Lisa)

print("Is age_Miriam > age_Lisa or age_Lisa > age_Marco? I predict is False.")
print(age_Miriam > age_Lisa or age_Lisa > age_Marco)

print("Is age_Marco > age_Miriam and age_Marco < age_Lisa? I predict is False.")
print(age_Marco > age_Miriam and age_Marco < age_Lisa)

#Test whether an item is in a list
print("TEST WHETHER AN ITEM IS IN A LIST:")

my_list:list = ["a", "2", "c", "4", "e"]

print("Is b in my_list? I predict is False.")
print('b' in my_list)

print("Is 3 in my_list? I predict is True.")
print(3 in my_list)

print("Is c in my_list? I predict is True.")
print('c' in my_list)

#Test whether an item is not in a list
print("TEST WHETHER AN ITEM IS NOT IN A LIST:")

list1:list = ["cactus", "orchidea", "penna", "a", "foglio"]

print("Is b not in list1? I predict is True.")
print("b" not in list1)

print("Is cactus not in list1? I predict is False.")
print("cactus" not in list1)