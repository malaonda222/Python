'''Rimuovere tutte le occorrenze di un elemento specifico da un elenco'''

list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_values(sample_list, val):
    return [i for i in sample_list if i != val]
result = remove_values(list1, 20)
print(result)

while 20 in list1:
    list1.remove(20)
print(list1)