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

print(set1)
# {'A847154', 'A825662', 'A978457', 'A825772'}
l1 = list(set1)  # converting set to list
l1.append('A825661')
set1 = set(l1)  # converting list back to set
print(set1)
print(type(set1))  # <class 'set'>

# collections : set, list, tuple, dictionary
