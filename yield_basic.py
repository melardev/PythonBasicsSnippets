def get_generator():
    # It is like 3 returns executed!! it returns a generator object
    yield 1  # returns this first item and goes to suspended mode
    print("inside get_generator")
    yield 2  # returns this second item and goes to suspend mode
    print("inside get_generator")
    yield 3  # ...


generator = get_generator()

print("first loop")
for i in generator:
    print(i)
    if i == 2:
        break

print()
print("second loop")
for i in generator:
    print(i)
