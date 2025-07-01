# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list1_reverse = reversed(list1)
for item in list1_reverse:
    print(item)

list2 = [10, 20, 30, 40, 50]
lunghezza = len(list2) -1
for i in range(lunghezza, -1, -1):
    print(i)
