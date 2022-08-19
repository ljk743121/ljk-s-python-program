import requests as rr
from bs4 import BeautifulSoup
import time
import os
import pickle


class Number:
    def __init__(self,number):
        self.number = number


title=''
content=''
bs=''
path=''
number=Number(0)
url = 'http://www.bswtan.com/0/36/'
path='D:\\Cpanku\\Desktop\\dazhuzai\\{}.txt'
path_pick='D:\\Cpanku\\Desktop\\dazhuzai\\number.data'
cannot = ['\\','/',':','*','?','"','<','>','|']


def start(u):
    global a,b,bs
    a=rr.request('get',u)
    a.encoding = 'big-5'
    b=a.text
    bs=BeautifulSoup(b,'html.parser')

def get_title_content():
    global title
    title_t = title
    while title_t == title:
        title=str(bs.title)
        title=title.replace('<title>','')
        title=title.replace('</title>','')
        title=title.replace('_大主宰_笔趣阁','')
        #print(title + '    ' +title_t)
    time.sleep(0.25)
    global content
    content_c = content
    while content_c == content:
        content=str(bs.find(id="content"))
        content=content.replace('<div id="content">','')
        content=content.replace('<br/><br/>','\n')
        content=content.replace('</div>','')
    time.sleep(0.25)

def get_url():
    global url_list
    n=0
    #list=bs.find(id='dd')
    list=bs.find_all('a')
    url_list=[]
    #print(list)
    for item in list:
        url_list.append(item.get('href'))
    #print(url_list[30])
    for n in range(31):
        url_list.pop(0)
    #print(url_list)

def pick_number():
    global path_pick,number
    if not os.path.isfile(path_pick):
        with open (path_pick,'wb') as f:
            pickle.dump(Number(0),f)
            number = Number(0)
    else:
        with open (path_pick,'rb') as f:
            number = pickle.loads(f.read())

def main():
    global use_url,count_n,path,title
    pick_number()
    start(url)
    get_url()
    n=0
    for txt in url_list:
        if n > int(number.number):
            use_url =url + txt
            start(use_url)
            get_title_content()
        if n > int(number.number):
            if os.path.isfile(path.format(title)):
                print ('第{0}章<{1}>已存在'.format(n,title))
            else:
                try:
                    with open(path.format(title),'w',encoding='utf-8') as f:
                        #print (title)
                        #print (content)
                        f.write(str(title))
                        f.write('\n')
                        f.write(str(content))
                except OSError:
                    for s in cannot:
                        title = title.replace(s,'')
                    with open(path.format(title),'w',encoding='utf-8') as f:
                        #print (title)
                        #print (content)
                        f.write(str(title))
                        f.write('\n')
                        f.write(str(content))
                print('成功下载第{0}章:<{1}>'.format(n,title))
            with open (path_pick,'wb') as f:
                pickle.dump(Number(int(n)),f)
                #print (n)
        n=n+1
    print('finish')


#with open (path_pick,'wb') as f:
    #pickle.dump(Number(),f)

main()