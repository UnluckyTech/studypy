# Boolean Operators: and
# Sometimes conditional statements will require multiple boolean expressions.
# Here are more that will combine multiple boolean expressions into one.

# "and"
# "or"
# "not"

# "and" combines two boolean expressions and evaluates as "True" if both its
# components are "True" but otherwise "False".

# Example
(1 + 1 == 2) and (2 + 2 == 4) # True
(1 > 9) and (5 != 6)          # False
(1 + 1 == 2) and (2 < 1)      # False
(0 == 10) and (1 + 1 == 1)    # False

# Second and third example are partially true but due to them not being
# entirely True they are deemed as False.

# Example
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

# Example
credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

print('')
print('Now we have a better idea on what the boolean operator "and" does')