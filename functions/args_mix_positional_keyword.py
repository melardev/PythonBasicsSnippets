"""
Mixing positional arguments with keyword arguments
"""


def func(a, b=2, c=4):
    print('a=%s, b=%s, c=%s' % (a, b, c))


func(10)
# We can reorder args since we are passing them as keyword arguments
func(b=11, a=12, c=13)
# here we can not reorder it, the position argument must come first, the others we can reorder between them
func(14, c=15)
