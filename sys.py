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
        if i.startswith('#'):
            del fline[fline.index(i)]
        else:
            pass


    ###
    conf=fline


    #print(conf)
    return conf
def hconf(confl):
        print(confl)
hconf(readconf())
print(zhiliang)
#hconf(ll)
#readconf()
#hconf(readconf())
#print(conf)
