import os

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir): 
        for file in files:
            if os.path.splitext(file)[1] == '':
                L.append(file)
    return L

line = file_name(r'C:\Users\ljk\AppData\Local\Netease\CloudMusic\webdata\lyric')
print (line)
path= 'C:\\Users\\ljk\\AppData\\Local\\Netease\\CloudMusic\\webdata\\lyric'
i=1
for file_ in os.listdir(path):
    if os.path.isfile(os.path.join(path,file_))==True:
        if os.path.splitext(file_)[1] == '':
            print (file_)
            os.rename(os.path.join(path,file_),os.path.join(path,file_ + '.txt'))
print ("End")
