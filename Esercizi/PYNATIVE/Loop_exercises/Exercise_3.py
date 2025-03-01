# Calculate sum of all numbers from 1 to a given number

# chiedere all'utente di inserire un numero
number = int(input("Enter number: "))

sum = 0
for x in range(1, number+1):
    sum+=x
print(f"The sum of the numbers between 1 and {number} is: {sum}")


sum = 0 
i = 1
number_1 = int(input("Enter a number: "))
while i <= number_1:
    sum+=number_1
    i+=1
print(f"The sum of the numbers between 1 and {number_1} is: {sum}")
      
