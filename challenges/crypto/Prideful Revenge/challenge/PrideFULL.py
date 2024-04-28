from Crypto.Util.number import *
from random import randint
e= 65537


def generate_prime(p):
    while(True):
        p += 1 
        if(isPrime(p)):
            break
    return p


n = randint(1,2**512 - 1)

p1 = generate_prime(n)
p2 = generate_prime(p1 * 3) 
p3 = generate_prime(p2 * 5)
p4 = generate_prime(p3 * 7)

N = p1 * p2 * p3 * p4

flag = open('message.txt', 'rb').read()

ciphertext = hex(pow(bytes_to_long(flag), e, N))[2:]

public_key = f"Public Key = [{N}, {e}]"
ciphertext = f"CipherText = {ciphertext}"

file = open('cipher.txt','w')
file.writelines(public_key + '\n')
file.writelines(ciphertext)
