# -*- coding: cp949 -*-
import struct
def ModRM32(opcode,r1,r2,E=0):#여기서 opcode는 앞에 명령어 때고서 넘긴다
                    #이제 우리가 할 일은 명령어 뒤 문자열을 만드는 것
                    #최대로 만들어질 수 있는 형태는 [eax(+eax*??)(+??)],??
                    #                           reg1,reg2,reg2_x,plus,reg4
                    #r1,r2 에는 오퍼랜드의 바이트 크기가 들어가고 E에는 E가 있는 위치가 들어간다
                    #E가 있는 쪽이 표 왼쪽 레지 이름이 들어간다
                    #예외로 r1과 r2에 5,6 이 들어갈땐 mmo xmmo 를 뜻한다
    b=bin(int(opcode[0].encode('hex'),16))[2:]
    for x in range(8-len(b)):
        b='0'+b
    Mod=b[0:2]
    Reg=b[2:5]
    RM=b[5:8]
    reg1=''
    reg2=''
    reg2_x=''
    plus=''
    reg4=''
    set_mod11=0
    if E==1:
        r1,r2=r2,r1#이제 무조건 왼쪽에 표의 왼쪽 것이 들어간다. 리턴할때 E값 비교하고서 왼쪽 오퍼랜드와
                    #오른쪽 오퍼랜드 바꿔주면 된당
    if Mod != '11' and RM=='100':#sib비트 있음!
        has_sib=1
    else:
        has_sib=0
        
    if Mod=='00':
        plus=''
        
    elif Mod =='01':
        t=struct.unpack('<b',opcode[1+has_sib])[0]
        plus=hex(t)
        if t>0:
            plus='+'+plus
        elif t==0:
            plus = ''

    elif Mod == '10' :
        t1=opcode[1+has_sib:1+has_sib+3]
        t2=struct.unpack('<i',t1)[0]
        plus=hex(t2)
        if t2>0:
            plus='+'+plus
        elif t2==0:
            plus = ''

    elif Mod == '11' :
        set_Mod11=1
        plus = ''
        reg2 = ''
        reg2_x = ''
        if r1==4:
            if RM == '000':
                reg1='EAX'
            elif RM == '001':
                reg1='ECX'
            elif RM == '010':
                reg1='EDX'
            elif RM == '011':
                reg1='EBX'
            elif RM == '100':
                reg1='ESP'
            elif RM == '101':
                reg1='EBP'
            elif RM == '110':
                reg1='ESI'
            elif RM == '111':
                reg1='EDI'
        if r1==2:
            if RM == '000':
                reg1='AX'
            elif RM == '001':
                reg1='CX'
            elif RM == '010':
                reg1='DX'
            elif RM == '011':
                reg1='BX'
            elif RM == '100':
                reg1='SP'
            elif RM == '101':
                reg1='BP'
            elif RM == '110':
                reg1='SI'
            elif RM == '111':
                reg1='DI'
        if r1==1:
            if RM == '000':
                reg1='AL'
            elif RM == '001':
                reg1='CL'
            elif RM == '010':
                reg1='DL'
            elif RM == '011':
                reg1='BL'
            elif RM == '100':
                reg1='AH'
            elif RM == '101':
                reg1='CH'
            elif RM == '110':
                reg1='DH'
            elif RM == '111':
                reg1='BH'
        if r1==5: #MM
            if RM == '000':
                reg1='MM0'
            elif RM == '001':
                reg1='MM1'
            elif RM == '010':
                reg1='MM2'
            elif RM == '011':
                reg1='MM3'
            elif RM == '100':
                reg1='MM4'
            elif RM == '101':
                reg1='MM5'
            elif RM == '110':
                reg1='MM6'
            elif RM == '111':
                reg1='MM7'
        if r1==6: #XMM
            if RM == '000':
                reg1='XMM0'
            elif RM == '001':
                reg1='XMM'
            elif RM == '010':
                reg1='XMM2'
            elif RM == '011':
                reg1='XMM3'
            elif RM == '100':
                reg1='XMM4'
            elif RM == '101':
                reg1='XMM5'
            elif RM == '110':
                reg1='XMM6'
            elif RM == '111':
                reg1='XMM7'

    if Mod != '11':
        if RM == '000':
            reg1='EAX'
        elif RM == '001':
            reg1='ECX'
        elif RM == '010':
            reg1='EDX'
        elif RM == '011':
            reg1='EBX'
        #elif RM == '100':
            #reg1='ESP'
        elif RM == '101':
            reg1='EBP'
        elif RM == '110':
            reg1='ESI'
        elif RM == '111':
            reg1='EDI'

    if Mod == '00' and RM == '101':
        t1=opcode[1+has_sib:1+has_sib+3]
        t1=struct.unpack('<i',t1)[0]
        t2=hex(t1)
        if t2>0:
            reg1='+'+t2

    if r2==4:
        if Reg == '000':
            reg4='EAX'
        elif Reg == '001':
            reg4='ECX'
        elif Reg == '010':
            reg4='EDX'
        elif Reg == '011':
            reg4='EBX'
        elif Reg == '100':
            reg4='ESP'
        elif Reg == '101':
            reg4='EBP'
        elif Reg == '110':
            reg4='ESI'
        elif Reg == '111':
            reg4='EDI'
    if r2==2:
        if Reg == '000':
            reg4='AX'
        elif Reg == '001':
            reg4='CX'
        elif Reg == '010':
            reg4='DX'
        elif Reg == '011':
            reg4='BX'
        elif Reg == '100':
            reg4='SP'
        elif Reg == '101':
            reg4='BP'
        elif Reg == '110':
            reg4='SI'
        elif Reg == '111':
            reg4='DI'
    if r2==1:
        if Reg == '000':
            reg4='AL'
        elif Reg == '001':
            reg4='CL'
        elif Reg == '010':
            reg4='DL'
        elif Reg == '011':
            reg4='BL'
        elif Reg == '100':
            reg4='AH'
        elif Reg == '101':
            reg4='CH'
        elif Reg == '110':
            reg4='DH'
        elif Reg == '111':
            reg4='BH'
    if r2==5: #MM
        if Reg == '000':
            reg4='MM0'
        elif Reg == '001':
            reg4='MM'
        elif Reg == '010':
            reg4='MM2'
        elif Reg == '011':
            reg4='MM3'
        elif Reg == '100':
            reg4='MM4'
        elif Reg == '101':
            reg4='MM5'
        elif Reg == '110':
            reg4='MM6'
        elif Reg == '111':
            reg4='MM7'
    if r2==6: #XMM
        if Reg == '000':
            reg4='XMM0'
        elif Reg == '001':
            reg4='XMM'
        elif Reg == '010':
            reg4='XMM2'
        elif Reg == '011':
            reg4='XMM3'
        elif Reg == '100':
            reg4='XMM4'
        elif Reg == '101':
            reg4='XMM5'
        elif Reg == '110':
            reg4='XMM6'
        elif Reg == '111':
            reg4='XMM7'

    ret_byte=1+has_sib
    if RM=='101' and Mod=='00':
        ret_byte=ret_byte+4
    elif Mod=='01':
        ret_byte=ret_byte+1
    elif Mod=='10':
        ret_byte-ret_byte+4
            


    if has_sib == 0:
        if Mod == '11':
            if E:
                return reg4+','+reg1,ret_byte
            else:
                return reg1+','+reg4,ret_byte
        else:
            if E:
                return reg4+','+'['+reg1+plus+']',ret_byte
            else:
                return '['+reg1+plus+']'+','+reg4,ret_byte
            
    elif has_sib == 1:
        ret = sib(opcode[1],Mod)
        if E:
            return reg4+','+'['+reg1+ret+plus+']',ret_byte
        else:
            return '['+reg1+ret+plus+']'+','+reg4,ret_byte

