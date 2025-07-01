arithmetic operators

x = input("Enter a value for x    :   ")
print(x)
print(type(x))
y = input("Enter a value for y    :   ")
print(y)
print(type(y))

addition = x + y        
print(addition)

x = int(x)
y = int(y)
total = x + y
print(total)


x = float(input("Enter a value for x    :    "))
y = float(input("Enter a value for y    :    "))

print(x+y)          # addition
total = x + y
print(total)

print(f"Addition of {x} and {y} is x+y: {x+y}")
print(f"Multiplication of {x} and {y} x*y:  is {x*y}")
print(f"Subtract from {x} ,  {y} is x-y: {x - y}")
print(f"Divide {x} by {y} is x/y: {x/y}")
# side of square -> area

side = float(input("Enter the side size in ft: "))
area = side ** 2
print(f"The area of square with side {side} is {area}")

22 / 7 = 3, remainder = 1 

x_floor = 22 // 7
print("Floor value ", x_floor)
remainder = 22 % 7
print("Remainder value ", remainder)




Assignment Operator =
x = 10              # 10
x = 10 + 1          # 11
x += 1              # 12
x -= 5              # 7
print(x)

x = 20              # 20
x = x - 7           # 13
x *= 7              # 91
x /= 13             # 7
print(x)

price1 = float(input("Enter the car price from v1 : "))
price2 = float(input("Enter the car price from v2 : "))

# Comparison Operators
if price1 == price2 :
    print("Same price, you can purachase from anyone")
if price1 > price2 :
    print("purchase from v2")
if price1 < price2 :
    print("purchase from v1")
if price1 != price2 :
    print("Both are differemt")

