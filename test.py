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
        if re.match('.*=.*',fline[fline.index(i)]):
            lines.append(i)
        else:
            pass

        #setnumber=setnumber+1
print(lines)
print('#')
#print(re.search('.*=.*',lines[0]))
