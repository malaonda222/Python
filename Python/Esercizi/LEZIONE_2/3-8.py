#Seeing the World
my_list = ["China", "Thailand", "Japan", "Kenya", "Maldives"]
print(my_list)

my_list_sorted = sorted(my_list)
print(my_list_sorted)

my_list_sorted_reverse = sorted(my_list_sorted, reverse = True)
print(my_list_sorted_reverse)

my_list_2 = my_list[:]
my_list_2.reverse()
print(my_list_2)

my_list_3 = my_list_2[:]
my_list_3.reverse()
print(my_list_3)

my_list_4 = my_list[:]
my_list_4.sort()
print(my_list_4)

my_list_5 = my_list_4[:]
my_list_5.sort(reverse = True)
print(my_list_5)

