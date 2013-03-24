# -*- coding: cp949 -*-
from __future__ import division
import math
import random

# �̰� lff �Ҷ� �����ʿ��� �������� ���°ſ���....
# ���� �Է� ���� ��� 3���� ��
# ������ �ڽ��� bias �� ������ ��ȣ�� ����ġ���鿡 ���� ������ ������ �ִ�
# �Է��� ������ �迭
# �������� ��Ÿ���� �迭
# ������� ��Ÿ���� �迭
# ����� ������ �迭
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
        self.alpha = alpha #�󸶳� �ΰ��ϰ� �н��� ���� �����ϴ� ���
        self.do = [0]*no

        self.lih = clist(self.ni,self.nh)
        self.lho = clist(self.nh,self.no)

        self.oi = [0.0]*self.ni
        self.oh = [0.0]*self.nh
        self.oo = [0.0]*self.no
        self.answer = [0.0]*self.no #�̰� �Ʒÿ� ���� ����

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
            self.do[x] = dsigmoid(sum)#�Ʒ� ����-����� ���� ���

    def lff(self):
        #���� ����-����� ���
        self.s_delta=[0]*self.nh #��Ÿ���� ��
        self.s_error=0 #������ ��ǥ
        for x in range(self.no):
            error = self.do[x] - self.oo[x]
            self.s_error = self.s_error + error**2
            for y in range(self.nh):
                s_delta = 0.0
                delta = self.oo[x] * (1-self.oo[x])*error
                self.s_delta[y] = s_delta + delta*self.lho[y][x] #�Է�-���� ������ ���� ��ĥ�� ���
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
                    print '���� ����:',self.s_error

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
