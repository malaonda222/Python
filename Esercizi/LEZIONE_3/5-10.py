# Checking Usernames
current_users = ["Marco", "Lucia", "Sabina", "Filippo", "Riccardo"]
new_users = ["Lucia", "Riccardo", "Giuseppe", "Lapo", "Edoardo"]

new_current_users = [user.lower() for user in current_users]

for user in new_users:
    if user in new_current_users:
        print(f"{user}, please insert a new username")
    else:
        print(f"The username {user} is available")




