"""
Snippet on for loop, check if condition, then break, detect if not found using a variable
Do not use this approach, use for else construct, which is shown in other demo, this is just to explain
how you could achieve the same result manually
"""
found = False
for item in ['nike', 'adidas', 'reebok']:
    if item == 'asics':
        print('asics is there')
        found = True
        break

if not found:
    print("Asics was not found")
