n=m=int(input())
q = []
while True:
    it = 1
    for i in range(2,m+1):
        if m%i==0:
            q.append(i)
            m = m//i
            it = 0
            break
    if it:break
if len(q)>1:
    print (n//min(q))
else:
    print (1)