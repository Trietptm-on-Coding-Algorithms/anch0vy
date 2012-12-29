from opcode_parse_util import *
from vm_opcode_gen import *
from vm_opcode import *
print 'test'

while(1):
    code = raw_input('code: ')
    opcode = parser(code)
    print opcode
