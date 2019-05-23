"""
locals() contains a dictionary of local variables
one of the uses if when you want to use a variable but you don't know if it was
created or not, how do we make sure a variable exists in local scope? through locals()

The following snippet shows that, we want to use result dictionary to set the success key
to false or true, if we raise OSError before result gets created
we will hit the except block, if we try using result(which has not been created) we will
trigger yet another exception, to make sure it exists, or otherwise initialize it, we use locals()
"""


def get_computation_result():
    return {'number': 10}


try:
    # Uncomment this raise to see how useful is result
    # raise OSError("")
    result = get_computation_result()
    result['success'] = True
    raise OSError("Some run time error")
    result['second'] = get_computation_result()
except OSError as error:
    if 'result' not in locals():
        print('locals() saved me, ouf, thanks, let\'s initialize result before using it below')
        result = {}
    result['success'] = False

"""
Just in case you did not understand what I have said, run the following and you will
see your app crashing
"""
try:
    # Uncomment this raise to see how useful is result
    raise OSError("")
    result2 = get_computation_result()
    result2['success'] = True
except OSError as error:
    # result is used before initialization, which will lead to another exception
    # NameError: name 'result2' is not defined
    result2['success'] = False

print(result)
