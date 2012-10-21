import subprocess
import os
import urllib
from PIL import Image
program = os.path.abspath('gocr049.exe')
if not os.path.exists(program):
    print '[!]No gocr049.exe'
    print '[*]Plz download at http://www-e.uni-magdeburg.de/jschulen/ocr/gocr049.exe'
    exit(-1)
image_url = raw_input('image url: ')
image_url = image_url.replace('dtype=4','dtype=100000')
key =  image_url.split('key=')[1].split('&')[0]
answer = {}#input capcha strings
n = 0
print key #debug
capcha_f = os.getcwd() + '\\' + 'capcha'
if not os.path.exists(capcha_f):
    os.mkdir(capcha_f)
while n < 200:
    n = n+1
    if n%50==0:
        print '[*]',n,'th capcha processing...'
    name = capcha_f + '\\' + key +'_'+ str(n) +'.gif'
    f = open(name,'wb')
    tmp = urllib.urlopen(image_url)
    f.write(tmp.read())
    f.close()
    im = Image.open(name)
    im.convert('L').save(name+'.ppm','ppm')
    t = subprocess.check_output(program + ' -i ' + name+'.ppm',shell=True)
    t = t.replace('\r\n','')
    t = t.replace(' ','')
    t = t.replace('_','')
    t = t.upper()
    if len(t) == 6:
        print t
        try:
            answer[t] = answer[t] + 1
        except KeyError:
            answer[t] = 1
print answer
raw_input('end')
