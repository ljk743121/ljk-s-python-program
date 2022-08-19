from distutils.core import setup
import py2exe
import sys
#设置地柜限制次数
sys.setrecursionlimit(1000000)

INCLUDES = []

options = {
    "py2exe" :
        {
            "compressed" : 1, # 压缩   
            "optimize" : 2,
            "unbuffered" : True,#使用未缓冲的二进制stderr和stdout
            "bundle_files" : 1,#所有文件打包成一个.exe文件
            "dll_excludes" : []
        }
}


setup(
    options=options,    
    description = "this is a py2exe test",   
    zipfile=None,#不生成library.zip文件
    windows = [r'D:\Cpanku\Desktop\py\getmusic.py']
     )