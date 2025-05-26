# 1 Given the string
s = "Python"
print(s[4])
print(s[:4])
print(s[1:4])
print(s[1:] + s[:1])

print('\n')

# 2 Given the nested list:
l = [3, 7, [1, 4, 'hello']]
l[2][2] = "goodbye"
print(l)

# 3 Using keys and indexing, grab the 'hello from the following dictionaries:
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

print('\n')
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
print('\n')

# 4 Use a set to find the unique values of the list below
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
u_value = set(mylist)
print(u_value)
print('\n')

# 5 You are given two variables, use print formatting to print the following string.
age = 4
name = "Sammy"
print(f"\"Hello my dog's name is {name} and he is {age} years old.\"")




