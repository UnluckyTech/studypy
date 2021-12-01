# Review
# Add elements to a list by index using the .insert() method.
# Remove elements from a list by index using the .pop() method.
# Generate a list using the range() function.
# Get the length of a list using the len() function.
# Select portions of a list using slicing syntax.
# Count the number of times that an element appears in a list using the .count() method.
# Sort a list of items using either the .sort() method or sorted() function.


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
# How many items are in the warehouse?
inventory_len = len(inventory)
print(inventory_len)
# Select the first element in inventory.
first = inventory[1]
# Select the last element in inventory.
last = inventory[-1]
# Select items 2 through but not including 6 from inventory.
inventory_2_6 = inventory[2:6]
# Select the first 3 items from inventory.
first_3 = inventory[0:3]
# How many 'twin beds' are in inventory.
twin_beds = inventory.count('twin bed')
# Remove the 5th element.
removed_item = inventory.pop(4)
# Insert '19th Century Bed Frame' into inventory.
inventory.insert(10,"19th Century Bed Frame")
# Sort inventory
inventory.sort()
print(inventory)