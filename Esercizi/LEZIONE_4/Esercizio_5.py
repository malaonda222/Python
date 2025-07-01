def add_one(a:int):
    result = a+1
    return result 

def add_one_to_list(mylist:list) -> list[int, int]:
    new_list = []
    for element in mylist:
        new_list.append(add_one(element))
    print(new_list)

add_one_to_list([4, 5, 6, 7]) 
    
