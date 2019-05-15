"""
The same as args_all_types but showing that we can alter the order
the behaviour should be the same
"""


def func(a, b, *args, c=7, **kwargs):
    print('a=%s, b=%s, c=%s' % (a, b, c))
    print('args:', args)
    print('keyword arguments:', kwargs)


func(1, 2, 3, *(4, 5, 6), **{'A': 'a', 'B': 'b'})
print()
# very same as the previous
func(1, 2, 3, 4, 5, 6, A='a', B='b')
