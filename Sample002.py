# Print "Hello World" to the console
print("Hello World")

# Variable assignments with different data types
name = "Giri Prasad P"  # String assignment
age = 30                # Integer assignment
score = 8.7             # Float assignment
isAvailable = True      # Boolean assignment

# Print variable values and their data types
print("Name:", name)
print("Datatype of name:", type(name))
print("Age:", age)
print("Datatype of age:", type(age))
print("Score:", score)
print("Datatype of score:", type(score))
print("Is Available:", isAvailable)
print("Datatype of isAvailable:", type(isAvailable))

# Working with complex numbers
complex1 = 3 + 5j       # Complex number assignment
complex2 = 2 - 4j       # Another complex number
complex3 = complex1 + complex2  # Addition of complex numbers
print("Complex1:", complex1)
print("Complex2:", complex2)
print("Complex3:", complex3)
print("Datatype of complex1:", type(complex1))
print("Datatype of complex2:", type(complex2))
print("Datatype of complex3:", type(complex3))

# Demonstrating list operations
list1 = ['Pen', 'Pencil', 'Eraser', 10, 20.5, True]  # List with mixed data types
print("List1:", list1)
print("Datatype of list1:", type(list1))

# Accessing the fourth element in the list (index 3)
print(" Fourth element in list1:", list1[3])

# Changing the value at index 3 (lists are mutable)
list1[3] = 'Python List is mutable'
print("Updated List1:", list1)

# Appending a new item to the end of the list
list1.append('New Item')
print("List1 after appending a new item:", list1)

# Inserting an item at index 3
list1.insert(3, 'iPhone')
print("List1 after inserting 'iPhone' at index 3:", list1)

# Creating another list
list2 = ['Book', 'Notebook', 'Pen', 'Pencil']

# Extending list1 with list2
list1.extend(list2)
print("List1 after extending with list2:", list1)

# Demonstrating remove and pop operations
list1 = ['A', 'B', 'C', 'D', 'E', 'D', 'F', 'G', 'H', 'I', 'J']
list1.remove('D')  # Removes the first occurrence of 'D'
list1.pop(0)       # Removes the first element
list1.pop()        # Removes the last element
print("List1 after removing 'D' and popping first and last elements:", list1)

# Iterating through the list and printing each element
for element in list1:
    print("Element in list1:", element)

# Printing each element with its index
totalelements = len(list1)
for i in range(totalelements):
    print("Element at index", i, "is:", list1[i])

# Clearing the list (removes all elements)
list1.clear()
print("List1 after clearing:", list1)
print(len(list1))  # Prints the length of the now-empty list

# Appending and updating elements in the cleared list
list1.append('Giri Prasad P')
print(list1)
list1[0] = 'Python'
print(list1)
