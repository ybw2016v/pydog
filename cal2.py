#python3
import cal1
from cal1 import welldog,calone
hupdog=['Na=23\n', 'H=1\n', 'He=4\n', 'Li=6\n', 'O=16\n','C=12\n','K=39\n','Al=27\n'] 
lepdog={'Na': [[('Na', '2'), ('C', ''), ('O', '3')], '0.99', 'Na2CO3'], 'K': [[('K', '2'), ('C', ''), ('O', '3')], '0.98', 'K2CO3'], 'Al': [[('Al', '2'), ('O', '3')], '0.88', 'Al2O3']}
def caltwo(soupdog,peuodog):
    '''计算摩尔原子质量'''
    derdog={}
    for spdog in soupdog:
        hherdog=[]
        a=soupdog[spdog]
        hudog=0
        for huudog in a[0]:
            if huudog[0]==spdog:
                hudog=huudog[1]
            else:
                pass
                
        b=calone(peuodog,a[0])
        h=b/(float(a[1])*float(hudog))
        #print(h)
        hherdog.append(h)
        hherdog.append(b)
        derdog[spdog]=hherdog
    return derdog


u=caltwo(lepdog,hupdog)
print(u)