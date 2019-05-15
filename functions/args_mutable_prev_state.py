def func(my_list=[], my_dict={}):
    print(my_list)
    print(my_dict)
    my_list.append(len(my_list))
    my_dict[len(my_list)] = len(my_list)


func()
print()
func(my_list=[1, 2, 3], my_dict={'A': 1})
print()
func()  # Outch, it 'remembered' the previous list and dict objects, yeah, because they were created once, and changed
