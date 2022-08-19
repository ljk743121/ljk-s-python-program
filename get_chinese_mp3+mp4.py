import requests as rr
import requests
from bs4 import BeautifulSoup


def url_get_text(url):
    global bs
    a=rr.request('get',url)
    a.encoding = 'big-5'
    b=a.text
    bs=BeautifulSoup(b,'html.parser')

def get_url():
    global title
    for item in bs.find_all('div'):
        #print(str(item))
        if str(item.get('class'))=="['artical', 'litem']":
            #print(item.get('lesson'))
            title=item.get_text()


#url_get_text_(url)
#get_url()

def get_mp3_mp4():
    global path
    url_mp3='http://www.bihuachaxun.com/renjiaoban/mp3/volumn12/m{}.mp3'
    url_mp4='http://www.bihuachaxun.com/renjiaoban/video/volumn12/v{}.mp4'
    url_mp3_gsc='http://www.bihuachaxun.com/renjiaoban/mp3/volumn12/mgsc{}.mp3'
    url_mp4_gsc='http://www.bihuachaxun.com/renjiaoban/video/volumn12/vgsc{}.mp4'
    path = r'D:\Cpanku\Desktop\pygetvideo\\'
    
    for n in range(1,20):
        if len(str(n))==1:
            n_new='0' + str(n)
        else:
            if int(n)==10 or int(n)==11 or int(n)==12:
                n_new=str(n) + '_{}'.format(str(int(str(n)[1])+1))
            elif int(n)>12:
                n_new=str(int(n)-2)
        r_3=requests.get(url_mp3.format(n_new))
        r_4=requests.get(url_mp4.format(n_new))
        with open(path + n_new + '.mp3','wb') as f:
            f.write(r_3.content)
        with open(path + n_new + '.mp4','wb') as f:
            f.write(r_4.content)
        print ('第{}课下载完成'.format(n_new))

    for n in range(1,11):
        if len(str(n))==1:
            n_new='0' + str(n)
        else:
            n_new=str(n)
        r_3=requests.get(url_mp3_gsc.format(n_new))
        r_4=requests.get(url_mp4_gsc.format(n_new))
        with open(path + 'gsc' + n_new + '.mp3','wb') as f:
            f.write(r_3.content)
        with open(path + 'gsc' + n_new + '.mp4','wb') as f:
            f.write(r_4.content)
        print ('第{}首古诗词下载完成'.format(n))

path = r'D:\Cpanku\Desktop\pygetvideo\\'
print ('六下语文音视频下载程序\n')
print ('by:ljk')
print ('PS:第十四课无法下载')
while True:
    print('开始下载')
    get_mp3_mp4()



