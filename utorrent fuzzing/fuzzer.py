# -*- coding: cp949 -*-
from pydbg import *
from pydbg.defines import *

import utils
import random
import threading
import os
import shutil
import time

exe_path = '''C:\Documents and Settings\정현식\Application Data\uTorrent\uTorrent_original.exe'''

class file_fuzzer:
    def __init__(self,exe_path):
        self.exe_path = exe_path
        self.targetfile = '''sample.torrent'''
        self.copyfile = '''test.torrent'''
        self.test = '''"C:\Documents and Settings\정현식\바탕 화면\dev\trunk\utorrent fuzzing\test.torrent"'''
        self.ext = 'torrent'
        self.mutate_key = {}
        self.mutate_count = 10#변경될 수 있음
        self.iteration = 0
        self.crash = None
        self.pid = None
        self.in_accessv_handler = False
        self.dbg = None
        self.running = False
        self.ready = False
        self.eip = None
        self.runtime = 6

    def monitor_debugger(self): 
        print "[#] Monitoring... ",
        #지정된 시간만큼 sleep하고, process를 종료시킨다.
        counter = 0

        while counter < self.runtime:
            time.sleep(1)
            print counter,
            counter += 1
        time.sleep(1)


        try:
            self.dbg.terminate_process()
        except:
            pass

        self.pid = None
        self.running = False


    def mutate_file(self):
        
        fd=open(self.copyfile,'rb')
        stream = fd.read()
        stream_length=len(stream)
        fd2=open(self.copyfile,'wb')
        fd2.write(stream)
        attack_strs = ["\x00",'\x0d','\x0a','\xff']

        for i in range(self.mutate_count):
            rand_offset = random.randint(0,stream_length-1)
            self.mutate_key[rand_offset]={hex(ord(stream[rand_offset:rand_offset+1]))}
            attack_str = random.choice(attack_strs)
            fd2.seek(rand_offset)
            fd2.write(attack_str)
        fd.close()
        fd2.close()
        return
        
        


    def check_accessv(self,dbg):
        print "*************************\n[*]WTF!!\n*************************"
        self.in_accessv_handler = True
        crash_bin = utils.crash_binning.crash_binning()
        crash_bin.record_crash(dbg)
        self.crash = crash_bin.crash_sysnopsis()

        eipoff = self.crash.find('EIP')
        eaxoff = self.crash.find('EAX')
        self.eip = self.crash[eipoff+5:eaxoff-3]
        eipname = self.crash[eipoff+5:eipoff+13]
        print 'EIP= ',self.eip
        fd3 = open('crashes.txt','a')
        fd3.write(self.eip)
        fd3.write('  iteration : %s' % self.iteration)

        crash_fd = open('crashes\\crash-%s [%d].txt' % (eipname,self.iteration),'w+')
        crash_fd.write('utils log')
        crash_fd.write(self.crash)
        crash_fd.write('mutate_key log')
        crash_fd.write('%s ' % self.mutate_key)
        crash_fd.write('end\n\n\n')

        shutil.copy(self.copyfile,'crashes\\crash- %s [%d].%s' % (eipname,self.iteration,self.ext))
        fd3.close()
        crash_fd.close()
        self.dbg.terminate_process()
        self.in_accessv_handler =False
        return DBG_EXCEPTION_NOT_HANDLED


        

    def start_debugger(self):
        print '\n[*]starting debugger for iteration %d'% self.iteration
        self.running = True
        self.dbg = pydbg()
        self.dbg.set_callback(EXCEPTION_ACCESS_VIOLATION,self.check_accessv)
        pid = self.dbg.load(self.exe_path,self.copyfile)
        self.pid = self.dbg.pid
        try:
            self.dbg.run()
        except:
            print 'debug1'#debug
            self.dbg.terminate_process()



        
    def fuzz(self):
        while 1:
            if not self.running:
                self.iteration = self.iteration + 1
                try:
                    shutil.copy(self.targetfile,self.copyfile)
                    self.mutate_file()
                except:
                    print 'debug2'#debug

                pydbg_thread = threading.Thread(target=self.start_debugger)
                pydbg_thread.setDaemon(0)
                pydbg_thread.start()

                while self.pid == None:
                    time.sleep(1)

                monitor_thread = threading.Thread(target=self.monitor_debugger)
                monitor_thread.start()
                
                
fuzzer = file_fuzzer(exe_path)
fuzzer.fuzz()
