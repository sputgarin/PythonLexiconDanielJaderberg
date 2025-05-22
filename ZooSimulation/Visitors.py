# Visitors: A class to represent the visitors in the park, with attributes like name and age.
class Visitors:
    def __init__(self,name,age,happiness):
        self.name = name
        self.age = age
        self.happiness = happiness

    def feed_animal(self,other):
        return f"{self.name} is trying to feed {other}"

    def pet_animal(self,other):
        return f"{self.name} reach out to pet {other}"

    def look_at_animal(self,other):
        return f"{self.name} looked at {other}"

    def adjust_happiness(self, amount):
        self.happiness = max(0, min(100, self.happiness + amount))


