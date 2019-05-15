my_list = [0, 'one', 2.0, 3, 4]

print("type ", type(my_list))
print(my_list)

for elem in my_list:
    print(elem, end=' ')
print()

for index in range(len(my_list)):
    print(my_list[index], end=' ')
print()

for elem in reversed(my_list):
    print(elem, end=', ')
print()

print("in the reverse order")
for elem in my_list[::-1]:
    print(elem, end=' ')
print()

my_list_2 = my_list
my_list.insert(1, -3)
my_list.append(5)
print('mylist2', my_list_2)

mylist3 = my_list.copy()
# above is the same as mylist3 = mylist[:]
mylist3.append(6)
print("mylist3", mylist3)
print("mylist2", my_list_2)

mylist3.remove('one')
print("mylist3", mylist3)
mylist3.reverse()
print("mylist3", mylist3)
# Extending using iterables: list, tuples, strings ,etc
mylist3.extend((100, 101, 102))
print("mylist3 extended", mylist3)

print('mylist3 + mylist2', mylist3 + my_list_2)
print('mylist3 * 2', mylist3 * 2)

# min, max, len, sort
print("mylist3 min", min(mylist3))
print("mylist3 max", max(mylist3))
print("mylist3 len", len(mylist3))
mylist3.sort()  # in place operation
print("mylist3 sorted", mylist3)
print("mylist3 sum", sum(mylist3))

mylist3.extend((100, 101, 102))
print("mylist3 extended", mylist3)

del mylist3[0]
print("del mylist3[0]", mylist3)

persons = [
    ["Sonia", "Guerrero", 22],
    ["Shane", "Mcguire", 43]
]

print("persons[1][0]", persons[1][0])

# List comprehension expressions
mylist4 = [x + 2 for x in range(0, 20)]
print("First names: ")
[print(elem[0]) for elem in persons]
print("mylist4", mylist4)
