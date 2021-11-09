de_flag=[28777,25455,17236,18043,12598,24418,26996,29535,26990,29556,13108,25695,28518,24376,24368,13411,12343,13872,25725]
len(de_flag)
flag=[112,105,99,111,67,84,70,123]
print( (ord('p') << 8) + ord('i') == de_flag[0])
print( (ord('c') << 8) + ord('o') == de_flag[1])
print( (ord('C') << 8) + ord('T') == de_flag[2])
print( (ord('F') << 8) + ord('{') == de_flag[3])

for a in range(0,19):
    for j in range(32,127):
        flag.insert(2*a,j)

        for s in range(32,127):
            flag.insert(2*a+1,s)
            
            if((((flag[2*a])<<8)+flag[2*a+1])==de_flag[a]):
                print(chr(flag[2*a]),end="")
                print(chr(flag[2*a+1]),end="")
                
        



#flag[2]= chr((de_flag[1]) - ((ord)('i') << 8))


