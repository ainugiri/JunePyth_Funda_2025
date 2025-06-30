# Creating a tuple with multiple values (tuples are ordered and unchangeable)
tup1 = ('A','B','C','A','B')
print("Tuple1:", tup1)

# Accessing the second element in the tuple (index starts from 0)
print('Second element in Tuple1:', tup1[1])

# Accessing the first element in the tuple
print(tup1[0])

# Converting the tuple to a list to allow modifications
l1 = list(tup1)

# Appending a new item to the list
l1.append('C')

# Changing the first element in the list
l1[0] = 'Z'

# Converting the list back to a tuple
tup1 = tuple(l1)

# Printing the updated tuple
print("Updated Tuple1 after converting back from list:", tup1)