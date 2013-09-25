# -*- coding: cp949 -*-
from util import *


OpenProcess = windll.kernel32.OpenProcess
OpenProcess.restype = DWORD64
ReadProcessMemory = windll.kernel32.ReadProcessMemory
WriteProcessMemory = windll.kernel32.WriteProcessMemory
GetSystemInfo = windll.kernel32.GetSystemInfo
VirtualQueryEx = windll.kernel32.VirtualQueryEx

'''
SIZE_T WINAPI VirtualQueryEx(
  _In_      HANDLE hProcess,
  _In_opt_  LPCVOID lpAddress,
  _Out_     PMEMORY_BASIC_INFORMATION lpBuffer,
  _In_      SIZE_T dwLength
);
'''
def wOpenProcess(pid):
    return OpenProcess(PROCESS_VM_READ|PROCESS_VM_WRITE|PROCESS_VM_OPERATION|PROCESS_QUERY_INFORMATION,False,pid)

def wReadProcessMemory(handle,start_address,size):
    buff = c_char * size
    buff = buff()
    size = SIZE_T(size)
    address = DWORD64(start_address)
    ReadProcessMemory(handle,address,byref(buff),size,None)
    return buff.raw

def wWriteProcessMemory(handle,start_address,neyong):
    size = SIZE_T(len(neyong))
    buff = c_char_p(neyong)
    address = DWORD64(start_address)
    WriteProcessMemory(handle,address,buff,size,None)

def wGetSystemInfo():
    info=SYSTEM_INFO()
    GetSystemInfo(info)
    return info

def wVirtualQueryEx(handle,address):
    info=MEMORY_BASIC_INFORMATION64()#32bit에는 MEMORY_BASIC_INFORMATION32 써야 함
    size=sizeof(info)
    #print size
    address=DWORD64(address)
    #for x in range(2):
    #    r=VirtualQueryEx(handle,address,byref(info),size)
    #    #print r #WHAT THE FUCK BUG
    VirtualQueryEx(handle,address,byref(info),size)
    return info
