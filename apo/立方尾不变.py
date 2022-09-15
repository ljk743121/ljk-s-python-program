n = int(input())
ans = 0
for i in range(1,n+1):
    li = i**3
    if li%(10**len(str(i)))==i:
        ans += 1
print(ans)