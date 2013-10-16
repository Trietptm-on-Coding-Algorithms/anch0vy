# -*- coding: cp949 -*-
import two_byte_opcode
from util import *
from engine_util import *
import struct 
def asmgen(opcode,bit):
    if opcode[0]=='\x00':
        if bit==32:
            return Eb_Gb(opcode,'ADD',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x01':
        if bit==32:
            return Ev_Gv(opcode,'ADD',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x02':
        if bit==32:
            return Gb_Eb(opcode,'ADD',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x03':
        if bit==32:
            return Gv_Ev(opcode,'ADD',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x04':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'ADD AL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x05':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'ADD EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x06':
        if bit==32:
            return 'PUSH ES',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x07':
        if bit==32:
            return 'POP ES',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x08':
        if bit==32:
            return Eb_Gb(opcode,'OR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x09':
        if bit==32:
            return Ev_Gv(opcode,'OR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x0a':
        if bit==32:
            return Gb_Eb(opcode,'OR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x0b':
        if bit==32:
            return Gv_Ev(opcode,'OR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x0c':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'OR AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x0d':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'OR EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x0e':
        if bit==32:
            return 'PUSH CS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x0f': #two byte opcode
        return two_byte_opcode.asmgen(opcode,bit)


    elif opcode[0]=='\x10':
        if bit==32:
            return Eb_Gb(opcode,'ADC',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x11':
        if bit==32:
            return Ev_Gv(opcode,'ADC',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x12':
        if bit==32:
            return Gb_Eb(opcode,'ADC',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x13':
        if bit==32:
            return Gv_Ev(opcode,'ADC',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x14':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'ADC AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x15':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'ADC EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x16':
        if bit==32:
            return 'PUSH SS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x17':
        if bit==32:
            return 'POP SS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x18':
        if bit==32:
            return Eb_Gb(opcode,'SBB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x19':
        if bit==32:
            return Ev_Gv(opcode,'SBB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x1a':
        if bit==32:
            return Gb_Eb(opcode,'SBB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x1b':
        if bit==32:
            return Gv_Ev(opcode,'SBB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x1c':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'SBB AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x1d':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'SBB EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x1e':
        if bit==32:
            return 'PUSH DS',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x1f':
        if bit==32:
            return 'POP DS',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x20':
        if bit==32:
            return Eb_Gb(opcode,'AND',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x21':
        if bit==32:
            return Ev_Gv(opcode,'AND',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x22':
        if bit==32:
            return Gb_Eb(opcode,'AND',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x23':
        if bit==32:
            return Gv_Ev(opcode,'AND',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x24':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'ANC AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x25':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'ANC EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x26':
        if bit==32:
            return 'prefix SEG=ES',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x27':
        if bit==32:
            return 'DAA',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x28':
        if bit==32:
            return Eb_Gb(opcode,'SUB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x29':
        if bit==32:
            return Ev_Gv(opcode,'SUB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x2a':
        if bit==32:
            return Gb_Eb(opcode,'SUB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x2b':
        if bit==32:
            return Gv_Ev(opcode,'SUB',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x2c':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'SUB AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x2d':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'SUB EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x2e':
        if bit==32:
            return 'prefix SEG=CS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x2f':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x30':
        if bit==32:
            return Eb_Gb(opcode,'XOR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x31':
        if bit==32:
            return Ev_Gv(opcode,'XOR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x32':
        if bit==32:
            return Gb_Eb(opcode,'XOR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x33':
        if bit==32:
            return Gv_Ev(opcode,'XOR',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x34':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'XOR AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x35':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'XOR EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x36':
        if bit==32:
            return 'prefix SEG=SS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x37':
        if bit==32:
            return 'AAA',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x38':
        if bit==32:
            return Eb_Gb(opcode,'CMP',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x39':
        if bit==32:
            return Ev_Gv(opcode,'CMP',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x3a':
        if bit==32:
            return Gb_Eb(opcode,'CMP',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x3b':
        if bit==32:
            return Gv_Ev(opcode,'CMP',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x3c':
        if bit==32:
            ret=unpack_us1(opcode[1])[0]
            return 'CMP AL,'+str(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x3d':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'CMP EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x3e':
        if bit==32:
            return 'prefix SEG=DS',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x3f':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x40':
        if bit==32:
            return 'INC EAX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x41':
        if bit==32:
            return 'INC ECX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x42':
        if bit==32:
            return 'INC EDX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x43':
        if bit==32:
            return 'INC EBX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x44':
        if bit==32:
            return 'INC ESP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x45':
        if bit==32:
            return 'INC EBP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x46':
        if bit==32:
            return 'INC ESI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x47':
        if bit==32:
            return 'INC EDI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x48':
        if bit==32:
            return 'DEC EAX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x49':
        if bit==32:
            return 'DEC ECX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4a':
        if bit==32:
            return 'DEC EDX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4b':
        if bit==32:
            return 'DEC EBX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4c':
        if bit==32:
            return 'DEC ESP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4d':
        if bit==32:
            return 'DEC EBP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4e':
        if bit==32:
            return 'DEC ESI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x4f':
        if bit==32:
            return 'DEC EDI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x50':
        if bit==32:
            return 'PUSH EAX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x51':
        if bit==32:
            return 'PUSH ECX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x52':
        if bit==32:
            return 'PUSH EDX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x53':
        if bit==32:
            return 'PUSH EBX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x54':
        if bit==32:
            return 'PUSH ESP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x55':
        if bit==32:
            return 'PUSH EBP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x56':
        if bit==32:
            return 'PUSH ESI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x57':
        if bit==32:
            return 'PUSH EDI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x58':
        if bit==32:
            return 'POP EAX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x59':
        if bit==32:
            return 'POP ECX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5a':
        if bit==32:
            return 'POP EDX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5b':
        if bit==32:
            return 'POP EBX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5c':
        if bit==32:
            return 'POP ESP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5d':
        if bit==32:
            return 'POP EBP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5e':
        if bit==32:
            return 'POP ESI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x5f':
        if bit==32:
            return 'POP EDI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x60':
        if bit==32:
            return 'PUSHAD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x61':
        if bit==32:
            return 'POPAD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x62':#BOUND 뒤의 Ma가 문제 있음 앞의 크기의 2배 ㄷㄷ
        if bit==32:
            ret,ret_byte=ModRM32(opcode[1:],4,4,E=1)
            return 'BOUND '+ret,opcode[1+ret_byte:]
        elif bit==64:
            pass


    elif opcode[0]=='\x63':
        if bit==32:
            ret,ret_byte=ModRM32(opcode[1:],2,2,E=0)
            return 'ARPL '+ret,opcode[1+ret_byte:]
        elif bit==64:
            pass


    elif opcode[0]=='\x64':#prefix
        if bit==32:
            return 'prefix SEG=FS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x65':
        if bit==32:
            return 'prefix SEG=GS',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x66':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x67':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x68':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'PUSH '+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\x69':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6a':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'PUSH '+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6b':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6c':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6d':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6e':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x6f':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x70':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JO $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x71':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JNO $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x72':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JB $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x73':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JNB $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x74':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x75':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JNE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x76':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JBE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x77':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JA $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x78':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JNS $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x79':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JPE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7a':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JPO $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7b':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JNGE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7c':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JGE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7d':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JLE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7e':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JG $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\x7f':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x80':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x81':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x82':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x83':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x84':
        if bit==32:
            return Eb_Gb(opcode,'TEST',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x85':
        if bit==32:
            return Ev_Gv(opcode,'TEST',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x86':
        if bit==32:
            return Eb_Gb(opcode,'XCHG',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x87':
        if bit==32:
            return Ev_Gv(opcode,'XCHG',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x88':
        if bit==32:
            return Eb_Gb(opcode,'MOV',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x89':
        if bit==32:
            return Ev_Gv(opcode,'MOV',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x8a':
        if bit==32:
            return Gb_Eb(opcode,'MOV',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x8b':
        if bit==32:
            return Gv_Ev(opcode,'MOV',1)
        elif bit==64:
            pass


    elif opcode[0]=='\x8c':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x8d':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x8e':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x8f':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x90':
        if bit==32:
            return 'NOP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x91':
        if bit==32:
            return 'XCHG EAX,ECX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x92':
        if bit==32:
            return 'XCHG EAX,EDX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x93':
        if bit==32:
            return 'XCHG EAX,EBX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x94':
        if bit==32:
            return 'XCHG EAX,ESP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x95':
        if bit==32:
            return 'XCHG EAX,EBP',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x96':
        if bit==32:
            return 'XCHG EAX,ESI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x97':
        if bit==32:
            return 'XCHG EAX,EDI',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x98':
        if bit==32:
            return 'CWDE',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x99':
        if bit==32:
            return 'CDQ',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9a':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9b':
        if bit==32:
            return 'WAIT',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9c':
        if bit==32:
            return 'PUSHFD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9d':
        if bit==32:
            return 'POPFD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9e':
        if bit==32:
            return 'SAHF',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\x9f':
        if bit==32:
            return 'LAHF',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa0':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'MOV AL,'+hex(ret),opcode[1+4:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa1':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa2':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'MOV ['+hex(ret)+'],AL',opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa3':
        if bit==32:
            ret=unpack_us4(opcode[1:5])[0]
            return 'MOV ['+hex(ret)+'],EAX',opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa4':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa5':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa6':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa7':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa8':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'TEST AL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xa9':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'TEST EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xaa':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xab':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xac':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xad':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xae':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xaf':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb0':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV AL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb1':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV CL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb2':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV DL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb3':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV BL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb4':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV AH,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb5':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV AH,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb6':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV AH,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb7':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'MOV AH,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb8':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EAX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xb9':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV ECX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xba':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EDX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xbb':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EBX,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xbc':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV ESP,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xbd':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EBP,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xbe':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV ESI,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xbf':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'MOV EDI,'+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc0':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc1':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc2':
        if bit==32:
            ret = unpack_us2(opcode[1:3])
            return 'RETN '+hex(ret),opcode[3:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc3':
        if bit==32:
            return 'RETN',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc4':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc5':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc6':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc7':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc8':
        if bit==32:
            ret1=unpack_us2(opcode[1:3])
            ret2=unpack_us1(opcode[3])
            return 'ENTER '+hex(ret1)+','+hex(ret2),opcode[4:]
        elif bit==64:
            pass


    elif opcode[0]=='\xc9':
        if bit==32:
            return 'LEAVE',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xca':
        if bit==32:
            ret=unpack_us2(opcode[1:3])
            return 'RETF '+hex(ret),opcode[3:]
        elif bit==64:
            pass


    elif opcode[0]=='\xcb':
        if bit==32:
            return 'RETF',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xcc':
        if bit==32:
            return 'INT3',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xcd':
        if bit==32:
            ret=unpack_us1(opcode[1])
            return 'INT ',opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xce':
        if bit==32:
            return 'INTO',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xcf':
        if bit==32:
            return 'IRETD',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd0':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd1':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd2':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd3':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd4':
        if bit==32:
            return 'AAM',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd5':
        if bit==32:
            return 'AAD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd6': #undocument opcode 라는데... 
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd7':
        if bit==32:
            return 'XLAT',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd8':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xd9':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xda':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xdb':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xdc':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xdd':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xde':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xdf':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe0':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'LOOPNE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe1':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'LOOPE $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe2':
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'LOOP $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe3':#이름??
        if bit==32:
            ret=unpack_s1(opcode[1])+2
            return 'JECXZ $'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe4':
        if bit==32:
            ret=unpack_s1(opcode[1])
            return 'IN AL,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe5':
        if bit==32:
            ret=unpack_s1(opcode[1])
            return 'IN EAX,'+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe6':
        if bit==32:
            ret=unpack_s1(opcode[1])
            return 'OUT '+hex(ret)+',AL',opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe6':
        if bit==32:
            ret=unpack_s1(opcode[1])
            return 'OUT '+hex(ret)+',EAX',opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe7':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe8':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'CALL '+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xe9':
        if bit==32:
            ret=unpack_us4(opcode[1:5])
            return 'JMP near '+hex(ret),opcode[5:]
        elif bit==64:
            pass


    elif opcode[0]=='\xea':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xeb':
        if bit==32:
            ret=unpack_us1(opcode[1])+2
            return 'JMP short '+hex(ret),opcode[2:]
        elif bit==64:
            pass


    elif opcode[0]=='\xec':
        if bit==32:
            return 'IN AL,DX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xed':
        if bit==32:
            return 'IN EAX,DX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xee':
        if bit==32:
            return 'OUT DX,AL',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xef':
        if bit==32:
            return 'OUT DX,EAX',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf0':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf1':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf2':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf3':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf4':
        if bit==32:
            return 'HLT',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf5':
        if bit==32:
            return 'CMC',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf6':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf7':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf8':
        if bit==32:
            return 'CLC',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xf9':
        if bit==32:
            return 'STC',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xfa':
        if bit==32:
            return 'CLI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xfb':
        if bit==32:
            return 'STI',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xfc':
        if bit==32:
            return 'CLD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xfd':
        if bit==32:
            return 'STD',opcode[1:]
        elif bit==64:
            pass


    elif opcode[0]=='\xfe':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass


    elif opcode[0]=='\xff':
        if bit==32:
            return 'xxx',opcode[:]
        elif bit==64:
            pass
  
