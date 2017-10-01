#python3
import re
zhiliang={}
listdata=[]
def start():
    '''启动界面'''
    print("KNN PROGECT")
start()
conf=''
def readconf():
    global conf
    conf=['','']
    '''读取配置文件'''
    f = open ('data.conf','r')

    #conf=0
    #while True:

    fline = f.readlines()
    ###删除注释
    for i in fline:
        if i.startswith('#') or not re.match('.*=.*',fline[fline.index(i)]):
            del fline[fline.index(i)]
        else:
            pass


    conf=fline


    #print(conf)
    return conf
def hconf(confl):
        print(confl)
        comdog=re.compile(r'(.*)=(.*)')
        for j in confl:
            jdog=comdog.findall(j)
            zhiliang[jdog[0][0]]=float(jdog[0][1])
        print(zhiliang)



hconf(readconf())
#print(zhiliang)
#hconf(ll)
#readconf()
#hconf(readconf())
#print(conf)
