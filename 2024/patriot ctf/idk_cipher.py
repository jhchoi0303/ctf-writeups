import base64

# Given encoded string
encoded_string = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="

# Secret key used in the original encoding
secret_key = 'secretkey'

# Decode the base64 encoded value to get the encoded string
decoded_string = base64.b64decode(encoded_string).decode()

# Determine the original plaintext length
length = len(decoded_string)

# Initialize an empty string to hold the decoded plaintext
plaintext_arr = [''] * length

# Decoding process: Use the encoded string and reverse engineering logic
for i in range(0, length, 2):
    # Retrieve original character codes from encoded pairs
    enc_p1 = decoded_string[i]
    enc_p2 = decoded_string[i + 1]
    
    # XOR with the secret key to get the original characters
    c1 = ord(enc_p1) ^ ord(secret_key[i // 2 % len(secret_key)])
    c2 = ord(enc_p2) ^ ord(secret_key[i // 2 % len(secret_key)])
    
    # Place decoded characters in the correct position
    plaintext_arr[i // 2] = chr(c1)
    plaintext_arr[length - 1 - (i // 2)] = chr(c2)

# Join the decoded characters to form the original plaintext
decoded_plaintext = ''.join(plaintext_arr)
decoded_plaintext
