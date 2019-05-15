"""
You can not specify positional arguments after keyword based arguments
This script triggers an error with message: positional argument follows keyword argument
"""


def func(a, b=2, c=4):
    print(a, b, c)


func(b=1, c=3, 0)
