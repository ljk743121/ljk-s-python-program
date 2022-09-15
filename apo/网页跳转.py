t = int(input())
website = []
for i in range(t):
    n = int(input())
    m = []
    for j in range(n):
        m.append(input().split())
    website.append(m)
for i in website:
    sign = -1;memory = []
    for j in range(len(i)):
        get = i[j][0]
        if get=='VISIT':
            if sign!=len(memory)-1:
                while sign<len(memory)-1:
                    memory.pop()
            memory.append(i[j][1])
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