from operator import itemgetter

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

sorted_items = sorted(my_dict.items(), key=itemgetter(1))
sorted_dict = dict(sorted_items)

for key, value in sorted_dict.items():
    print(f"{key}: {value}")