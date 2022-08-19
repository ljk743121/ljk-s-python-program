put = input()+" "
m = 0
finish = list()
every = 1
for n in put:
    if m == 0:
        m += 1
        last = n
        continue
    if n == last:
        every += 1
    else:
        finish.append(last + str(every))
        every = 1
    last = n
finall = ''.join(finish)
if len(put)-1 == len(finall):
    finall = put
print (finall)