# Removing by Index: Pop
# pop() is a method to remove elements at a specific index.

# Example
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
# The method can be called without a specific index. Using .pop() without an index will 
# remove whatever the last element of the list is. In our case "Clowns 101" gets removed. 
removed_element = cs_topics.pop()
print(cs_topics)
# .pop() is unique in that it will return the value that was removed. If we wanted to 
# know what element was deleted, simply assign a variable to the call of the .pop() method. 
# In this case, we assigned it to removed_element.
print(removed_element)
# The method can be called with an optional specific index to remove. In our case, the 
# index 2 removes the value of "Balloon Making".
cs_topics.pop(2)
print(cs_topics)

# Example
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(3)
print(data_science_topics)

