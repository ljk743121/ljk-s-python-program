n,m = list(map(int,input().split()))
s = list(map(int,input().split()))
wait_pool = s[:m]
sec = 0;choose = m
while wait_pool!=[0]*m:
    for x in range(len(wait_pool)):
        if wait_pool[x]!=0:
            wait_pool[x] = wait_pool[x]-1
    sec += 1
    for i in range(len(wait_pool)):
        if wait_pool[i] == 0 and choose<n:
            wait_pool[i] = s[choose]
            choose += 1
print (sec)