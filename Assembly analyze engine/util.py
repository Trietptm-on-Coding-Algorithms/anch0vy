import struct
def unpack_us1(string):
    return struct.unpack('<B',string)[0]

def unpack_us2(string):
    return struct.unpack('<H',string)[0]

def unpack_us4(string):
    return struct.unpack('<I',string)[0]

def unpack_s1(string):
    return struct.unpack('<b',string)[0]

def unpack_s2(string):
    return struct.unpack('<h',string)[0]

def unpack_s4(string):
    return struct.unpack('<i',string)[0]
