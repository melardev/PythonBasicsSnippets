mytuple = (1.28, 2.901, 4, 5, 4, 5, 6)
print(type(mytuple))

print(mytuple[0])

print(mytuple.count(4))
print(mytuple.index(4))

# mytuple[1] = 7 will not work, tuples are immutable
my_tuple_from_list = tuple(['apple', 'mango', 'kiwi'])
print(my_tuple_from_list)


for elem in mytuple:
    print(elem)

coordinates = [(2.325,2.11), (1.06,6.545), (8.121,8.090)]
for x,y in coordinates:
    print("(%f, %f)" %(x, y))

