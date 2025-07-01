# input from user
# calculate area of rectangle
# check area > 4000 sqft -> approved 
# else -> not approved

len = float(input("enter the length of the plot"))
bred = float(input("enter the breadth of the plot"))

area = len * bred

# if area > 4000:
#     print("Approved")
# else :
#     print("Not approved")

# if area > 100000 -> approved for school
# if area > 6000 -> approved for hospital
# if area > 4000 -> approved for residential
# if area <= 4000 -> not approved

if area > 100000:
    print("Approved for school")
elif area > 6000:
    print("Approved for hospital")
elif area > 4000:
    print("Approved for residentials")
else: 
    print("NOT Approved")


# collect 
s1 = float(input("Enter the score for sub1: "))
s2 = float(input("Enter the score for sub2: "))
s3 = float(input("Enter the score for sub3: "))

total_score = s1 + s2 + s3
avg_score = total_score / 3

if avg_score > 95 :
    print("You got A+")
elif avg_score > 90:
    print("You got A")
elif avg_score > 80:
    print("You got B")
else :
    print("Less than 80, not qualified for the next level")



user_option = int(input("Enter your option 1 for iPhone, 2 for Samsung, 3 for OnePlus   :" ))

match user_option:
    case 1:
        print("You selected iPhone")
        op2 = int(input("Enter your option for iPhone: 1. Purchase 2. Repair 3. Accessories: "))
        match op2:
            case 1:
                print("You selected Purchase for iPhone")
                print("Select the model: 1. iPhone 14 2. iPhone 15 3. iPhone 16")
                model = int(input())
                match model:
                    case 1:
                        print("You selected iPhone 14")
                        print("Payment options: 1. Credit Card 2. Debit Card 3. UPI")
                    case 2:
                        print("You selected iPhone 15")
                    case 3:
                        print("You selected iPhone 16")
                    
            case 2:
                print("You selected Repair for iPhone")
            case 3:
                print("You selected Accessories for iPhone")
    case 2:
        print("You selected Samsung")
        op2 = int(input("Enter your option for Samsung: 1. Purchase 2. Repair 3. Accessories: "))
    case 3:
        print("You selected OnePlus")
        op2 = int(input("Enter your option for OnePlus: 1. Purchase 2. Repair 3. Accessories: "))
    case _:
        print("Invalid option selected")


ip2 = int(input())
match ip2:
    case 1:
        # code
        i1 = input()
        match i1:
            case 1:
                #code
                pass
            case 2: 
                # code
                pass
    case 2: 
        pass
    case 3:
        pass
    case 4:
        pass