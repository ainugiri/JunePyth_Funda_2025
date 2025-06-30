# multiple value / elements 
# ordered - 0,1,2,3,4,5, - unchangeable

tup1 = ('A','B','C','A','B')
print("Tuple1:", tup1)
print('Second element in Tuple1:', tup1[1])  # accessing the second element in the tuple (index starts from 0)
print(tup1[0])

l1 = list(tup1)
l1.append('C')  # converting tuple to list and appending a new item
l1[0] = 'Z'  # changing the first element in the list
tup1 = tuple(l1)  # converting the list back to tuple
print("Updated Tuple1 after converting back from list:", tup1)