import math
n = int(input())
a = list(map(int,input().split()));a = math.ceil(n/a[0])*a[1]
b = list(map(int,input().split()));b = math.ceil(n/b[0])*b[1]
c = list(map(int,input().split()));c = math.ceil(n/c[0])*c[1]
print (min(a,b,c))