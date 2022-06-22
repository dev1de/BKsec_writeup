from SageMath           import *
from Crypto.Util.number import *

p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 5

flag = open("flag.txt", "rb").read()

print(f'e = {e}')
print(f'N = {N}')
print(f'l = {len(flag)}')
print(f'c = {pow(bytes_to_long(flag), e, N)}')


