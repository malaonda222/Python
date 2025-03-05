# def check_value(num):
#     if num>5:
#         print(f"{num} is greater than 5")
#     elif num<5:
#         print(f"{num} is smaller than 5")
#     else:
#         print(f"{num} is equal to 5")

    

'''Write a function check_value(), which takes a number as an argument. 
Using if/else, the function should print whether the number is bigger, smaller, or equel to 5.'''
a:int = 5
def check_value(a:int):
    if a>5:
        print(f"{a} is greater than 5")
    elif a<5:
        print(f"{a} is smaller than 5")
    else:
        print(f"{a} is equal to 5")

check_value(int(input(f"Insert a number: ")))