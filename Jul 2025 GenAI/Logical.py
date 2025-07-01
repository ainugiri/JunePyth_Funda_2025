# Logical Operators
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))
# smallest 
# and - both conditions should be true
"""
condition1 condition2       AND     OR      Not(Condition1)
True        True            True    True     False
True        False           False   True     False
False       True            False   True     True
False       False           False   Flase    True 
"""




if ((x < y) and (x < z)):
    print(f"x: {x} is smallest")    # block will execute if both conditions are true
    #false  or  true   ->  True
if ((x < y) or (x < 10)) :
    #false  or  false  -> false
    print("Lesser price")  # block will execute if any one condition is true


#  identity operator 
obj1 = [123,234]      # variable pointing to an object in memory
obj2 = [123,234]      # variable pointing to another object in memory
obj3 = obj1     # obj3 is refer same memory of obj1


if obj3 == obj2:
    print("obj1 and obj2 are equal")  # checks value
if obj3 is obj2:
    print("obj3 and obj2 are same objects")  # checks identity  
else : 
    print("obj3 and obj2 are not same objects")



list1 = ['A825662', 'A932190', 'A825661', 'A933190']

print("A825662 is in the list",'A825662' in list1)  # True
print("A825665 is in the list",'A825665' in list1)  # False