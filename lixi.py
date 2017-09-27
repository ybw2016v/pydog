import time,os
bj=250000

t=0
i=0
idog=1
q=250000
m=250000
h=0
l=0
ipdog=1
while idog==1:
    benjin=250000
    qian1=benjin
    q=q+benjin*0.07
    h=m*0.03
    l=m
    m=m*1.03
    #fangan1[i]=q
    print('百分之七：')
    print('第'+str(i+1)+'年，本金：'+str(benjin)+'利息：'+str(benjin*0.07))
    print('累计：'+str(q))
    print('百分之三：')
    print('第'+str(i+1)+'年，本金：'+str(l)+'利息：'+str(h))
    print('累计：'+str(m))
    time.sleep(0.25)
    os.system("clear")
    

    i=i+1
    if m>q:
        if ipdog<0 :
            pass
        else:
            ipdog=0
        if ipdog==0:
            print('转折点')
    else:
        pass
    if ipdog < 1 :
        ipdog=ipdog-1
    else:
        pass
    if ipdog==-5:
        idog=0
    else:
        pass




print('end')
