import pwn

p = pwn.process(["./babyrev_level11_testing1","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"])
p.sendline("922")
p.sendline("b8")
for i in range(4):
    p.sendline(hex(2339+i)[2:])
    p.sendline("0")
print(p.clean())