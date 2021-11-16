# Review

# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.

# We can create boolean expressions using relational operators: 
#  ==: Equals
#   !=: Not equals
#   >: Greater than
#   >=: Greater than or equal to
#   <: Less than
#   <=: Less than or equal to

# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements.

# Side note. There can be several if statements that can print if several are True.
# Example

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

venus = 0.91
mars = 0.38
jupiter = 2.34
saturn = 1.06
uranus = 0.92
neptune = 1.19

# Write an if statement below:

if planet == 1:
  print(weight * venus)
elif planet == 2:
  print(weight * mars)
elif planet == 3:
  print(weight * jupiter)
elif planet == 4:
  print(weight * saturn)
elif planet == 5:
  print(weight * uranus)
elif planet == 6:
  print(weight * neptune)
else:
  print("Invalid defintion. Please try again.")