# Review
# In summary:
# How to create a list
# How to access, add, remove, and modify list elements
# How to create a two-dimensional list
# How to access and modify two-dimensional list elements

# Example

# We create a list
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
preferred_size = ['Small', 'Large', 'Medium']
# Added 'Medium' to preferred_size
preferred_size.append('Medium')
print(preferred_size)
# Created a 2D list
customer_data = [['Ainsley', 'Small', True], ['Ben', 'Large', False], ['Chani', 'Medium', True], ['Depak', 'Medium', False]]
print(customer_data)
# Modified 'Chani' to 'False'
customer_data[2][2] = False
# Removed False from Ben
customer_data[1].remove(False)
# Merged two 2D lists into one.
customer_data_final = customer_data + [['Amit', 'Large', True], ['Karim', 'X-Large', False]]
print(customer_data_final)