# -*- coding: cp949 -*-
#vmopcode�� �޾Ƽ� ��ɾ�,������ ��, �� �ǿ�����, �� �ǿ����� �� ���� �и��Ѵ�
#������: ��ɾ 0000 �ϰ�� opcode�� ���̰� 1.5 ����Ʈ�� ���� ���� �ٵ� �׳� ����Ʈ �ϸ� �ǳ�? -> �� �� ��Ʈ�� 1�� �����ؼ� �ذ�

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

