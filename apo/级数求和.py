from re import I


k = int(input())
s = 0
i = 1
while s<=k:
    s += 1/i
    i += 1
print (i-1)