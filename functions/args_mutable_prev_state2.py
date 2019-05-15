def func(my_list=[], my_dict={}, counter=0):
    my_list.append(counter)
    my_dict[counter] = counter
    counter += 1
    print(my_list)
    print(my_dict)
    print()


func()
func()
func()
