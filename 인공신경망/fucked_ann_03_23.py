# -*- coding: cp949 -*-
from __future__ import division
import math
import random

# 이거 lff 할때 오른쪽에서 왼쪽으로 가는거였당....
# 층은 입력 은닉 출력 3개의 층
# 뉴런당 자신의 bias 랑 들어오는 신호의 가중치값들에 대한 정보를 가지고 있다
# 입력을 저장할 배열
# 히든층을 나타내는 배열
# 출력층을 나타내는 배열
# 출력을 저장할 배열
#

def rand(a, b):
    return (b-a)*random.random() + a

def sigmoid(x):
    return 1/(1+math.e**(-x))

def dsigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))

def clist(x,y,fill=0.0):
    m = []
    for i in range(x):
        m.append([fill]*y)
    return m
    

class ann:
    def __init__(self,ni,nh,no,alpha=0.1):
        self.ni = ni
        self.nh = nh
        self.no = no
        self.alpha = alpha #얼마나 민감하게 학습을 할지 결정하는 상수
        self.do = [0]*no

        self.lih = clist(self.ni,self.nh)
        self.lho = clist(self.nh,self.no)

        self.oi = [0.0]*self.ni
        self.oh = [0.0]*self.nh
        self.oo = [0.0]*self.no
        self.answer = [0.0]*self.no #이건 훈련에 사용될 답지

        for x in range(self.ni):
            for y in range(self.nh):
                self.lih[x][y] = rand(-2.4/(self.ni+self.nh+self.no),2.4/(self.ni+self.nh+self.no))
        for x in range(self.nh):
            for y in range(self.no):
                self.lho[x][y] = rand(-2.4/(self.ni+self.nh+self.no),2.4/(self.ni+self.nh+self.no))

    def calc(self):
        for x in range(self.nh):
            sum = 0.0
            for y in range(self.ni):
                sum = sum + self.lih[y][x]*self.oi[y]
            self.oh[x] = sigmoid(sum)

        for x in range(self.no):
            sum = 0.0
            for y in range(self.nh):
                sum = sum + self.lho[y][x]*self.oh[y]
            self.oo[x] = sigmoid(sum)
            self.do[x] = dsigmoid(sum)#아래 은닉-출력층 계산시 사용

    def lff(self):
        #먼저 은닉-출력층 계산
        self.s_delta=[0]*self.nh #델타값의 합
        self.s_error=0 #오차의 지표
        for x in range(self.no):
            error = self.do[x] - self.oo[x]
            self.s_error = self.s_error + error**2
            for y in range(self.nh):
                s_delta = 0.0
                delta = self.oo[x] * (1-self.oo[x])*error
                self.s_delta[y] = s_delta + delta*self.lho[y][x] #입력-은닉 사이의 층을 고칠때 사용
                self.lho[y][x] = self.lho[y][x] + self.alpha * self.lho[y][x] * delta

        for x in range(self.nh):
            for y in range(self.ni):
                delta = self.oh[x] * (1-self.oh[x]) * self.s_delta[x]
                self.lih[y][x] = self.lih[y][x] + self.alpha * self.oi[y] * delta

    def train(self,pat,num=1000):
        for n in range(num):
            for x in range(len(pat)):
                self.oi = pat[x][0]
                self.answer = pat[x][1]
                self.calc()
                self.lff()
                self.calc()
            if num%100 is 0:
                    print '현재 오차:',self.s_error

    def test(self,pat):
        for x in range(len(pat)):
            self.oi = pat[x][0]
            self.answer = pat[x][1]
            self.calc()
            print self.oi,' ---> ',self.oo
        
def demo():
    pat = [[[0,0],[0]],
           [[0,1],[1]],
           [[1,0],[1]],
           [[1,1],[0]]]
    ai=ann(2,5,1)
    ai.train(pat)
    ai.test(pat)
        
if __name__ == '__main__':
    demo()
