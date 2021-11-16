# Boolean Operators: or
# The "or" operator combines two expressions into a larger expression
# that is "True" if either component is "True"

# Example
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

# Example
credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print('You have met at least one of the requirements.')

print('')
print("As long as one of the components is true then the if statement will run.")