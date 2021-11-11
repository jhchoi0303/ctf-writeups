string="bagelarenotwholewheatsometimes"

for i in range(0,len(string)):
	print(chr((ord(string[i])+(i%5))),end="")
	
