n,num,m = int(input()),input(),int(input())
dec = 0
n_to_m = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
m_to_n = list(map(lambda x:x[0],list(n_to_m.items())))
for i in range(-1,-len(num)-1,-1):
    dec += n_to_m[num[i]]*(n**(-i-1))
ans = []
while True:
    ans.append(m_to_n[dec%m])
    dec = dec//m
    if dec==0 : break
ans.reverse()
print (''.join(ans))