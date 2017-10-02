#python3
import re
from indog import shi
def sdogread():
    '''读取来源资料'''
    f = open ('s.conf','r')
    fline = f.readlines()
    hdog=[]
    pdog={}
    for i in fline:
        if i.startswith('#') or not re.match('.*>.*=.*',fline[fline.index(i)]):
            del fline[fline.index(i)]
        else:
            pass
    print(fline)
    pptdog=re.compile(r'(.*)>(.*)=(.*)')
    for idog in fline:
        hdog.append(pptdog.findall(idog))
    #print(hdog[0][0][1])
    for icat in hdog:
        lindog=[]
        number=hdog.index(icat)
        lindog.append(shi(hdog[number][0][1]))
        lindog.append(hdog[number][0][2])

        pdog[hdog[number][0][0]]=lindog
    print('#')
    print(pdog)


sdogread()
