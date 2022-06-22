from pwn import *
import os
import subprocess as sub
from multiprocessing import current_process
if  os.fork():
	sleep(2)
	print('echoing...')
	os.system("echo -n '99999999hmdoxevfyoqa' > ./pqbix")
	print('written')
else:
	print('Parent process')
	s=[]
	os.system("./babyrev_level6_testing1")

