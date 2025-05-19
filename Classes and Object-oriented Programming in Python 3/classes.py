class Employee:
    def __init__(self,name,age,position,salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return(f"{self.name} is {self.age} years old. Employee is a {self.position} "
              f"with the salary of ${self.salary}")

    def __repr__(self):
        return (f"Employee("
                f"{repr(self.name)}, {repr(self.age)}, "
                f"{repr(self.position)}, {repr(self.salary)})"
                )

e1 = Employee('Ji-Soo', 38,'Developer', 1200)
e2 = Employee('Laura', 25,'QA', 120)

print(str(e1))
print(repr(e1))
print(eval(repr(e1)))
print(e1.__class__)



