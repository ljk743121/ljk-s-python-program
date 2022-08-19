import requests

url=input('请输入下载地址')
name=input('请输入下载文件名称(包括扩展名)')
get=requests.get(url)
with open('.\\{}'.format(name),'wb') as f:
    f.write(requests.get(url=url).content)