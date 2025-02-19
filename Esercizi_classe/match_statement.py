#insert a number
n:int = int(input("Insert Finishing Position: "))

#check inserted number and return the position in cardinal form

#if n = 1
if n == 1:
    print(f"{n}st!")

#elif = 2
elif n == 2:
    print(f"{n}nd!")
    
#elif n = 3
elif n == 3:
    print(f"{n}rd!")
    
#else
else:
    print(f"{n}th!")

#insert a number
n:int = int(input("Insert Finishing Position: "))

#check inserted number and return the position in cardinal form

#match statement
match n:
    #n = 1 
    case 1:
        print(f"{n}st!")
    
    #n = 2
    case 2:
        print(f"{n}nd!")
    
    #n = 3
    case 3:
        print(f"{n}rd!")
    
    #default case
    case _:
        print(f"{n}th!")


http_status=200

match http_status:
    case 200|201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not found")
    case 500|501:
        print("Server Error")
    case _:
        print("Unknown")