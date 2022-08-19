alpha = input().lower()
string = input().lower().split()
n = 0;position = 0;istrue = 0
for i in range(len(string)):
    if string[i] == alpha:
        if istrue == 0:
            position = len(''.join(string[:i]))+len(string[:i])
            istrue = 1
        n += 1
if n == 0:
    print (-1)
else:
    print(n,position)