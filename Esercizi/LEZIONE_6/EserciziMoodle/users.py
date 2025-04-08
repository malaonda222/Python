class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"\nFirst name: {self.first_name}\nLast name: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}")
    
    def greet_user(self):
        print(f"Ciao {self.first_name}, how you're doing?")


class Privileges:
    def __init__(self, privileges_list:list=None):
        if privileges_list is None:
            privileges_list = []
        self.privileges = privileges_list

    def show_privileges(self):
        if self.privileges:
            print(f"The privileges for the user are {self.privileges}.")
        else:
            print("Nessun privilegio assegnato.")

class Admin:
    def __init__ (self, user, privileges):
        self.user = user 
        self.privileges = privileges 

    def describe_admin(self):
        return self.user.describe_user()
    
    def show_admin_privileges(self):
        return self.privileges.show_privileges()
    

        
