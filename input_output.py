print("Hello world")
print("Hello ", end=' ')
print('World')

import sys

sys.stdout.write('Hello world')
sys.stdout.write('Another one')
# flush the contents from the buffer
sys.stdout.flush()

print()
import time

for i in range(3):
    sys.stdout.write(str(i) + ", ")
    # time.sleep(1)

print()
print('enter something')
line = sys.stdin.read()
print(line)

secret = 'my secret'
another_line = input('enter something > ')
print(another_line)

# python 3 does not have raw_input, python 2 does, raw_input just returns string
# input() is the new raw_input() in python 3
import getpass

mypass = getpass.getpass()
print(mypass)
