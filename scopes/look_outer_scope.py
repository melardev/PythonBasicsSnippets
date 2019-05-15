# Local versus Global

def local_scope_func():
    # The interpreter will look for the variable in the current scope
    # it does find it, so it will look the outer scope, which is the global scope
    # this happens when you don't create the variable anywhere else in this scope
    # for example, if you try to variable=20 after the below line, then the script crashes
    print('In local scope variable has the following value', variable)



variable = 150
print('In global scope variable has the following value', variable)

local_scope_func()
