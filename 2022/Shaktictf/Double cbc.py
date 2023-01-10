from pwn import *
from Crypto.Util.strxor import strxor
context.log_level='debug'
s1 = "a"*16
s1hex = s1.encode("hex")

l = remote("13.232.45.235",31938)
l.recv()
l.sendline("3")
l.recv()
l.sendline("415f68617070795f6362635f6d6f6465")
l.recv()
l.sendline("0")
l.recv()
l.sendline(s1hex)
l.recvline()
l.recvline()

y = l.recvline().strip()
print(type(y))


i3 = strxor(strxor(s1,"415f68617070795f6362635f6d6f6465".decode("hex")),"5519ab6975a05390ad637e11560fcfcb".decode("hex"))
#IV "415f68617070795f6362635f6d6f6465" 를 추가로 XOR 해준 부분

print(i3)

s2 = s1+i3
s2hex = s2.encode("hex")
print(s1hex)
print(s2hex)