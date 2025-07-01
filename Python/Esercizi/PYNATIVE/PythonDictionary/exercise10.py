employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees, defaults)
print(result)
print(result["Emma"])