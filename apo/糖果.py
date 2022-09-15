n,m,r = list(map(int,input().split()))
candy = list(map(int,input().split()))
children = {}
for i in range(m):
    if candy[i] in children.keys():
        children[candy[i]] += [str(i+1)]
    else:
        children[candy[i]] = [str(i+1)]
for i in range(r):
    ec1,ec2 = list(map(int,input().split()))
    children[ec1],children[ec2] = children[ec2],children[ec1]
for i in range(1,n+1):
    print (len(children[i]),' '.join(children[i]))