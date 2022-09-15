n,m = list(map(int,input().split()))
shape = []
sign = []
for i in range(n):
    shape.append([x for x in input()])
while True:
    memory = []
    for i in range(n):
        s = []
        for j in range(m):
            s.append(shape[i][j])
        memory.append(s)
    for i in range(len(shape)):
        if shape[i] == m*['*']:
            shape[i] = m*['.']
    sign = []
    for i in range(-1,-n-1,-1):
        if shape[i]==["."]*n:
            sign.append(i+n)
    sign=[shape[x] for x in range(m) if not x in sign]
    shape = [["."]*n]*(m-len(sign))+sign
    if memory==shape:
        break
for ans in shape:
    print (''.join(ans))