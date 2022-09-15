n,m = list(map(int,input().split()))
fire = []
for i in range(n):
    fire.append([x for x in input()])
sec = 0
match = [['*']*m]*n
while match!=fire:
    memory = []
    for i in range(n):
        s = []
        for j in range(m):
            s.append(fire[i][j])
        memory.append(s)
    for i in range(n):
        for j in range(m):
            if fire[i][j]=='*':
                if i!=0:
                    memory[i-1][j]='*'
                if i!=n-1:
                    memory[i+1][j]='*'
                if j!=0:
                    memory[i][j-1]='*'
                if j!=m-1:
                    memory[i][j+1]='*'
    for i in range(n):
        s = []
        for j in range(m):
            s.append(memory[i][j])
        fire[i] = s
    sec += 1
print (sec)