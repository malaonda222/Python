# Print all prime numbers within a range
start = 25
end = 50
print(f"I numeri primi tra {start} e {end} sono: ")

for item in range(start, end + 1):
    if item>1:
        for i in range(2, item):
            if (item % i) == 0: 
                break
        else:
            print(item)

