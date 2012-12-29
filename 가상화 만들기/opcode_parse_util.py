# -*- coding: cp949 -*-
#vmopcode를 받아서 명령어,저장할 곳, 앞 피연산자, 뒤 피연산자 를 각각 분리한다
#문제점: 명령어가 0000 일경우 opcode의 길이가 1.5 바이트가 나옴 ㄷㄷ 근데 그냥 라이트 하면 되나? -> 맨 앞 비트를 1로 설정해서 해결

def get_cmd(opcode):
    opcode = 0b0111000000000000 & opcode
    opcode = opcode / 0b0001000000000000
    return opcode

def get_save(opcode):
    opcode = 0b0000111100000000 & opcode
    opcode = opcode / 0b0000000100000000
    return opcode

def get_f_operand(opcode):
    opcode = 0b0000000011110000 & opcode
    opcode = opcode / 0b000000000010000
    return opcode

def get_s_operand(opcode):
    opcode = 0b0000000000001111 & opcode
    return opcode

def get_opcode(opcode):
    t_opcode = [get_cmd(opcode) + get_save(opcode) + get_f_operand(opcode) + get_s_operand(opcode)]
    return t_opcode

def make_opcode(cmd,save,f_operand,s_operand):
    t_opcode = int(cmd) * 0b0001000000000000 + save * 0b0000000100000000 + f_operand * 0b0000000000010000 + s_operand
    return t_opcode

