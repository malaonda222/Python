list1:list = [1, 2, 3, 4, 5]
#1 modo
#for i in range(0, len(list1))
#oppure
print("Modo I")
for i in range(len(list1)):
    print(f"{list1[i]}")
    
#2 modo
print("Modo II:")
for item in list1:
    print(item)

print("Modo III:")   
list2:list = [1, True, 0.5, {}]
for i in range(len(list2)):
    print(f"{list2[i]}")
    
print("Modo III")
list2:list = [1, True, 0.5, {}]
for i in list2:
    print(item)
