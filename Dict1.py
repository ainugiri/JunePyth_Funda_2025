# store collection of key-value pairs in a single variable.
# item1 
#    name: 'Parker'
#    price: 10.5
#    quantity: 100


item1 = {
    'name': 'Parker',
    'price': 10.5,
    'quantity': 100,
    'name': 'Hero',
    'quantity': 200  # This will overwrite the previous 'quantity' value
}
print("Item1:", item1)
item1 = {
    'name': 'Hero',
    'price': 12.5,
    'quantity': 450
}
print("Updated Item1:", item1)

d2 = dict()
print(d2)
print(type(d2))  # <class 'dict'>

d3 = dict(name="Raj", mobile = True, email = False, city="Pune")
print(d3)

print(f" Name of the person is {d3.get('name')} and email : {d3.get('email')}")

d3.pop('mobile')
print(d3)

d3.popitem()
print(d3)