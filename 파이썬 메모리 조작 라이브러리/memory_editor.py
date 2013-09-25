# -*- coding: cp949 -*-
from winapi import *
import struct

sys_info=wGetSystemInfo()
min_address=sys_info.lpMinimumApplicationAddress
max_address=sys_info.lpMaximumApplicationAddress
CAN_NOT_CHANGE=0x13#PAGE_NOACCESS|PAGE_READONLY|PAGE_EXECUTE

def check_writeable(info):
    if info.State == MEM_COMMIT and info.Protect&CAN_NOT_CHANGE == 0:
        return [info.BaseAddress,info.RegionSize]
    else:
        return 0

class memory_edit:
    def __init__(self,pid):
        self.pid=pid
        self.h=0 #핸들
        self.writeable_memory=[] #수정 가능한 메모리 맵
        self.h=wOpenProcess(pid)
        self.mmap=[]#찾은 메모리 값들 [[주소,값],[주소,값],...]의 형태를 가짐
        a=min_address
        while a<max_address:
            info=wVirtualQueryEx(self.h,a)
            a=a+info.RegionSize
            t=check_writeable(info)
            if t:
                self.writeable_memory = self.writeable_memory+[check_writeable(info)]
                
    def new_find_4byte(self,v):#v=value
        self.mmap=[]
        v2=v
        v=struct.pack('<I',v)
        for x in self.writeable_memory:
            tmp=wReadProcessMemory(self.h,x[0],x[1])
            tmp2=tmp.find(v)
            s=0
            while tmp2>=0:
                self.mmap=self.mmap + [[x[0]+tmp2,v2]]
                s=tmp2+4
                tmp2=tmp.find(v,s)

    def next_find_4byte(self,v):
        v2=v
        v=struct.pack('<I',v)
        mmap=self.mmap
        self.mmap=[]
        for x in mmap:
            tmp=wReadProcessMemory(self.h,x[0],4)
            if tmp == v:
                self.mmap=self.mmap+[[x[0],v2]]
    def change_value(self,start_address,value):
        value=struct.pack('<I',value)
        wWriteProcessMemory(self.h,start_address,value)
            


