# -*- coding: utf8-*-

#print a[0].encode('cp949')

import xlrd
book_name = raw_input('엑셀파일: ')
save = raw_input('저장할 곳: ')
save = open(save,'wb')
book = xlrd.open_workbook(book_name)
sheet = book.sheet_by_index(4)
hira = ''
kanji = ''
hangul = ''
for a in range(2,2301):
    print a
    hira = sheet.cell_value(rowx=a,colx=0)
    kanji = sheet.cell_value(rowx=a,colx=1)
    hangul = sheet.cell_value(rowx=a,colx=2)
    if type(hangul) == float:
        print 'passsssssssss'
    else:
        if kanji == '':
            wr = hira + ' ||' + hangul + '\n'
        else:
            wr = kanji + ' ' +  hira + ' ||' + hangul + '\n'
        save.write(wr.encode('utf-8'))
    

    
