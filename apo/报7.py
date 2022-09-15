n,m,t = list(map(int,input().split()))
person = []
for i in range(n):
    person.append(input())
sign = m-1
while len(person)>1:
    if t&7==0:
        person.pop(sign)
    t += 1;sign += 1
    if sign>=len(person):
        sign = 0
print (person[0])