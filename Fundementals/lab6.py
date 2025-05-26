# 1. Veichle Inheritance
# Create a Python program that models a hierarchy of vehicles using inheritance. Start
# with a base class Vehicle, and then create two or more derived classes (e.g., Car,
# Bicycle, Motorcycle) that inherit from the Vehicle class. Each class should have specific
# attributes and methods related to the type of vehicle it represents.
# 1. Define the Vehicle base class with common attributes such as make, model, and
# year, and methods like start(), stop(), and fuel_up().
# 2. Create derived classes for diƯerent types of vehicles, e.g., Car, Bicycle, and
# Motorcycle. Each derived class should inherit from the Vehicle base class and
# add attributes and methods specific to that type of vehicle. For example, the Car
# class might have attributes like num_doors, and the Bicycle class could have
# attributes like num_gears.
# 3. Implement specific methods for each derived class. For instance, the Car class
# might have a method to honk the horn, and the Bicycle class could have a
# method to ring the bell.
# 4. Create instances of each vehicle type and demonstrate their specific methods
# and attributes. For example, you can create a car, bicycle, and motorcycle, and
# call methods like start(), stop(), and their specific methods like honk_horn() or
# ring_bell().

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def start(self):
        print(f"Starting {self.model}")

    def stop(self):
        print(f"Stopping {self.model}")
    def fuel_up(self):
        print(f"Filling up {self.model}")

class Car(Vehicle):
    def __init__(self,make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Numbers of doors: {self.number_of_doors}"
    def honk_horn(self):
        print(f"{self.model} Honking the horn")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, number_of_gears):
        super().__init__(make, model, year)
        self.number_of_gears = number_of_gears

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Number of gears: {self.number_of_gears}"
    def ring_bell(self):
        print(f"{self.model} Ringing the bell.")

    def start(self):
        print(f"Pedaling {self.model}")

    def fuel_up(self):
        print(f"{self.model} Doesn't need fuel, it's a bike.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Sidecar: {self.has_sidecar}"

    def do_a_wheelie(self):
        print(f"{self.model} Doing a cool wheelie.")

car1 = Car("BMW", "STR9001", 1994, 2)
print(car1)
car1.start()
car1.stop()
car1.fuel_up()
car1.honk_horn()
bicycle1 = Bicycle("Impala", "T-47","1947", 24)
print(bicycle1)
bicycle1.start()
bicycle1.stop()
bicycle1.ring_bell()
bicycle1.fuel_up()
motorcycle1 = Motorcycle("Suzuki", "Ninja", 2000, False)
print(motorcycle1)
motorcycle1.start()
motorcycle1.stop()
motorcycle1.fuel_up()
motorcycle1.do_a_wheelie()



# 2. Multiple Inheritance and MRO Challenge
# Task:
# 1. Create classes X, Y, Z, each with an identify() method.
# 2. Create a class W that inherits from both X and Y.
# 3. Call the identify() method on an instance of W and print the MRO of W.
# Challenge:
# 4. Add a super() call in one of the subclasses identify() methods to observe how the
# method chaining works.


class X:
    def identify(self):
        print(f"I am X")
        super().identify()

class Y:
    def identify(self):
        print(f"I am Y")

class Z:
    def identify(self):
        print(f"I am Z")



class W(X,Y):
    def identify(self):
        print(f"I am W")
        super().identify()


w1 = W()
w1.identify()
print(W.mro())