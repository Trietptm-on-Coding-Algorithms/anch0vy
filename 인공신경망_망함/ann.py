# -*- coding: cp949 -*-
from __future__ import division
import math
import random
import pprint


def sigmoid(a):
    #�ñ׸��̵� �Լ��� tanh �Լ� ���
    return math.tanh(a)/2 + 0.5

def rand(a, b):
    # a <= rand < b
    return (b-a)*random.random() + a

def nn_activation(nn_input,nn_weight,bias = -1):
    #nn_input �� nn_weight �� ����Ʈ
    if len(nn_input) != len(nn_weight)-1:
        print '�Է°��� ����ġ�� ���� ���� ����'
        exit()
    nn_len = len(nn_input) + 1
    nn_input = nn_input + [bias]
    activation = 0
    for n in range(nn_len):
        activation = activation + nn_input[n] * nn_weight[n]
    return sigmoid(activation)

############����###############
#nn_input = [1,0,1,1,0]
#nn_weight = [0.5,-0.2,-0.3,0.9,0.1]
#test = nn_activation(nn_input,nn_weight)
#print test
#���⼭ test�� 1.1 �� �Ǿ�� �Ѵ�
############����###############

def make_list(m,n):
    #���� �뵵�� ����� ����Ʈ(2���� �迭)
    #n �� ���� m�� ����
    l1 = []
    l2 = []
    for tmp1 in range(n):
        for tmp2 in range(m):
            l2 = l2 + [0]
        l1.append(l2)
        l2 = []
    return l1

############����###############
#import pprint
#t = make_list(4,7)
#pprint.pprint(t)
#���
#[[0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0]]
############����###############

def make_nn(n_input,n_hidden,n_output,init_weight = 0.2):
    #�Է°��� �� , ���緹�̾��� ������, ����� ��, �ʱ� ����ġ ���� ����
    #����ġ�� ���� �������� å��
    nn_hidden = make_list(n_input+1,n_hidden)
    nn_output = make_list(n_hidden+1,n_output)
    for a in range(n_input+1):
        for b in range(n_hidden):
            nn_hidden[b][a] = rand(-init_weight,init_weight)
    for a in range(n_hidden+1):
        for b in range(n_output):
            nn_output[b][a] = rand(-init_weight,init_weight)    
    return [nn_hidden,nn_output]


def cpu(l_input,l_nn):
    tmp1 = []
    for x in l_nn[0]:
        tmp1 = tmp1 + [nn_activation(l_input,x)]
    print tmp1
    tmp2 = []
    for x in l_nn[1]:
        tmp2 = tmp2 + [nn_activation(tmp1,x)]
    print tmp2

def fix(l_input,l_answer,l_hidden,l_output,l_nn,alpha = 0.1):
    #�Է°� ����Ʈ,���丮��Ʈ,���緹�̾��� ��°�����Ʈ,���� ������� ��¸���Ʈ,����,�ΰ���
    #����ġ ����, ���ϰ��� l_nn
    #���� ���-���� ����ġ ����
    error_out = []
    for x in range(len(l_answer)):
        error_out = error_out + [(l_answer[x] - l_output[x]) * l_output[x] * (1 - l_output[x])]
        print 'error_out -> ',error_out
        for y in range(len(l_nn[1][x])):#y���� ����ġ�� ��ȣ? �� �� ����
            l_nn[1][x][y] = l_nn[1][x][y] + alpha * error_out[x] * l_hidden[y] #����ġ ����
    #�������� �Է�-���� ����ġ ����
    for x in range(len(l_nn[0])):#���緹�̾��� ������
        #���� = ������ ���(1-������ ���) * �ñ׸�(1~��´����� ��)(��´����� ����*���紺���� ��´����� ����ġ)
        sum = 0
        for tmp in range(len(error_out)):
            sum = sum + error_out[tmp] * l_nn[1][tmp][x]
        error_hidden = error_out[x] * (1 - error_out[x]) * sum
        print 'error_hidden -> ',error_hidden
        for y in range(len(
            
            
            
            
        error_hidden = l_hidden[x] * (1 - l_hidden[x])
        

    
    return l_nn


def train(l_input,l_answer):
    
