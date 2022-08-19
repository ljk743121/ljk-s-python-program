import math

n = int(input())
sum = 1
if n == 2:
    print (sum)
else:
    for i in range(2,n+1):
        max = math.ceil(math.sqrt(i))
        istrue = 1
        for j in range(2,max+1):
            if i%j==0:
                istrue = 0
                break
        if istrue:
            sum += 1
    print (sum)