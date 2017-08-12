ectdog={ 'zf1' : 1,
         'zf2' : 1,
         'zf3' : 1,
         'zf4' : 1,
         'zf5' : 1,
         'zf6' : 1,
         'zf7' : 1
       }#这个字典没有顺序。
#ectdog.sort() #这里报错了。
numberdog= 0
for a,b  in ectdog.items():
    #a=int(input('the code of %s:' %a ))   #这里好像没有什么用
    ectdog[a]=int(input('the code of %s:' %a ))
for a,b  in ectdog.items():
    numberdog=numberdog+b
for a,b  in ectdog.items():
    print (b)
print ('共有')
print(7-numberdog)
print ('个倒立文字。')
kdog=0
ll=''
if ectdog['zf1']==0 :
    ll='[12.95,15]'
    kdog=1
else:
    pass
if ectdog['zf2']==0 :
    if kdog==0:
        ll=ll+'[36.1,16.1]'
        kdog=1
    else:
        ll=ll+',[36.1,16.1]'
else:
    pass
if ectdog['zf3']==0 :
    if kdog==0:
        ll=ll+'[57.16,24.44]'
        kdog=1
    else:
        ll=ll+',[57.16,24.44]'
else:
    pass
if ectdog['zf4']==0 :
    if kdog==0:
        ll=ll+'[84.52,19.17]'
        kdog=1
    else:
        ll=ll+',[84.52,19.17]'
else:
    pass
if ectdog['zf5']==0 :
    if kdog==0:
        ll=ll+'[108.72,28.64]'
        kdog=1
    else:
        ll=ll+',[108.72,28.64]'
else:
    pass
if ectdog['zf6']==0 :
    if kdog==0:
        ll=ll+'[132.95,24.44]'
        kdog=1
    else:
        ll=ll+',[132.95,24.44]'
else:
    pass
if ectdog['zf7']==0 :
    if kdog==0:
        ll=ll+'[151.89,23.38]'
        kdog=1
    else:
        ll=ll+',[151.89,23.38]'
else:
    pass
print(ll)
captcha='{"img_size":[200,44],"input_points":['+ll+']}'
print(captcha)
