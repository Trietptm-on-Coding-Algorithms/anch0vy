# -*- coding: cp949 -*-
from __future__ import division
import math
import random
import pprint


def sigmoid(a):
    #�ñ׸��̵� �Լ��� tanh �Լ� ���
    return math.tanh(a)

def rand(a, b):
    # a <= rand < b
    return (b-a)*random.random() + a

def nn_activation(nn_input,nn_weight):
    #nn_input �� nn_weight �� ����Ʈ
    if len(nn_input) != len(nn_weight):
        exit()
    nn_len = len(nn_input)
    activation = 0
    for n in range(nn_len):
        activation = activation + nn_input[n] * nn_weight[n]
    return activation

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

def make_nn(n_input,n_hidden,n_output,init_weight):
    #�Է�, ���緹�̾��� ������, ����� ��, �ʱ� ����ġ ���� ����
    #����ġ�� ���� �������� å��
    nn_hidden = make_list(n_input,n_hidden) #���� ���̾��� ������ ����ġ
    nn_output = make_list(n_hidden,n_output) #��� ������ ����ġ
    #����ġ �������� �ʱ�ȭ
    for a in range(n_input):
        for b in range(n_hidden):
            nn_hidden[b][a] = rand(-init_weight,init_weight)
    for a in range(n_hidden):
        for b in range(n_output):
            nn_output[b][a] = rand(-init_weight,init_weight)


