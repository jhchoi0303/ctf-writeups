from pwn import *

context.log_level='debug'

p=remote("20.194.123.97",11111)


for i in range(0,200):
	stringa="stage "+str(i)
	p.recvuntil(stringa)

	a=int(p.recvuntil(' ')[:-1])
	b=int((p.recvuntil(' ')[:-1]))
	c=float((p.recvuntil('\n')[:-1]))  
		
	if( (a+b) == c):
			p.send("+")
	elif( (a-b) == c):
			p.send("-")
	elif( (a*b == c)):
			p.send("*")
	elif(float(float(a)/float(b)) == c):
			p.send("/")
	
		
	






