import random

num = random.randint(0, 10)

print(num)

if num < 5:
    print('less than 5')
else:
    print('5 or more')

if num > 8:
    print("greater than 8")
elif num > 6:
    print("greater than 6")
elif num > 4:
    print("greater than 4")
elif num > 2:
    print("greater than 2")
else:
    print("2 or less")
