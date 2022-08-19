t = int(input())
website = []
for i in range(t):
    n = int(input())
    for j in range(n):
        website.append(input().split())
sign = -1;memory = []
for i in range(len(website)):
    get = website[i][0]
    if get=='VISIT':
        if sign!=len(memory)-1:
            while sign<len(memory)-1:
                memory.pop()
        memory.append(website[i][1])
        sign += 1
        print (memory[sign])
    elif get=='BACK':
        if sign-1>-1:
            sign -= 1
            print (memory[sign])
        else:
            print ('Ignore')
    else:
        if sign+1<len(memory):
            sign += 1
            print (memory[sign])
        else:
            print ('Ignore')