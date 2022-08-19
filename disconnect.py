from pywifi import PyWiFi
from pywifi import const

wifi = PyWiFi()
ifaces = wifi.interfaces()[0]    

while True:
    if ifaces.status() == const.IFACE_CONNECTED:
        ifaces.disconnect()
        print ("disconnect succeed")
