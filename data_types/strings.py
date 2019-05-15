s = 'my string in python'
# sequence operations with []

print(s[1:5])
print(s[-1])
print(s[5:-3])
print(s[12:-12])

# concatenation and repetition sequence operations
print(s + " new sequence")
print(s)  # unchanged
print('A' * 10)

print(list(s))
for char in s:
    # python 2: from __future__ import print_function
    print(char, end=' ')

# s[0] = "a" will not work because strings are immutable
# other inmutable data types are tuples, numbers, strings
# lists, dictionaries and sets are not inmutable so ...
print()
string_as_list = list(s)
string_as_list[3] = 'Introduced'
print(string_as_list)
for char in s:
    print(char, end=' ')
print()
print(''.join(string_as_list))

# find() is like index() but index raises an Exception if it does find the sequence
print(s.find('y'))
print(s.find('y', 2))
print(s.title())
print(s.upper())
print(s.split(' '))  # returns a list of elements after splitting by space
print(s.count('python'))  # how many ocurrences
print(len(s))
print(s.replace('python', 'java'))

first_name = "Melar"
last_name = "Dev"
print('First Name: %s, Last Name %s' % (first_name, last_name))

print('First Name: {}, Last Name {}'.format(first_name, last_name))
print('Banana\tApple\nOnion\tMinner\'s lettuce')
