# -*- coding: cp949 -*-
from __future__ import division
import math
import random
import pprint


def sigmoid(a):
    #시그모이드 함수로 tanh 함수 사용
    return math.tanh(a)

def rand(a, b):
    # a <= rand < b
    return (b-a)*random.random() + a

def nn_activation(nn_input,nn_weight):
    #nn_input 과 nn_weight 는 리스트
    if len(nn_input) != len(nn_weight):
        exit()
    nn_len = len(nn_input)
    activation = 0
    for n in range(nn_len):
        activation = activation + nn_input[n] * nn_weight[n]
    return activation

############예제###############
#nn_input = [1,0,1,1,0]
#nn_weight = [0.5,-0.2,-0.3,0.9,0.1]
#test = nn_activation(nn_input,nn_weight)
#print test
#여기서 test는 1.1 이 되어야 한다
############예제###############

def make_list(m,n):
    #여러 용도로 만드는 리스트(2차원 배열)
    #n 은 세로 m은 가로
    l1 = []
    l2 = []
    for tmp1 in range(n):
        for tmp2 in range(m):
            l2 = l2 + [0]
        l1.append(l2)
        l2 = []
    return l1

############예제###############
#import pprint
#t = make_list(4,7)
#pprint.pprint(t)
#결과
#[[0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0]]
############예제###############

def make_nn(n_input,n_hidden,n_output,init_weight):
    #입력, 히든레이어의 뉴런수, 출력의 수, 초기 가중치 랜덤 범위
    #가중치는 대충 랜덤으로 책정
    nn_hidden = make_list(n_input,n_hidden) #히든 레이어의 뉴런의 가중치
    nn_output = make_list(n_hidden,n_output) #출력 뉴런의 가중치
    #가중치 랜덤으로 초기화
    for a in range(n_input):
        for b in range(n_hidden):
            nn_hidden[b][a] = rand(-init_weight,init_weight)
    for a in range(n_hidden):
        for b in range(n_output):
            nn_output[b][a] = rand(-init_weight,init_weight)


