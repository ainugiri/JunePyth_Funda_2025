print("Hello World")
#  name = "Giri"
# in c, c++, java. 
# datatype variablename = value
# variablename = value

name = "Giri Prasad P" # Python is dynamically typed language, no need to declare datatype. if it within a quote, it is a string.
age = 30 # integer 
score = 8.7 # if it is a decimal, it is a float.
isAvailable = True # boolean value, True or False

print("Name:", name)
print("Datatype of name:", type(name))
print("Age:", age)
print("Datatype of age:", type(age))
print("Score:", score)
print("Datatype of score:", type(score))
print("Is Available:", isAvailable)
print("Datatype of isAvailable:", type(isAvailable))

complex1 = 3 + 5j # complex number
complex2 = 2 - 4j # complex number
complex3 = complex1 + complex2 # complex number addition
print("Complex1:", complex1)
print("Complex2:", complex2)
print("Complex3:", complex3)
print("Datatype of complex1:", type(complex1))
print("Datatype of complex2:", type(complex2))
print("Datatype of complex3:", type(complex3))


# Built-in data types in Python:
# 1. Numeric Types: int, float, complex.
# 2. Sequence Types: list, tuple, range.
# list = 
#      ordered
#      duplicates allowed
#      mutable (can be changed)
#      different data types allowed
#      set of items within square brackets []
list1 = ['Pen','Pencil', 'Eraser', 10, 20.5, True] # list can contain different data types]
#    index: 0     1       2        3    4      5
# total no of elements in list1 = 6
print("List1:", list1)
print("Datatype of list1:", type(list1))

print(" Fourth element in list1:", list1[3]) # accessing the fourth element in the list (index starts from 0)

# Mutable - change
list1[3] = 'Python List is mutable'
print("Updated List1:", list1)

list1.append('New Item') # adding a new item to the end of the list
print("List1 after appending a new item:", list1)

# list1[0] = 'iPhone'
# print("List1 after changing first element:", list1)

list1.insert(3, 'iPhone') # inserting 'iPhone' at index 3, fourth position
print("List1 after inserting 'iPhone' at index 3:", list1)

list2 = ['Book', 'Notebook', 'Pen', 'Pencil'] # another list

list1.extend(list2) # extending list1 with list2
print("List1 after extending with list2:", list1)


list1 = ['A', 'B', 'C', 'D', 'E', 'D', 'F', 'G', 'H', 'I', 'J']
list1.remove('D') # removes the first occurrence of 'D' from the list
list1.pop(0) # removes the first element, A is removed
list1.pop() # removes the last element, J is removed
print("List1 after removing 'D' and popping first and last elements:", list1)


for element in list1: 
    print("Element in list1:", element) # iterating through the list and printing each element

totalelements = len(list1) # printing the length of the list

for i in range(totalelements):
    print("Element at index", i, "is:", list1[i]) # printing each element with its index



list1.clear() # clears the list, removes all elements
print("List1 after clearing:", list1) # list1 is now empty
print(len(list1))

list1.append('Giri Prasad P')
print(list1)
list1[0] = 'Python'
print(list1)