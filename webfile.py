import urllib3
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall  
  
  
  
page = urllib3.urlopen('https://app.readoor.cn/app/cm/pl/1482288115/21132-3251665b35d3e9?l_id=43089&s=1')   
contents = page.read()   
 #print(contents)  
soup = BeautifulSoup(contents,"html.parser")     
file_url_list = soup.find_all('ul', class_='mtree transit')
url_list = []
for tag in soup.find_all('li', class_='playlist_song mtree-active mtree_check'):
    url_list.append(tag)
print (url_list)