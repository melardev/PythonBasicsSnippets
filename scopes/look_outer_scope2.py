def wrapper_func():
    variable = 100

    def local_func1():
        # variable does not exist in this local scope, it will be looked up
        # on the outer scopes until first is found
        print('In local scope variable has the following value', variable)

    # calling the function local
    local_func1()

    def local_func2():
        def local_func3():
            print('In local scope3 variable has the following value', variable)

        local_func3()

    local_func2()


variable = 150
print('In global scope variable has the following value', variable)
wrapper_func()
