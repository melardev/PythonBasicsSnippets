'''
Demo on difference between local and global scope
'''


def local():
    value = 300
    print('Inside local(), value is %d' % value)


value = 200
print('In global scope, value is %d' % value)

local()
# The expected result is 200, even though local has changed value, that variable was another one,
# it had local scope, it was available only on that function
print('In global scope after local(), value is %d' % value)
