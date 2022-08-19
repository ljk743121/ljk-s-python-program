mathstring = input()
result = 0
for i in mathstring.split('+'):
    if '*' in i:
        c = list(map(int,i.split('*')))
        m = c[0]
        for j in range(1,len(c)): m *= c[j]
        result += m
    else:
        result += int(i)
print (result)
#print (eval(mathstring))