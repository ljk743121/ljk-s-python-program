import os
from cn_to_num import chinese2digits

files = os.listdir(r'D:\Cpanku\Desktop\大主宰')
print (files)
i=3

for f in files:
    original = r'D:\Cpanku\Desktop\大主宰\\' + files[i]
    front=int(files[i].index('第')) + 1
    last=int(files[i].index('章'))
    new = r'D:\Cpanku\Desktop\大主宰\\' +files[i].replace(files[i][front:last],str(chinese2digits(files[i][front:last])))
    print(os.rename(original,new))
    i += 1