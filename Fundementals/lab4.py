# 	 1.Write a lambda function to calculate the square of a number.
x = lambda a : a ** 2
print(x(5))

# inline test
print((lambda a: a**2)(4))



# 	 2.Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.

lst = [1,2,3,4,5,6,7,8,9,10]
def return_square_list(helper_func, my_number_list):
    result = []
    for num in my_number_list:
        helper_result = helper_func(num)
        result.append(helper_result)
    return result
result = return_square_list(lambda a : a ** 2, lst)
print(result)

# 	3.Write a function that returns a list of prime numbers up to a given number using lambda.
#Without lambda, get my bearings.
def is_prime_regular(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime_regular(4))

# With Lambda
def is_prime_lambda_helper(n):
    result = []
    for num in range(2, n + 1):
        if(lambda x: is_prime_regular(x))(num):
            result.append(num)
    return result

print(is_prime_lambda_helper(10))
print(is_prime_lambda_helper(5))
print(is_prime_lambda_helper(2))





# 	4. Write a program that modifies a global variable inside a function
x = 5
def add_numbers(a,b):
    global x
    x =  a + b
    return x

print(add_numbers(10,10))
print(x)



# 	5. Create a program that defines a function within another function and access variables from the outer function.
# 	(Often called Enclosing Scope)

def first_func():
    x = 10
    def second_func():
        print(x)
    second_func()
first_func()


# 	6. Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.

y = 10
def funky_func():
    y=3
    print(f"local is {y}")
funky_func(y)
print(f"global y is {y}")

