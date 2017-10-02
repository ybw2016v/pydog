#python3
import re
zhongdog=['Na=23\n', 'H=1\n', 'He=4\n', 'Li=6\n', 'O=16\n','Al=27\n']
longdog=[('H', '0'), ('Al', '2'), ('Na', '0'), ('O', '3')]


def welldog(list1):
    '''提取数据'''
    healdog={}
    comdog=re.compile(r'(.*)=(.*)')
    for j in list1:
        healdog[comdog.findall(j)[0][0]]=float(comdog.findall(j)[0][1])
    return healdog

#print(welldog(zhongdog))

def calone(l1dog,l2dog):
    setldog=[]
    # puchdog={}
    for ipdog in l2dog:
        ipdog=list(ipdog)
        #print(ipdog[1])
        if ipdog[1]==r'':
            ipdog[1]='1'
        else:
            #ipdog[1]='2'
            pass
        setldog.append(ipdog)
        #print(ipdog)
        #l2dog[l2dog.index(ipdog)]=ipdog
    #print(l2dog)
    pppdog=setldog
    puchdog=welldog(l1dog)
    mdog=0
    for itdog in pppdog:
        mdog=mdog+float(itdog[1])*puchdog[itdog[0]]





    return mdog

print(calone(zhongdog,longdog))
