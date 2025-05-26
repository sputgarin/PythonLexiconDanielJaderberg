# Method Overriding

class Car:
    def drive(self):
        return "Driving a generic car"

class Sedan(Car):
    def drive(self):  # Overrides Car’s drive()
        return "Cruising at 60 mph"

# Test overriding
sedan = Sedan()
print(sedan.drive())  # Cruising at 60 mph

# Polymorphism

class Car:
    def drive(self):
        return "Driving a generic car"

class Sedan(Car):
    def drive(self):  # Overrides
        return "Cruising at 60 mph"

class SportsCar(Car):
    def drive(self):  # Overrides
        return "Zooming at 120 mph"

# Test polymorphism
cars = [Sedan(), SportsCar()]
for car in cars:
    print(car.drive())  # Calls Sedan or SportsCar’s drive()

# Duck Typing
class Sedan:
    def drive(self):  # No parent class
        return "Cruising at 60 mph"

class SportsCar:
    def drive(self):  # No parent class
        return "Zooming at 120 mph"

class Truck:  # Not even a car, but has drive()
    def drive(self):
        return "Hauling at 40 mph"

def drive_vehicles(vehicles):
    for vehicle in vehicles:
        print(vehicle.drive())  # Calls drive() if it exists

# Test duck typing
vehicles = [Sedan(), SportsCar(), Truck()]
drive_vehicles(vehicles)