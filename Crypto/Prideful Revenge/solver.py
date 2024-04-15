from Crypto.Util.number import *
from libnum import nroot


ciphertext = ''         # insert hex ciphertext here
N =                     # insert public key N here (the modulus)
e = 65537
def generate_prime(p):
    while(True):
        p += 1 
        if(isPrime(p)):
            break
    return p

p0 = nroot(N//(7*5*5*3*3*3), 4)
p1 = p0
for i in range(100000):
  if((N%p1 == 0) and (isPrime(p1))):
    print('Found')
    break
  p1 -= 1
p2 = generate_prime(p1 * 3) 
p3 = generate_prime(p2 * 5)
p4 = generate_prime(p3 * 7)
phi = (p1-1)*(p2-1)*(p3-1)*(p4-1)
flag = long_to_bytes(pow(int(ciphertext,16), inverse(e, phi), N))
print(flag)
