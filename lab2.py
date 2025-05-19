# 1 Write a program that takes two integers as input, base and exponent, and calculates the power using loops

def calculate_power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return (result)

print(calculate_power(int(input("Enter base:\n")),int(input("Enter exponent:\n"))))


# 2 Write a program that calculates the sum of all elements in a given tuple
def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total = total+i

    return (total)

print(calculate_sum((1,2,3)))
print(calculate_sum((4,5,6)))


# 3 Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
def create_evennumber_tuple(numbers):
    even_tuple = ()
    for tuple_content in numbers:
        if tuple_content % 2 == 0:
            even_tuple = even_tuple + (tuple_content,)

    return (even_tuple)

print((create_evennumber_tuple((1,2,3,4,5,6,7,8,9,10))))
print(create_evennumber_tuple((1,3,5)))

# 4 Write a program that merges two dictionaries into a single dictionary.
# If a key is common to both dictionaries, the value from the second dictionary should be used.
def merge_dicts(dict1, dict2):
        merged_dict = {}
        for key in dict1:
            merged_dict[key] = dict1[key]

        for key in dict2:
            merged_dict[key] = dict2[key]

        return (merged_dict)
print(merge_dicts({"brand": "Ford","model": "Mustang","year": 1964},
    {"brand": "Ford", "type": "Bike", "year": 1966}
))


# 5  Write a program that takes a list of integers as input and uses list comprehension to create a new
# list containing only the even numbers from the original list.
def create_list_listcomprehension(numbers):
    return ([num for num in numbers if num % 2 == 0])

print(create_list_listcomprehension([1,2,3,4,5,6,7,8,9,10]))
print(create_list_listcomprehension([1,3,5]))



# 6 Write a program that takes a string as input and prints its reverse.
def reverse_string(string):
    return string[::-1]

print(reverse_string("MyLittleTestString"))
print(reverse_string("Hello"))


# 7. You are given a list called my pairs. This list contains several tuples, and each tuple holds exactly 10 integers.
def print_pairs_manual(pairs):
        for item1,item2,item3,item4,item5,item6,item7,item8,item9,item10 in pairs:
            print(item1)
            print(item2)
            print(item3)
            print(item4)
            print(item5)
            print(item6)
            print(item7)
            print(item8)
            print(item9)
            print(item10)
def print_pairs_nested(pairs):
    for tuple in pairs:
        for value in tuple:
            print(value)

my_pairs = [(1,2,3,4,5,6,7,8,9,10),(11,12,13,14,15,16,17,19,20,21), (22,23,24,25,26,27,28,29,31,32)]
print("Manual Unpack\n")
print_pairs_manual(my_pairs)
print("Nested Loop Unpack\n")
print_pairs_nested(my_pairs)


