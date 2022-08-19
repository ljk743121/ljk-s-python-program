import eyed3
import os
import re

def tag_filename(rootdir):
    for root,dirs,files in os.walk(rootdir):
        for name in files:
            if name.endswith('.mp3'):
                audiofile = eyed3.load(os.path.join(root,name))
                title = audiofile.tag.title
                artist = audiofile.tag.artist
                pattern = re.compile(r'^\d+')
                if pattern.match(str(name.find('-'))):
                    index = int(name.find('-')) + 2
                    if not index < len(title):
                        if not name.replace('.mp3','')[index:] == artist.replace('/',','):
                            file_new = name.replace('.mp3','')
                            file_new_strlist = []
                            for i in file_new:
                                file_new_strlist.append(i)
                            file_new_strlist[index:] = artist.replace('/',',')
                            file_new = ''.join(file_new_strlist)
                            file_name = file_new + '.mp3'
                            file_name = os.path.join(root,file_name)
                            try:
                                os.rename(os.path.join(root,name),file_name)
                            except Exception as e:
                                print ('rename {} fail'.format(os.path.join(root,name)))
                            else:
                                print ('rename {} success'.format(file_name))
        for dir in dirs:
            tag_filename(dir)

def filename_tag(rootdir):
    for root,dirs,files in os.walk(rootdir):
        for name in files:
            if name.endswith('.mp3'):
                index = int(name.find(' - ')) + 2
                #print (index)
                artist = name.replace('.mp3','')[index+1:].replace(',','/')
                title = name.replace('.mp3','')[:index-2]
                #print (title+' '+artist)
                try:
                    audiofile = eyed3.load(os.path.join(root,name))
                    audiofile.initTag()
                    audiofile.tag.title = title
                    audiofile.tag.artist = artist
                    audiofile.tag.save()
                except Exception as e:
                    print ('add tag to {} fail'.format(os.path.join(root,name)))
                    print (e)
                else:
                    print ('add tag to {} success'.format(os.path.join(root,name)))
        for dir in dirs:
            tag_filename(dir)

def rename():
    for root,dirs,files in os.walk(rootdir):
        for name in files:
            if name.endswith('.mp3'):
                if ' - 单曲 - 网易云音乐' in name:
                    try:
                        os.rename(rootdir + '\\' + name,rootdir + '\\' + str(name.replace('_',',').replace(' - 单曲 - 网易云音乐','')))
                        print('rename successful')
                    except Exception as e:
                        print(e)
rootdir = r'E:\NDMDownload'
rename()
filename_tag(rootdir)