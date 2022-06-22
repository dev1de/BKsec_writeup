import base64
f = open("dump.bin","r")
s = f.read()
print(base64.standard_b64encode(s))
