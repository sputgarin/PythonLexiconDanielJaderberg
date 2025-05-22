# Basic objects: Animal
# Animal: The base class for all types of animals, common attributes may include:
# name,age,and energy level, basic methods might be: eat, sleep, make sound.
# Herbivores and carnivores: Subclasses that inherit from Animal, with specific characteristics and behaviors.

class Animals:
    def __init__(self,name,age,hunger,happiness,energy):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.dead = False

    def clamp_stats(self):
        self.hunger = max(0, min(100,self.hunger))
        self.energy = max(0, min(100,self.energy))
        self.happiness = max(0, min(100,self.happiness))
    def make_sound(self):
        return f"The animal makes an audible sound."

    def eat(self):
        return f"The animal is eating"

    def sleep(self):
        return f"The animal is sleeping"

    def is_dead(self):
        if self.hunger <= 0 and not self.dead:
            self.dead = True
        return self.dead

class Herbivore(Animals):
    def __init__(self, name,age, hunger, happiness,energy):
        super().__init__(name,age, hunger, happiness, energy)
        self.carnivore = False

    def eat(self):
        return "The animal eats some insects-spray poisoned plants, all in good health."

class Carnivore(Animals):
    def __init__(self, name,age, hunger, happiness,energy):
        super().__init__(name,age, hunger, happiness, energy)
        self.carnivore = True

    def eat(self):
        return "The animal eats a warm juicy steak wrapped in bacon."


class Giraffe(Herbivore):
    def __init__(self,name, age, hunger, happiness,):
        super().__init__(name,age, hunger,happiness,energy=100)
        self.animal_type = "Giraffe"
    def make_sound(self):
        return(f"Giraffe makes a Giraffe sound something like hmmmmm.")

    def eat(self):
        return f"The Giraffe is eating the leaves your park attendants left on the ground"
    def sleep(self):
        return f"The Giraffe is sleeping"

class Antilope(Herbivore):
    def __init__(self,name, age, hunger, happiness):
        super().__init__(name,age, hunger,happiness,energy=100)
        self.animal_type = "Antilope"
    def make_sound(self):
        return(f"Antilope makes a  sound!\n")

    def eat(self):
        return f"The Antilope is eating the leaves your park attendants left on the ground"
    def sleep(self):
        return f"The Antilope is sleeping"

class Lion(Carnivore):
    def __init__(self,name, age, hunger, happiness):
        super().__init__(name,age, hunger,happiness,energy=100)
        self.animal_type = "Lion"
    def make_sound(self):
        return(f"The lion roars magestically, making small children cry")

    def eat(self):
        return f"The lion is eating the carcass of a more insignificant animal.\nCircle of life and all that."

    def sleep(self):
        return f"The lion is sleeping"

class Tiger(Carnivore):
    def __init__(self,name, age, hunger, happiness):
        super().__init__(name,age, hunger,happiness,energy=100)
        self.animal_type = "Tiger"
    def make_sound(self):
        return(f"The tiger roars magestically, making small children cry")

    def eat(self):
        return f"The Tiger is eating the carcass of a more insignificant animal.\nCircle of life and all that."

    def sleep(self):
        return f"The Tiger is sleeping"
