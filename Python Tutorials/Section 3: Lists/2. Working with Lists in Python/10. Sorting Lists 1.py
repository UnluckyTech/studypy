# Sorting Lists 1
# We can use the list method .sort() to sort lists in alphabetical order.

# Example
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)

# You can also reverse the order of the list.
# Example
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)