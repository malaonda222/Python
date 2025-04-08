from users import User, Privileges, Admin

dario = User("Dario", "Cirri", "da_ci", "daci@hotmail.com")

privileges1 = Privileges(["I can add a post", "I can do this correction"])

admin1 = Admin(dario, privileges1)

admin1.describe_admin()
admin1.show_admin_privileges()