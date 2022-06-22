def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

import pwn
p = pwn.remote("139.59.163.221", 30269)
p.recvuntil("> ")
p.sendline("1")
p.recvuntil(": ")
p.sendline(b"A"*31)
p.recvuntil("> ")
p.sendline("2")
p.recvuntil("Vault: ")
password = p.recvline()
print(password)