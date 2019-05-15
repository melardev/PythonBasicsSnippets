def func(**kwargs):
    print(kwargs)


# All the below lead to the same result
func(a=1, b=2)
func(**{'a': 1, 'b': 2})
func(**dict(a=1, b=2))
