from sage.all import matrix, Zmod
from Crypto.Util.number import *


flag = open('flag.txt', 'rb').read()

n = 2
N_BITS = 256
N_FRAGS = n**2

e = 65537

Primes = [getPrime(N_BITS // N_FRAGS) for i in range(4)]

N = 1
for i in Primes:
  N *= i

fragments = [int(flag[i * ((len(flag)//N_FRAGS) + 1): (i + 1) * ((len(flag)//N_FRAGS) + 1) ].hex(), 16) for i in range(N_FRAGS)]
Plaintexts = matrix(Zmod(N), [[fragments[n * i + j] for j in range(n)] for i in range(n)])


Ciphertexts = Plaintexts ** e

with open("ciphertext.txt", "w") as file:
    file.write(f"N = {N}\n\n")
    file.write("Ciphertext Matrix:\n\n")
    for row in Ciphertexts:
        for num in row:
            file.write(str(num) + " ")
        file.write("\n\n")
