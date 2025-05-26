class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'


    def increase_salary(self):
        self.salary = int(self.salary * self.increase)



class Developer(Employee):

    increase = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'




emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Carl', 'Cson', 50000, 'Python')

print(emp1)
print(emp2)
print(dev1)

emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()

print(emp1)
print(emp2)
print(dev1)


# Base class
class Animal:
    def __init__(self):
        print('Animal created')

    def WhoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating..nom nom...')


# Derived class
class Dog(Animal):
    def __init__(self):
        print('Dog created')

    def WhoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof')


d = Dog()
d.WhoAmI()
d.eat()
d.bark()


class A:
    def __init__(self, value):
        print(f'In A.__init__ and value {value}')
        self.value = value

class B(A):
    def __init__(self, value):
        print(f'In B.__init__ and value = {value}')
        super().__init__(value)
        self.value += 10

class C(A):
    def __init__(self, value):
        print(f'In C.__init__ and value = {value}')
        super().__init__(value)
        self.value *= 4

class D(C, B):
    def __init__(self, value):
        print(f'In D.__init__ and value = {value}')
        super().__init__(value)

d = D(10)
print(d.value)
print(D.mro())


