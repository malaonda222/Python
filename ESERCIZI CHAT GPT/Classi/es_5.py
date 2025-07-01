class Employee:
    total_employees = 0
    total_salary = 0

    @classmethod
    def add_employees(cls, salary:float):
        cls.total_employees += 1
        cls.total_salary += salary

    @classmethod
    def get_average_salary(cls):
        if cls.total_employees == 0:
            return 0
        else:
            return cls.total_salary / cls.total_employees


Employee.add_employees(1200)
Employee.add_employees(3000)
Employee.add_employees(1500)
Employee.add_employees(1700)

print(f"La media degli stipendi degli impiegati inseriti è: {Employee.get_average_salary()}")