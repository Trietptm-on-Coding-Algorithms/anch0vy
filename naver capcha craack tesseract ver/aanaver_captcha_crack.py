# -*- coding: cp949 -*-
import httplib
import os
import urllib
from PIL import Image
from pytesser import *



def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

def lcm(a, b):
  gcd_value = gcd(a, b)
  if (gcd_value == 0): return 0 # 인수가 둘다 0일 때의 에러 처리
  return abs( (a * b) / gcd_value )


url = '''http://xcz.kr/START/prob/prob_files/prob25_img.php'''

headers ={}
headers['Connection']='keep-alive'
headers['User-Agent']='NONE'
headers['Content-Type']='application/x-www-form-urlencoded'
headers['Accept']='*/*'
headers['Accept-Encoding']='deflate'
headers['Accept-Language']='ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
headers['Accept-Charset']='windows-949,utf-8;q=0.7,*;q=0.3'
headers['Host']='xcz.kr'
headers['Cookie']='PHPSESSID=sl7o51hgeog30o1r3bsmcgk016'

f_ = raw_input('img: ')
f = open(f_,'wb')

for qq in range(1000):
    #get img
    f = open(f_,'wb')
    conn=httplib.HTTPConnection('xcz.kr')
    conn.request('GET','/START/prob/prob_files/prob25_img.php',None,headers)
    response = conn.getresponse()
    ii = response.read()
    f.write(ii)
    f.close()
    f = 'trash'
    aa = Image.open(f_)
    txt = image_to_string(aa)
    conn.close()
    try:
        txt = txt.split('LCPI(')[1]
        txt = txt.split(')')[0]
        num1,num2 = txt.split(', ')
        num1 = int(num1)
        num2 = int(num2)
        lcm_ = str(lcm(num1,num2))
        conn=httplib.HTTPConnection('xcz.kr')
        conn.request('GET','/START/prob/prob_files/prob25_ok.php?lcm='+lcm_,None,headers)
        response = conn.getresponse()
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print response.read()
        conn.close()
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    except Exception:
        pass

#send answer

