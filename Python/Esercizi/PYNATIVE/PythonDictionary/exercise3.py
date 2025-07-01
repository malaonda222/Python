keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {}
for i in range(len(keys)):
    my_dict.update({keys[i] : values[i]})
print(my_dict)

