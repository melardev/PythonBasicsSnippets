"""
positional arguments are required arguments
optional arguments are keyword based arguments
args is used to allow the called to pass extra arguments
kwargs is used to allow caller to pass extra keyword arguments
"""


def func(a, b, c=7, *args, **kwargs):
    print('a=%s, b=%s, c=%s' % (a, b, c))
    print('args:', args)
    print('keyword arguments:', kwargs)


func(1, 2, 3, *(4, 5, 6), **{'A': 'a', 'B': 'b'})
print()
# very same as the previous
func(1, 2, 3, 4, 5, 6, A='a', B='b')
