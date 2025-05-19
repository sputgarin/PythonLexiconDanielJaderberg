# Not Lambda:
def timeTwo(num):
    return 2*num

# Lambda
lambda num: num*2


lst = [1,2,3,4,5,6,7,8,9,10]

# Not lambda
def evenBool(num):
    return num%2==0

evens = filter(evenBool,lst)
print(list(evens))

# Lambda
evens = filter(lambda num: num%2==0, lst)
print(list(evens))


# map(func, *iterables) –> map object
# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

values = [1,2,3,4,5]
answer = map(lambda x: x+1, values)
print((list(answer)))

x = 15
def printer():
    x = 30
    return x

print(x)
print(printer(x))
print(x)

# 1. Name assignment will create or change local names by default
# 2 Name references search (at most) four scopes, these are: (LEGB rule )
    # Local: Name assignement in any way withing a function (def or lambda) and not declared global in




def mapper(helper_func, iterable):
    result = []
    for value in iterable:
        helper_result = helper_func(value)
        result.append(helper_result)
    return result

values = [1,2,3,4,5]
result = mapper(lambda x:x-1, values)

print(list(result))

answer = map(lambda x: x+1, values)
print(list(answer))
