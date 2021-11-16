# Sal's Shipping
# I learned with this project you dont need to use the + to put
# stuff together. Just use a comma like in line 11.

weight = 41.5
charge = 20
premium = 125
# Ground Shipping

if weight <= 2:
  cost = 1.5
  print("Ground Shipping:$", cost * weight + charge)

elif weight > 2 and weight <= 6:
  cost = 3.00
  print("Ground Shipping:$", cost * weight + charge)

elif weight > 6 and weight <= 10:
  cost = 4.00
  print("Ground Shipping:$", cost * weight + charge)

elif weight > 10:
  cost = 4.75
  print("Ground Shipping:$", cost * weight + charge)

else:
  print("Invalid")
print("Ground Shipping Premium:$", premium)

if weight <= 2:
  cost = 4.5
  print("Drone Shipping:$", cost * weight)

elif weight > 2 and weight <= 6:
  cost = 9.00
  print("Drone Shipping:$", cost * weight)

elif weight > 6 and weight <= 10:
  cost = 12.00
  print("Drone Shipping:$", cost * weight)

elif weight > 10:
  cost = 14.25
  print("Drone Shipping:$", cost * weight)