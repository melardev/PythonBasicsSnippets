"""
In programming languages there are some scenarios where we pass arguments by reference
that means, if we change it inside a function, it will be changed everywhere this variable is used
this happens for lists, dictionaries, custom classes, etc, etc.
A snippet is worth 1000 words
"""


def func(my_list, my_dict):
    my_list.append(1)
    my_dict['A'] = 'b'


list_example = []
dict_example = {}
func(list_example, dict_example)

# Oops, now list contains something, the same for dict
print(list_example)
print(dict_example)
