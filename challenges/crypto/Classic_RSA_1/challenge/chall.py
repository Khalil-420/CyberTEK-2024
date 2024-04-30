from Crypto.Util.number import *
from random import randint
import os
sys.set_int_max_str_digits(100000000)

e= getPrime(12)
print(e)

p = getPrime(256) ** e
q = getPrime(256) ** e


N = p * q


flag = open('message.txt', 'rb').read()

ciphertext = hex(pow(bytes_to_long(flag), e, N))[2:]

public_key = f"Public Key = [{N}, {e}]"
ciphertext = f"CipherText = {ciphertext}"

file = open('cipher.txt','w')
file.writelines(public_key + '\n')
file.writelines(ciphertext)
