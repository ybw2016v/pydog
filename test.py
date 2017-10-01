#python3
import re
f = open ('data.conf','r')
lines=[]
fline = f.readlines()
print(fline)
#setnumber=0
for i in fline:
    if i.startswith('#'):
        pass
    else:
        lines.append(i)
        #setnumber=setnumber+1
print(lines)
