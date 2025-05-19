

# Base class (superclass)
class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

# Derived class (subclass)
class Dog(Animal):
    def make_sound(self):
        return "Bau Bau!"

# Derived class (subclass)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog("Fuwawa"), Cat("Okayu")]

for animal in animals:
    print((f"{animal.name} makes sound: {animal.make_sound()}"))

class Bird:
    def make_sound(self):
        return "Chirp!"

class Dog:
    def make_sound(self):
        return "Woof"

def animal_sound(animal):
    return animal.make_sound()

bird = Bird()
dog = Dog()

print(animal_sound(bird))
print(animal_sound(dog))
print(dog.make_sound())
print(animals)

class CreditCardPayment:
    def __init__(self, amount, card_number):
        self.amount = amount
        self.card_number = card_number

    def process_payment(self):
        print(f"Processing credit card payment of {self.amount}")

class PayPalPayment:
    def __init__(self,amount, paypal_account):
        self.amount = amount
        self.paypal_account = paypal_account

    def process_payment(self):
        print(f"Processing PayPal payment of {self.amount} from account: {self.paypal_account}")

class CryptoPayment:
    def __init__(self, amount, wallet_address):
        self.amount = amount
        self.wallet_address = wallet_address

    def process_payment(self):
            print(f"Processing crypto payment of {self.amount} from account {self.wallet_address}")

def process_payment(payment):
    payment.process_payment()

credit_card = CreditCardPayment(100, "1234-5678-9101-1123")
paypal = PayPalPayment(200, "user@example.com")
crypto = CryptoPayment(0.05, "abcdef123xyz456crypto")

for payment_method in [credit_card, paypal, crypto]:
    process_payment(payment_method)

#
from math import sqrt
print(sqrt(20))

#
import math
print(math.sqrt(25))

def sqrt(x):
    return "hello"

print(sqrt(25)) # Does not get overridden
print(math.sqrt(25)) # Gets overridden

from math import sqrt as sq

print(sq(25)) # Use an alias for sqrt.




