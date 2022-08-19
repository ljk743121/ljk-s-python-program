import requests as rr
import requests
import re
from bs4 import BeautifulSoup


_url=r'http://www.bihuachaxun.com/langdu/items.php?wel=1&uid=ojZgU00U4XHBYka7EpN_mZnE4gc0&volumn=12&book_type=renjiaoban&vname=%E4%BA%BA%E6%95%99%E7%89%88'
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
    url_mp3='http://www.bihuachaxun.com/renjiaoban/mp3/volumn12/m{}.mp3'
    url_mp4='http://www.bihuachaxun.com/renjiaoban/video/volumn12/v{}.mp4'
    url_mp3_gsc='http://www.bihuachaxun.com/renjiaoban/mp3/volumn12/mgsc{}.mp3'
    url_mp4_gsc='http://www.bihuachaxun.com/renjiaoban/video/volumn12/vgsc{}.mp4'
    path = 'D:\\Cpanku\\Desktop\\yuwen\\'
    for n in range(1,18):
        if len(str(n))==1:
            n_new='0' + str(n)
        else:
            n_new=str(n)
        r_3=requests.get(url_mp3.format(n_new))
        r_4=requests.get(url_mp4.format(n_new))
        with open(path + n_new + '.mp3','wb') as f:
            f.write(r_3.content)
        with open(path + n_new + '.mp4','wb') as f:
            f.write(r_4.content)
        print ('第{}课下载完成'.format(n))
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
    
    
get_mp3_mp4()

