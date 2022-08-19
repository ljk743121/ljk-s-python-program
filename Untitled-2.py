import itertools as its
import datetime
import string
 
#记录程序运行时间
start=datetime.datetime.now()
words_1 = '1234567890'#这里可以加入字母和其他字符，使用string包更方便
words_2 = 'qwertyuiopasdfghjklzxcvb'
words_3 = words_2.upper() + "_"
words = words_1# + words_2# + words_3

#with open(r"D:\Cpanku\Desktop\paswwer.txt",'r') as f:
#    line = f.readlines()
#    if len(line) != 0:
#        read = len(line)
#        read_2 = len(line[len(line) - 1])
    

# 生成密码的位数
def makepassword(n) :
    r = its.product(words,repeat=n)#4即生成4位密码，正常情况下热点密码位数为8
    #print (r)
    for i in r:
        dic.write(''.join(i))
        dic.write(''.join('\n'))
        print(i)
 
dic =open(r"D:\Cpanku\Desktop\paswwer2.txt",'a')
#for m in read:
#    txt = ''.join(i)
for n in range(9):
    makepassword(n) 

dic.close()
print('密码本生成好了')
end=datetime.datetime.now()
print("生成密码本用时间：{}".format(end-start))
