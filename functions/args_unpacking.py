def func(*args):
    print(args)


values = (1, 2, 3, 4)
# pass the tuple(single argument) as argument
func(values)
# pass the contents of tuple as arguments, tuple has 4 values, so pass 4 arguments to the function
func(*values)
