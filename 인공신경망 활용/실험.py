# -*- coding: cp949 -*-
from __future__ import division
import math
import random
import md5

# �̰� lff �Ҷ� �����ʿ��� �������� ���°ſ���....
# ���� �Է� ���� ��� 3���� ��
# ������ �ڽ��� bias �� ������ ��ȣ�� ����ġ���鿡 ���� ������ ������ �ִ�
# �Է��� ������ �迭
# �������� ��Ÿ���� �迭
# ������� ��Ÿ���� �迭
# ����� ������ �迭


def rand(a, b):
    return (b-a)*random.random() + a

def sigmoid(x):
    return 1/(1+math.e**(-x))

def clist(x,y,fill=0.0):
    m = []
    for i in range(x):
        m.append([fill]*y)
    return m
    

class ann:
    def __init__(self,ni,nh,no,alpha=0.1,moment=1.0):
        self.ni = ni
        self.nh = nh
        self.no = no
        self.alpha = alpha #�󸶳� �ΰ��ϰ� �н��� ���� �����ϴ� ���
        self.do = [0]*no
        self.moment=moment #���Ʈ ���

        self.lih = clist(self.ni,self.nh)
        self.lho = clist(self.nh,self.no)
        self.cih = clist(self.ni,self.nh)#�ٲ�� ���� ��
        self.cho = clist(self.nh,self.no)#�ٲ�� ���� ��

        self.oi = [0.0]*self.ni
        self.oh = [0.0]*self.nh
        self.oo = [0.0]*self.no
        self.answer = [0.0]*self.no #�̰� �Ʒÿ� ���� ����

        for x in range(self.ni):
            for y in range(self.nh):
                self.lih[x][y] = rand(-2.0,2.0)
        for x in range(self.nh):
            for y in range(self.no):
                self.lho[x][y] = rand(-0.2,0.2)

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

    def lff(self):
        output_delta = [0.0] * self.no
        for x in range(self.no):
            error = self.answer[x]-self.oo[x]
            output_delta[x] = self.oo[x] * (1 - self.oo[x]) * error

        hidden_delta = [0.0] * self.nh
        for x in range(self.nh):
            error = 0.0
            for y in range(self.no):
                error = error + output_delta[y] * self.lho[x][y]
            hidden_delta[x] = self.oh[x] * (1 - self.oh[x]) * error

        for x in range(self.nh):
            for y in range(self.no):
                change = output_delta[y] * self.oh[x]
                self.lho[x][y] = self.lho[x][y] + self.alpha*change + self.moment*self.cho[x][y]
                self.cho[x][y] = change

        for x in range(self.ni):
            for y in range(self.nh):
                change = hidden_delta[y] * self.oi[x]
                self.lih[x][y] = self.lih[x][y] + self.alpha*change + self.moment*self.cih[x][y]
                self.cih[x][y] = change

        error = 0.0
        for x in range(self.no):
            error = error + 0.5*(self.answer[x]-self.oo[x])**2
        self.s_error = error
                
    def train(self,pat,num=1000):
        for n in range(num):
            for x in range(len(pat)):
                self.oi = pat[x][0]
                self.answer = pat[x][1]
                self.calc()
                self.lff()
            num = num + 1
            if num % 100 == 0:
                    print '���� ����:',self.s_error

    def test(self,pat):
        for x in range(len(pat)):
            self.oi = pat[x][0]
            self.answer = pat[x][1]
            self.calc()
            print self.oi,' ---> ',self.oo

        
def demo():
    for x in range(1000):
        pat = []
        x = str(x)
        a=md5.md5(x).hexdigest
        for q in range(16):
            qq = '0x' + a[a*2:a*2+1]
            qq = bin(int(qq,16))
        
        
    pat = [[[0,0],[0]],
           [[0,1],[1]],
           [[1,0],[1]],
           [[1,1],[0]]]
    ai=ann(2,5,1)
    ai.train(pat)
    ai.test(pat)
    #print ai.lih,'\n',ai.lho
if __name__ == '__main__':
    demo()
