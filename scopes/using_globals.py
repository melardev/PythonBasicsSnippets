"""
Practical example on using globals in python, it is really useful when you have app resources
that you wanna share across your whole application
"""

# At your application entry point you would use the following
globals()['log'] = open('./logfile', 'a')

# Later, somewhere in your code you would use
globals()['log'].write('An Error occurred\n')

# In other place in your codebase
logger = globals()['log']
logger.write('An Event occurred\n')
