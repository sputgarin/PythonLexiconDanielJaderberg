l = [1,2,3]

print(type(l))

class Sample():
    pass
# The pass statement
# pass_stmt ::=  "pass"
# pass is a null operation — when it is executed, nothing happens.
# It is useful as a placeholder when a statement is required syntactically,
# but no code needs to be executed, for example:

x = Sample()

print(type(x))

class Dog():
    # class object attributes:
    species = 'mammal'
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

    def __str__(self):
        return f'{self.name} the {self.breed}'
    def __repr__(self):
        return self.name


milo = Dog(breed='Labrador', name='Milo')
frank = Dog(breed='Huskie',name='Frank')

print(milo.name)
print(milo.breed)
print(frank.name)
print(frank.breed)

dog_list = [milo,frank]
print(dog_list)
print(milo.species)

for dog in dog_list:
    print(dog)

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

c = Circle()
c.setRadius(2)
print('Radius is:', c.getRadius())
print('Area is: ',c.area())

class Person:
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old and has email {self.email}'

p1 = Person('Alice', 'alice@email.com', 34)
p2 = Person('Bob', 'Bob@email.com', 35)

print(p1)
print(p2)

p1.phone = '072123'
print(p1.phone)
# print(p2.phone) Gives error since it is not assigned


class PersonNew:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

p1 = PersonNew(name = 'Alice', age = 23)
p2 = PersonNew(name = 'Bob', age = 25)
print(p1)
print(p2)


class Something:
    def __init__(self, data:dict):
        self.__dict__= data

    def __str__(self):
        # Rewrite 4 lines as comprehension
        #str_rep = '' # Where available info will go
        #for key, value in self.__dict__.items():
        #    str_rep += f'{key} = {value}'
        #return str_rep
        return ''.join(f'{key} = {value}' for key, value in self.__dict__.items())

data_dict1 = {
    'a' : 10,
    'b' : 20,
    'name' : 'One'
}

data_dict2 = {
    'c' : 15,
    'd' : 25,

}

s1 = Something(data_dict1)
s2 = Something(data_dict2)

print(s1)
print(s2)





my_little_list = [1,2,3]
print(my_little_list)











