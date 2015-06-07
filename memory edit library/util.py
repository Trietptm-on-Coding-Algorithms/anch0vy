from ctypes import *
BYTE      = c_ubyte
WORD      = c_ushort
DWORD     = c_ulong
DWORD64   = c_ulonglong
LPBYTE    = POINTER(c_ubyte)
LPTSTR    = POINTER(c_char) 
HANDLE    = c_void_p
PVOID     = c_void_p
LPVOID    = c_void_p
UINT_PTR  = c_ulong
SIZE_T    = c_ulonglong

PROCESS_VM_READ=0x0010
PROCESS_VM_WRITE=0x0020
PROCESS_VM_OPERATION=0x0008
PROCESS_QUERY_INFORMATION=0x0400

MEM_COMMIT=0x1000
MEM_FREE=0x10000
MEM_RESERVE=0x2000


class STARTUPINFO(Structure):
    _fields_ = [
        ("cb",            DWORD),        
        ("lpReserved",    LPTSTR), 
        ("lpDesktop",     LPTSTR),  
        ("lpTitle",       LPTSTR),
        ("dwX",           DWORD),
        ("dwY",           DWORD),
        ("dwXSize",       DWORD),
        ("dwYSize",       DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",       DWORD),
        ("wShowWindow",   WORD),
        ("cbReserved2",   WORD),
        ("lpReserved2",   LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",    HANDLE),
        ("hStdError",     HANDLE),
        ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
        ]


class PROC_STRUCT(Structure):
    _fields_ = [
        ("wProcessorArchitecture",    WORD),
        ("wReserved",                 WORD),
]


class SYSTEM_INFO_UNION(Union):
    _fields_ = [
        ("dwOemId",    DWORD),
        ("sProcStruc", PROC_STRUCT),
]


class SYSTEM_INFO(Structure):
    _fields_ = [
        ("uSysInfo", SYSTEM_INFO_UNION),
        ("dwPageSize", DWORD),
        ("lpMinimumApplicationAddress", LPVOID),
        ("lpMaximumApplicationAddress", LPVOID),
        ("dwActiveProcessorMask", DWORD),
        ("dwNumberOfProcessors", DWORD),
        ("dwProcessorType", DWORD),
        ("dwAllocationGranularity", DWORD),
        ("wProcessorLevel", WORD),
        ("wProcessorRevision", WORD),
]

class MEMORY_BASIC_INFORMATION32(Structure):
    _fields_ = [
        ("BaseAddress",DWORD),
        ("AllocationBase",DWORD),
        ("AllocationProtect",DWORD),
        ("RegionSize",SIZE_T),
        ("State",DWORD),
        ("Protect",DWORD),
        ("Type",DWORD),
]

class MEMORY_BASIC_INFORMATION64(Structure):
    _fields_ = [
        ("BaseAddress",DWORD64),
        ("AllocationBase",DWORD64),
        ("AllocationProtect",DWORD),
        ("__alignment1",DWORD),
        ("RegionSize",DWORD64),#SIZE_T),
        ("State",DWORD),
        ("Protect",DWORD),
        ("Type",DWORD),
        ("__alignment2",DWORD)
]
    
