# Boolean Operators: not
# The "not" operator reverses the boolean value.
# So if we have a True statement and apply a "not"
# operator we get a False statement.

# Example
not True == False
not False == True
not 1 + 1 == 2  # False
not 7 < 0       # True

# Example
credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")

print('Put not behind the variable. Found that kind of odd but whateva.')