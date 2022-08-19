from Crypto.Cipher import AES
from requests_html import HTMLSession
import re
import os
import time

#initialize
ts_url_list = list()
download_path = 'D:\\Cpanku\\Desktop\\download_ts'
if not os.path.exists(download_path):
    os.makedirs(download_path)
if not os.path.isfile(download_path+'\\memory.data'):
    with open(download_path+'\\memory.data','w') as f:
        f.write(str(0))
started_time = time.time()

def read_m3u8(file):
    global key_url,ts_url_list
    with open(file,'r') as f:
        line = f.readline().replace('\n','')
        if line != '#EXTM3U':
            print ('this is not a m3u8 file')
            quit()
        while line:
            line = f.readline().replace('\n','')
            if re.match(re.compile('#EXT-X-KEY'),line):
                key_url = line.split(',')[1].replace('URI=','').replace('"', '')
            if not re.match(re.compile('#'),line):
                ts_url_list.append(line)
        ts_url_list.pop()

def DeCrypt(key, encryptData):                  # AES 解密
    myCipher = AES.new(key,AES.MODE_CBC,key)    # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
    date = myCipher.decrypt(encryptData)        # 调用解密方法，得到解密后的数据
    return date                                 # 返回解密数据

def get_file(url):
    get = HTMLSession().get(url)
    return get

def main():
    #m3u8_path = input()
    read_m3u8(r'D:\Cpanku\Desktop\asset.m3u8')
    key = get_file(key_url).text
    print('key is '+key)
    i = 1
    with open(download_path+'\\memory.data','r') as f:
        memory = int(f.read())
    for url in ts_url_list:
        if i > memory: 
            ts = get_file(url).content
            with open(download_path+'\\download.mp4','ab') as f:
                f.write(DeCrypt(key,ts))
            with open(download_path+'\\memory.data','w') as f:
                f.write(str(i))
            print ('{}.ts download successful'.format(i))
        i += 1
    end_time = time.time()
    print ('download mp4 successful!')
    print ('用时:'+str(end_time - started_time))

if __name__=='__main__':
    main()