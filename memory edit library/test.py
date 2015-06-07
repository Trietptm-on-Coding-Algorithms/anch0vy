# -*- coding: cp949 -*-
import memory_editor
pid=int(raw_input("pid:"))
test=memory_editor.memory_edit(pid)
a=1
v=int(raw_input('초기 값:'))
test.new_find_4byte(v)
while a:
    v=int(raw_input('바뀐 값:'))
    test.next_find_4byte(v)
    for x in test.mmap:
        print 'address:',x[0],'value',x[1]
    a=int(raw_input("찾는 메모리 값이 없으면 1,있으면 0을 입력:"))
c_a=int(raw_input("바꿀 값의 메모리 주소:"))
c_v=int(raw_input("뭘로 바꾸겠습니까:"))
test.change_value(c_a,c_v)
