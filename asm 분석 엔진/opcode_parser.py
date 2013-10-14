# -*- coding: cp949 -*-
import engine
def asmgen(string,bit=32):
    #앞에 꾸밈자 있는거랑 없는거랑 구별
    #1바이트 2바이트 3바이트 명령어 구별
    #32비트 64비트 구별
    pass

def full_asmgen(string):
    tmp=[]
    ret=''
    while(len(string)):
        op,string=engine.asmgen(string,32)
        ret=ret+'\n'+op
        print ret#debug
    return ret[1:]

