from Crypto.Util.number import *
from random import randint
import os

e = 65537
print(e)

p = randint(1, 2**256)
q = randint(1, 2**256)

d = inverse(e, (q - 1)*(p - 1))

N = p * q



flag = open('message.txt', 'rb').read()

ciphertext = hex(pow(bytes_to_long(flag), e, N))[2:]

public_key = f"Public Key = [{N}, {e}]"
ciphertext = f"CipherText = {ciphertext}"

file = open('cipher.txt','w')
file.writelines(public_key + '\n')
file.writelines(ciphertext)
