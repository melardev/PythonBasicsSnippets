my_dict = {
    'Manager': ['Shannon', 'Schmidt', 20],
    'Admin': ['Melani', 'Holloway', 25],
    'Developer': ['Maria', 'Valdez', 30],
}
print('Add a new one')
my_dict['Beginner'] = ['Bonnie', 'Sullivan', 18]
for key, value in my_dict.items():
    print(key, value)

print('Delete Manager')
del my_dict['Manager']
for key, value in my_dict.items():
    print(key, value)

if 'Manager' in my_dict:
    print('No manager in the group')

if 'Beginner' in my_dict:
    print('There is a beginner here!')
