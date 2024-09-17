
from pwn import *
alpha_dict = {}
r = remote("24.199.110.35", 42189)

r.recv()

r.sendline("16")


payload = str(r.recv().strip())[10:-2]
print(payload)
payload = payload.split(" + ")

answer = int(payload[0])+int(payload[1])

r.sendline(str(answer))


for i in range(15):
    totaltime = pow(2, i)

    print(r.recvline())

    r.recvline()
    time.sleep(totaltime / 3)
    r.recvline()
    time.sleep(totaltime / 3)
    r.recvline()
    time.sleep(totaltime / 3)


    payload = str(r.recv().strip())[10:-2]
    print(payload)
    payload = payload.split(" + ")

    answer = int(payload[0])+int(payload[1])

    r.sendline(str(answer))

print(str(r.recvline()))
print(str(r.recvline()))
print(str(r.recvline()))
print(str(r.recvline()))

print(str(r.recvline()))

r.close()


#print(alpha_dict)
