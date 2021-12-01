# Len's Slice

# Create a list for 'toppings'
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Create a list for 'prices'
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurrences of 2 in the prices list.
num_two_dollar_slices = prices.count(2)

# Print the results.
print(num_two_dollar_slices)
print('')
# Find the length of the list toppings.
num_pizzas = len(toppings)

# Print 'We sell [num_pizzas] different kinds of pizza!'
print('We sell', num_pizzas, 'different kinds of pizza!' )
print('')

# Convert toppings and prices into a two-dimensional list.
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Print the two-dimensional list.
print(pizza_and_prices)

# Sort pizza_and_prices in the order of increasing prices (ascending)
pizza_and_prices.sort()

# Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print('')
#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[6]

# Remove anchovies from the list.
pizza_and_prices.pop(-1)
print(pizza_and_prices)
print('')

# Add pepper to the list. Ensure it stays in order of ascending.
pizza_and_prices.insert(4, [2.5,"peppers"])
print(pizza_and_prices)
print('')

# Price the 3 lowest cost pizza into a list called three_cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
print('')
