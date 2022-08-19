from itertools import permutations

item = list(permutations(['A','B','AB','O']))
#print (item)
result = list()
for a,b,c,d in item:
    if c == 'A' or c == 'AB':#c == 'AB'
        if d == 'A' or d == 'AB':#d == 'A'
            if b == 'B':
                result.append((a,b,c,d))
print (result)
        
    