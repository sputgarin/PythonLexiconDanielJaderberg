def my_function():
    print("Func")


my_function()


def any_name(parameter='default'):
    """
    Comment
    """
    print((parameter))


any_name()


def hello():
    print('hello')


hello()


def giveMeHello():
    return 'hello you'


print(giveMeHello())
res = giveMeHello()
print(res)


def evenCheck(number):
    if number % 2 == 0:
        return ('even number')
    else:
        return ("odd number")


print(evenCheck(1))


def evenCheck2(number):
    print((number % 2 == 0))


evenCheck2(11)


def helloYou(name='Johnny'):
    return('Hello ' + name)
resul = helloYou("Pelle")
print(resul)


def addEvenNumbersOnly(num1,num2):
    if (num1 % 2 != 0) or (num2 % 2 != 0):
        return False
    else:
        return num1 + num2

x = addEvenNumbersOnly(1,2)
y = addEvenNumbersOnly(2,4)

print(x)
print(y)

def func(a,b,c=10,d=11):
    print(a,b,c,d)

func(1,2,)
func(1,2,3)
func(1,2,3,4)
func(c='c', a='a', d='d', b='b')
func(1,2,d=4)

# Pass any number of arguments, arg becomes am immutable tuple where you can't add anything
def funky_func(*args):
    print(args)

funky_func()
funky_func(1,2)
funky_func(1,2,3)

# Kwargs uses double asterix. it created keyword arguments
def func2(a, b, **kwargs):
    print(a,b, kwargs['c'], kwargs['d'])
    #print(kwargs)

# Crating a c and d as keyword arguments. IT has now created a dictionary that can be accessed.
func2(1,2,c=14, d=19)


# An if statment prevents the crash if one of the kwargs are missing, in this case func3 does not use the d argument.
def funcA(a,b,**kwargs):
    print(a,b,)
    if'c' in kwargs:
        print(kwargs['c'])
    if 'd' in kwargs:
        print(kwargs['d'])
funcA(8,9, c=14)


def func3(a,b,*args,name='John', **kwargs):
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('args = {}'.format(args))
    print('name = {}'.format(name))
    print('kwargs = {}'.format(kwargs))

# In this case it will add jojje to the tupple instead. so you have to be careful when adding the arguments.
# To change name use name=jojje
func3(1,2, 3,'jojje', age=33, email='jojje@cyberrymden.nu')


# * Tupple
# ** Dictionary





















