"""
Snippet on implementing a minimum enforcement rule using ternary conditional operators
"""
value = 5
MINIMUM = 7
new_value = value if value > MINIMUM else MINIMUM
print(new_value)
