n, m = list(map(int, input().split()))
shape = []
for i in range(n):
    shape.append([x for x in input()])

def clear(li):
    global shape
    for i in li:
        try:
            line = shape[i[0]]
            data = [x for x in line]
            for j in range(1,len(i)):
                data[i[j]]='.'
            shape[i[0]] = data
        except Exception:
            pass


def pcz(list):
    memory = []
    times = 0
    for i in list:
        m2 = []
        for j in range(m):
            if len(m2)==3:
                memory.append(([times]+m2))
                break
            elif i[j] == "*":
                m2.append(j)
            else:
                continue
        if len(m2)<3:
            return False
        times += 1
    p = 0;z = 0
    for i in range(len(memory)-1):
        a = memory[i][1]-memory[i+1][1]
        b = memory[i][2]-memory[i+1][2]
        c = memory[i][3]-memory[i+1][3]
        if a==1 and b==1 and c==1:
            p += 1
        elif a==0 and b==0 and c==0:
            z += 1
        else:
            return False
    if p == len(memory)-1:
        clear(memory)
        return "平行四边形"
    elif z == len(memory)-1:
        if z == 2:
            clear(memory)
            return "正方形"
        else:
            clear(memory)
            return "长方形"
    else:
        return False

def ts(list):
    memory = []
    times = 0
    tf = 0
    for i in list:
        for j in range(m):
            if i[j] == "*" and j-1>=0:
                if i[j-1] == '.' and i[j+1] == '.':
                    memory.append(([times,j]))
                    for k in range(1,n-times):
                        line = [int(times+k)]
                        line2 = []
                        for ii in range(j-k,j+k+1):
                            line2.append(ii)
                        memory.append((line+line2))
                    clear(memory)
                    tf = 1
                    return "三角形"
            else:
                continue
        times += 1
    if not tf:
        memory = []
        times = 0
        for i in list:
            for j in range(m):
                if i[j] == "*":
                    data = j
                    while i[j] == "*":
                        j += 1
                    for k in range(n-times):
                        line = [int(times+k)]
                        line2 = []
                        for ii in range(data-k,j+k+1):
                            line2.append(ii)
                        memory.append((line+line2))
                    clear(memory)
                    return "梯形"
                else:
                    continue
            times += 1

is_true = [['.'] * m] * n
while is_true != shape:
    result = pcz(shape)
    if result:
        print (result,end=' ')
    else:
        result = ts(shape)
        print (result,end=' ')