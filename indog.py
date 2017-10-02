#python3
import re
def shi(setdog):
    pptdog=re.compile(r'([A-Z][a-z]{0,2})([0-9]{0,}\.{0,}[0-9]{0,})')
    #setdog='Na2.5S1O4'#input('in:')
    hhdog=pptdog.findall(setdog)
    #print(hhdog)
    return hhdog
