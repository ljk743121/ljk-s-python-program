number = {}
n = int(input())
m = list(map(int,input().split()))
for i in m:
    if i in number.keys():
        number[i] = number[i]+1
    else:
        number[i] = 1
ans = list(number.items())
ans.sort(key=lambda x:x[0])
ans.sort(key=lambda x:x[1])
print (ans[-1][0],ans[-1][1])