def sib(s,Mod): #reg1 * reg1_x + reg2 형태를 띄게 된다.
    reg1=''
    reg1_x=''
    reg2=''
    plus='+'
    b=bin(int(s.encode('hex'),16))[2:]
    for x in range(8-len(b)):
        b='0'+b
    scale=b[0:2]
    index=b[2:5]
    base=b[5:8]

    if scale == '00':
        reg1_x=''
    elif scale =='01':
        reg1_x='*2'
    elif scale == '10':
        reg1_x='*4'
    elif scale == '11':
        reg1_x = '*8'

    if index == '000':
        reg1='EAX'
    elif index == '001':
        reg1='ECX'
    elif index == '010':
        reg1='EDX'
    elif index == '011':
        reg1='EBX'
    elif index == '100':
        reg1_x=''
        reg1=''
        plus=''
    elif index == '101':
        reg1='EBP'
    elif index == '110':
        reg1='ESI'
    elif index == '111':
        reg1='EDI'

    if base == '000':
        reg2='EAX'
    elif base == '001':
        reg2='ECX'
    elif base == '010':
        reg2='EDX'
    elif base == '011':
        reg2='EBX'
    elif base == '100':
        reg2='ESP'
    elif base == '101':
        if Mod=='00':
            reg2=''
        else:
            reg2='EBP'
    elif base == '110':
        reg2='ESI'
    elif base == '111':
        reg2='EDI'

    return reg1 + reg1_x + plus +reg2
   