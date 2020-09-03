import platform,socket,re,uuid,json,logging

def sysInfo():
    info = {}
    info['Platform']=platform.system()
    info['Platform-release']=platform.release()
    info['Platform-version']=platform.version()
    info['Architecture']=platform.machine()
    info['Hostname']=socket.gethostname()
    info['Ip-Address']=socket.gethostbyname(socket.gethostname())
    info['Mac-Address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['Processor']=platform.processor()



    for x in info:
        print(x + ": " + info[x])


print(sysInfo())
