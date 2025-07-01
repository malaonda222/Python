# my_dict = {"sasso": 1, "carta": 2, "forbice": 3}

# # print(my_dict["sasso"])
# # print(my_dict["carta"])
# # print(my_dict["forbice"])

# for value in my_dict.values():
#     print(value)

# for key in my_dict.keys():
#     print(key)

# for key, value in my_dict.items():
#     print(key, value)


# my_dict["altalena"] = 4
# print(my_dict)

# my_dict.pop("altalena")
# print(my_dict)

list1 = [1, 2] #due puntatori con due puntatori diversi
list2 = [1, 2]

list3 = list2
list3.pop(0)
print(list2)

list2 = list3.copy()
list2.append(10)
print(list2, list3)

