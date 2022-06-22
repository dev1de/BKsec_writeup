import socket
import pwn
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p = pwn.process("./babyrev_level9_teaching1")
server_addr = ('localhost',47507)
s.connect(server_addr)

def swap(index_a, index_b):
    tmp = license[index_a]
    license[index_a] = license[index_b]
    license[index_b] = tmp


def reverse():
    for i in range(int(len(license)/2)):
        swap(i,len(license)-i-1)


def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


license = [b'\x08', b'\xcc', b'\x77', b'\x36', b'\x0d', b'\xde', b'\x7a', b'\x3e', b'\x08', b'\xd5', b'\x6c', b'\x3f', b'\x02', b'\xd9']

#reverse()
#license = xor(license,0x321c)
#reverse()
#license = xor(license, [b'\x69',b'\x7f',b'\x9d',b'\x04'])

license = b'vkcomnqbekztdav'
skipped_bytes = 12

s.send(b"A"*skipped_bytes+license)
s.close()
print(p.readall())
