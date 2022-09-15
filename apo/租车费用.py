from math import *
def ctime():
    stime = sum([int(b)/(60**a) for a,b in list(enumerate(input().split(':')))])
    etime = sum([int(b)/(60**a) for a,b in list(enumerate(input().split(':')))])
    time = ceil(etime-stime)-1
    return time if 10>=time else 10
print (ctime())