N = int(input())

def reverse(n):
    r = 0
    while n!=0:
        r = 10*r + n%10
        n = n//10
    return r

if N==0:
    print (0)
else:
    print ((N//abs(N))*reverse(abs(N)))