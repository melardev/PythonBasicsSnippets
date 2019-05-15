s = set('I want to travel to Lisbon')
print(type(s))
print(s)

s2 = {'Brazil', 'Spain', 'Germany', 'Argentina'}
popped = s2.pop()
print('popped', popped)
print('s2', s2)
s2.add(popped)
s3 = s2
s3.add('France')
print('s2', s2)

s4 = s2.copy()

s4.remove('France') # throws an exception if not found
# s4.discard('France') does not throw an exception if not found
print('s2', s2)
print('s4', s4)
s4.clear()
print('s4', s4)
s4.update({'Brazil', 'Spain'})  # changes the set in place
print('s4', s4)
print('s4.union()', s4.union({'Australia'})) # returns a new set
print('s4.union()', s4 | {'Australia'})
print('s4', s4)


list_countries = list(s2)
print('list_countries', list_countries)
set_countries = set(list_countries)
print('set_countries', set_countries)

set_countries.add('Morocco')
frozen_countries = frozenset(list_countries)
#frozen_countries.add('Some country')

print({'Argentina', 'Germany'}.issubset(set_countries))
print(set_countries.issuperset(['Argentina', 'Germany']))
print('difference', set_countries.difference({'Spain', 'Brazil'}))
#set_countries.difference_update({'Spain', 'Brazil'})
print(set_countries.intersection({'Spain', 'China'}))
# set_countries.intersection_update({'Spain', 'China'})

print(set_countries.symmetric_difference({'Japan', 'China', 'Argentina'}))
# set_countries.symmetric_difference_update({'Japan', 'China', 'Argentina'})

if 'Germany' in set_countries:
    print('Germany in the set')