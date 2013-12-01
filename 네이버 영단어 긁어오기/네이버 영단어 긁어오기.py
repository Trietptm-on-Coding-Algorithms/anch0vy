import urllib
import re
#소스 개그지임 누가 정규식 잘 쓰는법좀 알려줘...
#원래는 바로바로 write()를 해야 하나 이미 소스 다 짜고 file 부분 추가함 귀찮이즘 쩌네
#페이지 넘버는 1부터 195 까지 있음
#<span class="e_19_a" lang="en">단어</span>
#<td class="f_con">링크 포함 단어뜻 </td>
#<i class여기삭제</i>
#<img src=여기삭제/> 

#\x0a \x0d \x09

word_list=[]
mean_list=[]
f=open('D:\\dic_start_1.txt','w')

for y in range(1,434):
        page='http://endic.naver.com/rank.nhn?pubLev=1&firstWord=all&posp=all&pageNo='+str(y)
        p=urllib.urlopen(page)
        p=p.read()
        #쓸대없는 애들 제거
        p=re.sub('''<i class?(.*?)value="''','',p)
        ##없어도 잘만 된다##p=re.sub('''" lang="en">?(.*?)</i>''','',p)
        ##없어도 잘만 된다##p=re.sub('''">?(.*?)</i>''','',p)
        p=re.sub('''<img src=?(.*?)/>''','',p)
        ##없어도 잘만 된다##p=p.replace('''<img src=''','')
        
        #단어랑 뜻 뽑아온다
        tmp_word=re.findall('''<span class="e_19_a" lang="en">?(.*?)</span>''',p,re.DOTALL)
        tmp_mean=re.findall('''<td class="f_con">?(.*?)</td>''',p,re.DOTALL)

        word_list=word_list+tmp_word
        
        for x in tmp_mean:
                x=x.replace('\x0a','')
                x=x.replace('\x0d','')
                x=x.replace('\x09','')
                x=x.replace('\x20\x20','')
                x=x.replace('''<span class="itt_button">''','')
                x=x.replace('''<span class="fnt_k10">''','')
                x=x.replace('''<span class="fnt_e19" lang="en">''',' ')
                x=re.sub('''">?(.*?)</i>''',' ',x)
                x=x.replace('''<img src=''','')
                x=x.replace('''</span>''','')
                x=x.replace('<b>','')
                x=x.replace('</b>','')
                mean_list=mean_list+[x]
        for x in range(len(mean_list)):
                f.write(word_list[x]+'\t'+mean_list[x]+'\n')
        f.flush()
        mean_list,word_list=([],[])
        print 'page: ',str(y)
f.close()
print 'end'
        
