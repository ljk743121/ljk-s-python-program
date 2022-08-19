n = int(input())
for get in range(2,n+1):
    a = []
    for i in range(1,get+1):
        if i == 1:
            a.append(1)
        else:
            if get%i == 0:
                if not i in a and not i==get:
                    a.append(i)
                    a.append(get//i)
    a = set(a)
    if sum(a) == get:
        print (get)