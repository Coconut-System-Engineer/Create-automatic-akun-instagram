  GNU nano 4.8                                                               automisasi Istagram.py                                                                          
import os
import random
import sys
import time
from time import sleep

os.system('clear')
def mengetik (s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.4)
print ('\033[1;94mLoading...')
sleep(0.1)
mengetik(' > > > > > > > > > > > > > > > > > > > > > > > > > >] 100%')
sleep(1)
os.system('clear')

print "\033[1;00m==============================================================================================================="
sleep(0.1)
print "\033[1;91m*********************___________***Auto Create Akun Instagram***___________************************************"
sleep(0.1)
print "*        0000000000000 000000000000 000000000000         000000             000000       00000000000000000000 *"
sleep(0.1)
print "*       000       0000 000000000000 0000000000000      00000000000         000000000     00000000000000000000 *"
sleep(0.1)
print "*      000     00 0000 0000         0000    000000   000000  000000     000000  000000   00      00000     00 *"
sleep(0.1)
print "*     000       00000  0000         0000    000000  00000      00000   00000       00000         00000        *"
sleep(0.1)
print "*     000              000000000000 0000    00000  0000          0000 0000           0000        00000        *"
sleep(0.1)
print "*     000      00000   000000000000 00000000000    0000          0000 0000           0000        00000        *"
sleep(0.1)
print "*     000     00 0000  0000         00000000000     00000      00000   00000       00000         00000        *"
sleep(0.1)
print "*      000  0000 0000  0000         0000  000000     000000  000000     000000  000000           00000        *"
sleep(0.1)
print "*       000      0000  000000000000 0000   000000      00000000000        0000000000             00000        *"
sleep(0.1)
print "*        000000000000  000000000000 0000    000000       000000             000000          00000000000000    *"
sleep(0.1)
print "\033[00m \033[1;94m*********************___________****** C O C O N U T ******___________****************************************"
sleep(0.1)
print "\033[00m==============================================================================================================="
sleep(0.1)

# r = read
# w = write
# a = append

print '\033[1;94m********** Input Untuk Membuat File List **********'
print '======================================================'

#input untuk masukan dalam daftar list  
Email = raw_input('Masukan Nomor Telpon : ')
FullName = raw_input('Masukan Nama Full : ')
UserName = raw_input('Masukan User Name : ')
print '======================================================'

# membuat list
with open('no_tlp.txt','w') as f:
	f.write(Email + '\n')
with open('FullName.txt','w') as f:
	f.write(FullName +'\n')
with open('UserName.txt','w') as f:
	f.write(UserName +'\n')
with open('backup.txt', 'a') as f :
	f.write('email/no_tlp : ' + Email + '\n')
	f.write('Full Name : ' + FullName + '\n')
	f.write('Username : ' + UserName + '\n')

# menampilkan list yang sudah dibuat
print '\n'
print '********** daftar file yang baru dibuat **********'
print '======================================================'
with open('no_tlp.txt','r') as f:
     for Email in f.readlines():
	print 'Email : ' + Email
	f.close()
with open('FullName.txt','r') as f:
     for FName in f.readlines():
	print 'Full Name : ' + FName
	f.close()
with open('UserName.txt','r') as f:
     for UName in f.readlines():
	print 'User Name : ' + UName
	f.close()
print '======================================================'

jawab = 'ya'
hitung = 1
while(True) :
	hitung += 1
	print '********** Input Form Untuk menambahkan isi List **********'
	print "==========================================================="

	#input untuk masukan dalam daftar list  
	Email = raw_input('Masukan Nomor Telpon : ')
	FullName = raw_input('Masukan Nama Full : ')
	UserName = raw_input('Masukan User Name : ')
	print "=========================================================="
	print '\n'

	# menambahkan list
	with open('no_tlp.txt','a') as f:
        	f.write(Email + '\n')
	with open('FullName.txt','a') as f:
        	f.write(FullName + '\n')
	with open('UserName.txt','a') as f:
        	f.write(UserName + '\n')
	with open('backup.txt', 'a') as f :
        	f.write('email/no_tlp : ' + Email + '\n')
	        f.write('Full Name : ' + FullName + '\n')
        	f.write('Username : ' + UserName + '\n')

	print "========================================================="

	# menampilkan list yang sudah dibuat
	print '*************** Daftar List yang baru di tambahkan **************'
	with open('no_tlp.txt','r') as f:
	     for Email in f.readlines():
	        print 'Email : ' + Email
        	f.close()
	with open('FullName.txt','r') as f:
	     for FName in f.readlines():
	        print 'Full Name : ' + FName
        	f.close()
	with open('UserName.txt','r') as f:
	     for UName in f.readlines():
	        print 'User Name : ' + UName
        	f.close()
	print "=========================================================================================="
	jawab = raw_input('input key \"ya" jika ingin tambah list akun, jika tidak masukan key \"tidak" !!! : ' )
	if jawab == 'tidak' :
		break

print '\033[1;00m \033[1;92mTotal akun list yang dibuat : ' + str(hitung) + '\n' 
print '*************** proses penambahan list selesai ***************'
