from Crypto.Util.number import *

e = 65537


p1 = getPrime(64)
p2 = p1
p3 = getPrime(64)
p4 = p3
p5 = getPrime(64)
p6 = p5
p7 = getPrime(64)
p8 = p7
p9 = getPrime(64)



N = p1 * p2 * p3 * p4 * p5 * p6 * p7 * p8 * p9



flag = open('message.txt', 'rb').read()

ciphertext = hex(pow(bytes_to_long(flag), e, N))[2:]

public_key = f"Public Key = [{N}, {e}]"
ciphertext = f"CipherText = {ciphertext}"

file = open('cipher.txt','w')
file.writelines(public_key + '\n')
file.writelines(ciphertext)
