# -*- coding: cp949 -*-
import memory_editor
pid=int(raw_input("pid:"))
test=memory_editor.memory_edit(pid)
a=1
v=int(raw_input('�ʱ� ��:'))
test.new_find_4byte(v)
while a:
    v=int(raw_input('�ٲ� ��:'))
    test.next_find_4byte(v)
    for x in test.mmap:
        print 'address:',x[0],'value',x[1]
    a=int(raw_input("ã�� �޸� ���� ������ 1,������ 0�� �Է�:"))
c_a=int(raw_input("�ٲ� ���� �޸� �ּ�:"))
c_v=int(raw_input("���� �ٲٰڽ��ϱ�:"))
test.change_value(c_a,c_v)
