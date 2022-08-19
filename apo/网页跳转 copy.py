tt = int(input())

def cal():
    t = int(input())
    l = [] # a
    r = []
    while t:
        t -= 1
        x = input()
        if "VISIT" in x:
            y = x.split(' ')[1]
            l.append(y)
            print(y)
            r = []
        elif x == "BACK":
            if len(l) > 1:
                r.append(l[-1:][0])
                l = l[:-1]
                print(l[-1:][0])
            else:
                print("Ignore")
        elif len(r) > 0:
            l.append(r[-1:][0])
            print(r[-1:][0])
            r = r[:-1]
        else:
            print("Ignore")

while tt:
    tt -= 1
    cal()