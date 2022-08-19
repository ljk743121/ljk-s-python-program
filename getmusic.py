from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver,common
from eyed3 import load
from re import compile
import os
import time

def getmusic():
    global title,artist,driver,image,url
    pattern = compile(r'id=')
    id = pattern.split(url)[1]
    #获取音乐外链
    song = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(id)
    try:
        if not os.path.isdir(os.getcwd()+'\\Download_Music'):
            os.makedirs(os.getcwd()+'\\Download_Music')
        #绕过反爬虫机制获取音乐
        r = HTMLSession().get(song)
        with open(os.getcwd()+'\\Download_Music\\'+str(title+' - '+artist).replace('/',',')+'.mp3','wb') as f:
            f.write(r.content)
        print('Download music successful({})'.format(str(title+' - '+artist).replace('/',',')))
    except Exception as e:
        print('Download music fail({0}):{1}'.format(str(title+' - '+artist).replace('/',','),e))
    try:
        #下载音乐封面图片
        r = HTMLSession().get(image)
        with open(os.getcwd()+'\\Download_Music\\'+str(title+' - '+artist).replace('/',',')+'.jpg','wb') as f:
            f.write(r.content)
        print('Download image successful({})'.format(str(title+' - '+artist).replace('/',',')))
    except Exception as e:
        print('Download image fail({0}):{1}'.format(str(title+' - '+artist).replace('/',','),e))

def add_tag():
    global title,artist
    try:
        #为音乐添加标题,艺术家,封面图片等标签
        audiofile = load(os.getcwd()+'\\Download_Music'+'\\{}.mp3'.format(str(title+' - '+artist).replace('/',',')))
        audiofile.initTag()
        audiofile.tag.title = title
        audiofile.tag.artist = artist.replace('\\','/')
        audiofile.tag.images.set(3,open(os.getcwd()+'\\Download_Music\\'+str(title+' - '+artist).replace('/',',')+'.jpg','rb').read(),'image/jpeg')
        audiofile.tag.save()
        #删除图片文件
        os.remove(os.getcwd()+'\\Download_Music\\'+str(title+' - '+artist).replace('/',',')+'.jpg')
        print ('Add tag successful({})'.format(str(title+' - '+artist).replace('/',',')))
    except Exception as e:
        print ('Add tag fail({0}):{1}'.format(str(title+' - '+artist).replace('/',','),e))

def getin():
    global artist,title,driver,image,url
    try:
        #阻止弹出窗口
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        #selenium重定向到Chrome
        driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=option)
        driver.get(url)
        #解决request获取不到iframe的问题
        iframe = driver.find_element_by_tag_name('iframe')
        driver.switch_to_frame(iframe)
        #使用bs4分析html
        bs = BeautifulSoup(driver.page_source,'html.parser')
        #获取标题,艺术家,封面链接等信息
        title = str(bs.find(attrs={"property":"og:title"})['content'])
        artist = str(bs.find('title')).replace('<title>','').replace('</title>','').replace(' - 单曲 - 网易云音乐','').replace(title + ' - ','')
        image = str(bs.img.get('data-src'))
        #因技术原因,无法解决vip音乐
        is_vip = str(bs.find_all('i'))
        if 'VIP' in is_vip:
            raise Exception('Can\'t get the music because of VIP')
    except common as e:
        print ("WebdriverError:" +e)

def main():
    global url
    try:
        getin()
        print ('Start download music...')
        getmusic()
        print ('Start add tag...')
        add_tag()
    except Exception as e:
        print('Get music fail:{}'.format(e))


url = str(input('Please input the music\'s link:'))
start = time.time()
main()
print ('Use time:'+str(time.time()-start))