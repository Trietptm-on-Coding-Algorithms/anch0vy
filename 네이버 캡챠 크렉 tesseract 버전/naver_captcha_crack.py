import os
import urllib
from PIL import Image
from pytesser import *
def naver_cafe_capcha_crack(image_url):
    image_url = image_url.replace('dtype=4','dtype=100000')
    key =  image_url.split('key=')[1].split('&')[0]
    d_answer = {}#input capcha strings
    n = 0
    capcha_f = os.getcwd()
    names = []
    while n < 15:
        n = n+1
        name = capcha_f + '\\' + key +'_'+ str(n) +'.gif'
        names.append(name)
        f = open(name,'wb')
        tmp = urllib.urlopen(image_url)
        f.write(tmp.read())
        f.close()
        im = Image.open(name)
        t = image_to_string(im)
        t = t.replace('\r','')
        t = t.replace('\n','')
        t = t.upper()
        if t.isalpha():
            if len(t) == 6:
                try:
                    d_answer[t] = d_answer[t] + 1
                except KeyError:
                    d_answer[t] = 1

    answer = ''
    num = 0
    for a,b in d_answer.items():
        if b > num:
            answer = a
            num = b
    im = 'trash' #close image file pointer
    for name in names:
        os.remove(name)
    return answer

if __name__=='__main__':
    url = raw_input('image url: ')
    a = naver_cafe_capcha_crack(url)
    print 'answer is',a
    raw_input('End')
