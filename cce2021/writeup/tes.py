import base64
from Crypto.Cipher import AES

enc = "1z2YlwM84JhKbU5C40yZjD7USxpDFSy7XMXLL1m+nWp3AxFFINxXUKy21aPnR9yOdjIvTyuzHyiOgTwpy1GjHcPP3HFSz/baqKFffl7+uBxZ2UqEtLVmNpIWAH+PMHfiit4dJReIDq7Qt/Xu6d/EgXzL0tpkR5Ofck/6qzV4wvnniHQf3tFS4V06HGsIX0PB" # Flag
test = b'Xaa9o/IsDHDYPoOmWj4xr4qzE9Nrj7IKeSPmSXDfM/oXeSRA1sVk19vXyfyn2obyfuqzq1MLLvBtyrgvLy5tSGsK95c7Qs6K/62ibKwoQLCVyOsEr07clUBSWplk/vOXmeIWGl7mvP+YMHnUR0Q3YfDR98/ySbY3qK4EzFs8Qn0XeSRA1sVk19vXyfyn2obyfuqzq1MLLvBtyrgvLy5tSJoeKXW12UsbasavHvL5zDFXPUTx5bjk2a8NyCfRVD+j/asqalLt5Ayoyrc730vIZqJgNX7PPZz/gfr7cCjax4bgtmeZ/Qis54TvMwLMl3i8tBdw4MfO0YiRXamIKkOGpRd5JEDWxWTX29fJ/KfahvJ+6rOrUwsu8G3KuC8vLm1ImJV8jA289/8wX88VqkLfr54+LxVb2BP6G8R4JGt+APVQ8ctO5eQNcfKZ6Wdd27zZ9KJ+GhKiqMmN0wiW+4aWEuC2Z5n9CKznhO8zAsyXeLy0F3Dgx87RiJFdqYgqQ4al1pYpt9RT0knJsH9b+I1R2mN3+yC4ctjxuIPbriLiHfgXeSRA1sVk19vXyfyn2obyfuqzq1MLLvBtyrgvLy5tSAPz6oicXSnSntXh4h3MpwLIfRtw6tCXZTjKZSUH442KF3kkQNbFZNfb18n8p9qG8n7qs6tTCy7wbcq4Ly8ubUg=' # "0"*256


# Step 1: Bruteforce to find the key
enc_bytes = base64.b64decode(test)
print(len(enc_bytes))
print(len(enc_bytes) / 16)

iv = 'cce2021_i-vector' # Why iv exist?
keys = []
BS = 16
padd = lambda s: s + (BS - len(s) % BS) * bytes([BS - len(s) % BS])

for i in range(len(enc_bytes) // 32):
    for j in range(0, 0x100):
        sus = bytes([j])
        key = padd(sus)
        print(sus)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(enc_bytes[i*32: i*32 + 32])
        if decrypted == b'0000000000000000\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10':
            keys.append(sus.decode())

print(''.join(keys)) # @3sK3yT03nc0d3M3


# Step 2: Decrypt the real flag using extracted key
flag = []
key = ''.join(keys).encode()
enc_bytes = base64.b64decode(enc)
print(len(enc_bytes) / 16) # 9 => 2+2+2+2+1 : plaintext: 5 block
n = len(key) // 5 # n = 3
keys = [key[i * n:(i + 1) * n] for i in range((len(key) + n - 1) // n )] 
print(keys)
for i in range(len(enc_bytes) // 32):
    cipher = AES.new(padd(keys[i]), AES.MODE_ECB)
    flag.append(cipher.decrypt(enc_bytes[i*32:i*32+32])[:16].decode())

# Last block. I hate python string slicing
cipher = AES.new(padd(keys[4]), AES.MODE_ECB)
flag.append(cipher.decrypt(enc_bytes[-16:]).decode())

print("".join(flag)) 
