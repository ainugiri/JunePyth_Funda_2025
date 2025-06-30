# Store collection of key-value pairs in a single variable.

# Define a dictionary with duplicate keys ('name' and 'quantity').
# The last value for each duplicate key will overwrite the previous one.
item1 = {
    'name': 'Parker',
    'price': 10.5,
    'quantity': 100,
    'name': 'Hero',         # Overwrites previous 'name'
    'quantity': 200         # Overwrites previous 'quantity'
}
print("Item1:", item1)      # Prints the dictionary after overwriting

# Update the dictionary with new values.
item1 = {
    'name': 'Hero',
    'price': 12.5,
    'quantity': 450
}
print("Updated Item1:", item1)  # Prints the updated dictionary

# Create an empty dictionary.
d2 = dict()
print(d2)                      # Prints empty dictionary
print(type(d2))                # Prints the type: <class 'dict'>

# Create a dictionary using keyword arguments.
d3 = dict(name="Raj", mobile=True, email=False, city="Pune")
print(d3)                      # Prints the dictionary

# Access values using the get() method and formatted string.
print(f" Name of the person is {d3.get('name')} and email : {d3.get('email')}")

# Remove the key 'mobile' from the dictionary.
d3.pop('mobile')
print(d3)                      # Prints the dictionary after removal

# Remove the last inserted key-value pair from the dictionary.
d3.popitem()
print(d3)                      # Prints the dictionary after popitem