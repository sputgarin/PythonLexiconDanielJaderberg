class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f'Point x = {self.x}'
                f': y = {self.y}')

    def __str__(self):
        return f"Point object with x = {self.x} and y = {self.y}"

    def __eq__(self, other): # Will make it possible to compare point 1 and point 2
        return self.x == other.x, self.y == other.y

    def swap_xy(self):
        self.x, self.y = self.y, self.x

    def swap_points(self,other):
        self.x, self.y = other.x, other.y


point1 = Point(10,20)
point2 = Point(5,0)

print(point1.x, point1.y)
print(point1) # prints __str__
print((repr(point1))) # prints __repr__

print(point1 == point2) # Needs a dunder method to be able to compare, see above.

point1.swap_xy()
print(point1)

point1.swap_points(point2)
print(point1)


class A:
    def __init__(self,value):
        print(f"In A.__init__ and value {value}")
        self.value = value

class B(A): # Using inherit to get everything from class A
    def __init__(self,value):
        print(f"In b __init__ and value = {value}")
        self.value = value
        self.value += 10

#
class C(A):
    def __init__(self,value):
        print(f"f'In C.__init__ and value = {value}")
        super().__init__(value)
        self.value *= 4

class D(B,C):
    def __init__(self,value):
        print(f'In D.__init__ and value = {value}')
        super().__init__(value)


d = D(10)
print(d.value)
print(D.mro())

#MRO

print("\n")

# Base class
class Animal:
    def __init__(self):
        print("Animal created")

    def WhoAmI(self):
        print('Animal')

    def eat(self):
        print("Eating...")

    def roar(self):
        print("Hear me roar")

# Derived class
class Dog(Animal):
    def __init__(self):
        print("Dog created")
    def WhoAmI(self):
        print("DOG")

    def bark(self):
        print("BAO BAO! Protecting your smiles since forever!")
d = Dog()
d.WhoAmI()
d.eat()
d.bark()



class Employee:
    increase = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.salary}"

    def increase_salary(self):
        self.salary = int(self.salary * self.increase)

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary) # Super is what we want to inherit from Employee base class
        self.programming_language = programming_language
    def __str__(self):
        return f"{super().__str__()} {self.programming_language}"

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bobson', 35000)
dev1 = Developer('Carl', 'Cson', 50000, 'C#')

print(emp1)
print(emp2)
print(dev1)
dev1.increase_salary()
print(dev1)

