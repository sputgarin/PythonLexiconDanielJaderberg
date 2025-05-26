# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

test_cases = [
    [1,1,2,3,1],
    [1,1,2,4,1],
    [1,1,2,1,2,3]
]

results = [arrayCheck(case) for case in test_cases]
print(results)

# 2. Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

def stringBits(my_string):
    return my_string[::2]

test_strings = ['Hello', 'Hi', 'Heeololeo']
results = [stringBits(s) for s in test_strings]
print(results)


# 3. Given a string, return a string where for every char in the original,
# # there are two chars. Example:
# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(my_string):
    return ''.join([char*2 for char in my_string])

print(doubleChar('Hi There'))


# 4. Return the number of even integers in the given array/list.
# Examples:
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)

test_cases = [
    [2,1,2,3,4],
    [2,2,0],
    [1,3,5]
]

results = [count_evens(case) for case in test_cases]
print(results)