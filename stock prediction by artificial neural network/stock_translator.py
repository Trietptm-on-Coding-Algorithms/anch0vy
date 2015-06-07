# -*- coding: cp949 -*-
# 입력 형식: 날자,종가,대비,거래량(주),거래대금(원),시가,고가,저가,시가총액(백만),상장주식수(주)
# 출력 형식: 종가(비율),거래량(최대최소),거래회전율??(거래대금/시가총액,최대최소)


from bpnn import *
import os
import pprint

def WTF1(list_,n):
    #최대 최소값 계산
    min_ = float(list_[0][n])
    max_ = float(list_[0][n])
    for day in range(0,7):
        if min_ > float(list_[day][n]):
            min_ = float(list_[day][n])
        if max_ < float(list_[day][n]):
            max_ = float(list_[day][n])
    return max_,min_

def WTF2(list_,n,m):
    #거래회전율 계산
    min_ = float(list_[0][n])/float(list_[0][m])
    max_ = float(list_[0][n])/float(list_[0][m])
    for day in range(0,7):
        if min_ > float(list_[day][n])/float(list_[day][m]):
            min_ = float(list_[day][n])/float(list_[day][m])
        if max_ < float(list_[day][n])/float(list_[day][m]):
            max_ = float(list_[day][n])/float(list_[day][m])
    return max_,min_


def WTF4(list_,new,max_3,min_3,max_48,min_48):
    #데이터 변환
    for day in range(1,8):
        new[day-1] =[(float(list_[day][1])/float(list_[day-1][1])*10/3)-(0.85*10/3),(float(list_[day][3])-min_3)/(max_3-min_3),(float(list_[day][4])/float(list_[day][8])-min_48)/(max_48-min_48)]
    #pprint.pprint(new)#debug

def join(l_input,l_output):
    tmp = []
    for n in range(6,-1,-1):
        tmp.extend(l_input[n])
    return [[tmp,l_output]]


dir_stock = raw_input('stock folder: ')
stock_num = int(raw_input('stock num: '))
stock_list = os.listdir(dir_stock)
ann = NN(3*7, 30, 1)
#print 'debug info [1]'#debug
for stock_file in stock_list:
    #print 'start training at' + stock_file #debug
    #raw_input()#debug
    f_old   = open(dir_stock +'\\'+ stock_file,'r')
    #print 'debug info [2]'#debug
    trash = f_old.readline().split #예측할 날 버리기 
    day_result = f_old.readline().split(',')   #숫자가 크면 오늘에 가깝고 작으면 과거에 가까움
    day_7 = f_old.readline().split(',')
    day_6 = f_old.readline().split(',')
    day_5 = f_old.readline().split(',')
    day_4 = f_old.readline().split(',')
    day_3 = f_old.readline().split(',')
    day_2 = f_old.readline().split(',')
    day_1 = f_old.readline().split(',')
    day_0 = f_old.readline().split(',')
    day = [day_7,day_6,day_5,day_4,day_3,day_2,day_1,day_0,day_result]
    day_new = [[],[],[],[],[],[],[]]
    try:
        #print 'debug info [3]'#debug
        while 1:
            if not day_0:
                print stock_file + 'end'
                break
            #값 처리 시작
            max_3,min_3 = WTF1(day,3)
            max_48,min_48 = WTF2(day,4,8)
            #print 'debug info [4]'#debug
            #print max_3,min_3,max_48,min_48 #debug
            WTF4(day,day_new,max_3,min_3,max_48,min_48) #계산! day_new에 처리한 값 들거가있음!
            result = [(float(day[0][1])/float(day[1][1])*10/3)-(0.85*10/3)] #예측한 값(결과값)
            trainer = join(day_new,result) #입력에 맞춤
            #print trainer #debug
            #print 'start training...' + day[0][0] #debug
            ####################################################################
            ann.train(trainer,iterations=100,N=0.0001,M=0.00005) #오차 무지 큼
            #ann.train(trainer,iterations=10,N=0.001,M=0.05) #더큼
            #ann.train(trainer,iterations=2,N=0.0001,M=0.00005)
            ####################################################################
            #값 처리 끝
            day_result = day_7[:] #날자 이동하고...
            day_7 = day_6[:]
            day_6 = day_5[:]
            day_5 = day_4[:]
            day_4 = day_3[:]
            day_3 = day_2[:]
            day_2 = day_1[:]
            day_1 = day_0[:]
            day_0 = f_old.readline().split(',')
            if not day_0:
                print stock_file + 'end'
                break
            day = [day_7,day_6,day_5,day_4,day_3,day_2,day_1,day_0,day_result]
            #pprint.pprint(day) #debug
            #raw_input('pause') #debug
            #print 'debug info [5]'#debug
    except IndexError:
        print 'err at' + day[0][0]
f_old.close()        
#print 'save mattrix...'
#mat = open('C:\\Users\\USER\\Desktop\\stock\\mattrix', "w")
#mat.write(showMatrix(ann.wi))
#mat.write(showMatrix(ann.wo))
#mat.close()
print 'THE END!!!!!!!'
#테스트 시작
print 'start test\ngood luck!'
dir_stock = raw_input('test stock folder: ')
stock_num = int(raw_input('test stock num: '))
stock_list = os.listdir(dir_stock)
for stock_file in stock_list:
    f_old = open(dir_stock +'\\'+ stock_file,'r')
    day_result = f_old.readline().split(',')   #숫자가 크면 오늘에 가깝고 작으면 과거에 가까움
    day_7 = f_old.readline().split(',')
    day_6 = f_old.readline().split(',')
    day_5 = f_old.readline().split(',')
    day_4 = f_old.readline().split(',')
    day_3 = f_old.readline().split(',')
    day_2 = f_old.readline().split(',')
    day_1 = f_old.readline().split(',')
    day_0 = f_old.readline().split(',')
    day = [day_7,day_6,day_5,day_4,day_3,day_2,day_1,day_0,day_result]
    day_new = [[],[],[],[],[],[],[],[]]
    max_3,min_3 = WTF1(day,3)
    max_48,min_48 = WTF2(day,4,8)
    #print 'debug info [4]'#debug
    #print max_3,min_3,max_48,min_48 #debug
    WTF4(day,day_new,max_3,min_3,max_48,min_48) #계산! day_new에 처리한 값 들거가있음!
    result = [(float(day[0][1])/float(day[1][1])*10/3)-(0.85*10/3)] #예측한 값(결과값)
    tester = join(day_new,result)
    ann.test_custom(tester,day_7[1],day_result[1],day_7[1])
    #ann.test(tester)

