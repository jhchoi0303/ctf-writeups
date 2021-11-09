import base64

key="???????"

flag="cce2021{??????????????????????????????????}"
plain= base64.b64decode("Bg0PXUlMTx46AgYKIRcWMR4HHCENDAMaAxwNCjoBBAomPRELCRgODQ1fGA==")
plain=plain.decode('utf-8')



#key
key=""
for i in range (0,7):
	#print(chr(ord(plain.decode('utf-8')[i])^ord(flag[i])), end="")
	key+=(chr(ord(plain[i])^ord(flag[i])))



def decrypt(plain):
	res=""
	for _ in range(len(plain)):
		res+=chr(ord(key[_%7])^ord(plain[_]))
	return res

print(decrypt(plain))




