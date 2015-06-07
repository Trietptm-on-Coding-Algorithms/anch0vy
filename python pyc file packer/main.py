import marshal
l=lambda x:x
type_function=type(l)
type_code=type(l.func_code)

mycode=type_code(
ent.func_code.co_argcount
,ent.func_code.co_nlocals
,ent.func_code.co_stacksize
,ent.func_code.co_flags
,ent.func_code.co_code
,ent.func_code.co_consts
,ent.func_code.co_names
,tuple()
,''#,ent.func_code.co_filename
,ent.func_code.co_name
,ent.func_code.co_firstlineno
,ent.func_code.co_lnotab
    )

pyc='03 F3 0D 0A F1 F8 CC 54'.replace(' ','').decode('hex')
#pyc='03 F3 0D 0A 32 A7 C6 54'.replace(' ','').decode('hex')
with open('testWW.pyc','wb') as f:
    f.write(pyc+marshal.dumps(mycode))
    
#print e#nt.func_code.co_argcount,ent.func_code.co_nlocals,ent.func_code.co_stacksize,ent.func_code.co_flags,ent.func_code.co_code,ent.func_code.co_consts,ent.func_code.co_names,ent.func_code.co_varnames,ent.func_code.co_filename,ent.func_code.co_name,ent.func_code.co_firstlineno,ent.func_code.co_lnotab
