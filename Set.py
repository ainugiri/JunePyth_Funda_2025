# Define a set with some duplicate elements (duplicates will be removed automatically)
set1 = {
    'A825662',
    'A825772',
    'A847154',
    'A825662',
    'A825772',
    'A847154',
    'A978457',
    'A978457', 
}

# Print the set (duplicates are removed, order is not guaranteed)
print(set1)
# Example output: {'A847154', 'A825662', 'A978457', 'A825772'}

# Convert the set to a list
l1 = list(set1)

# Append a new element to the list
l1.append('A825661')

# Convert the list back to a set (to remove any duplicates, if any)
set1 = set(l1)

# Print the updated set
print(set1)

# Print the type of set1 to confirm it's a set
print(type(set1))  # <class 'set'>

# collections : set, list, tuple, dictionary
