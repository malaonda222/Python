# Hello Admin
my_list = ["admin", "Sarah", "Victoria", "Jaden", "Eric"]
print(my_list)

for name in my_list:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")


