# -*- coding: cp949 -*-
from vm_opcode import *
from opcode_parse_util import *
import random

########예제########
#r0 = 123
#r0 = r1 +,-,*,/,^,&,| r2
#r0 = r1
###################


def l_strip(_list):
    r = []
    for t in _list:
        r = r + [t.lstrip().strip()]
    return r
        
def parser(code):
    o_code = code
    code = code.split('=')
    code = l_strip(code)
    save = code[0]
    code = code[1]
    print code
    
    if code.count('+') == 1:
        cmd = c_sum
        code = code.split('+')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('-') == 1:
        cmd = c_sub
        code = code.split('-')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('*') == 1:
        cmd = c_mul
        code = code.split('*')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('/') == 1:
        cmd = c_div
        code = code.split('/')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('^') == 1:
        cmd = c_xor
        code = code.split('^')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('&') == 1:
        cmd = c_and
        code = code.split('&')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]
        
    elif code.count('|') == 1:
        cmd = c_or
        code = code.split('|')
        code = l_strip(code)
        f_operand = code[0]
        s_operand = code[1]

    elif code.count('r') == 1:
        cmd = c_eq
        f_operand = code.strip().lstrip()
        s_operand = 'r' + str(random.randrange(0, 16))

    else:
        print 'error: ',o_code
        exit()

    save = int(save.split('r')[1])
    f_operand = int(f_operand.split('r')[1])
    s_operand = int(s_operand.split('r')[1])
    opcode = make_opcode(cmd,save,f_operand,s_operand)
    return hex(opcode)
