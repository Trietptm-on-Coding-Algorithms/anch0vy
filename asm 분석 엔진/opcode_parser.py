# -*- coding: cp949 -*-
import engine
def asmgen(string,bit=32):
    #�տ� �ٹ��� �ִ°Ŷ� ���°Ŷ� ����
    #1����Ʈ 2����Ʈ 3����Ʈ ��ɾ� ����
    #32��Ʈ 64��Ʈ ����
    pass

def full_asmgen(string):
    tmp=[]
    ret=''
    while(len(string)):
        op,string=engine.asmgen(string,32)
        ret=ret+'\n'+op
        print ret#debug
    return ret[1:]

