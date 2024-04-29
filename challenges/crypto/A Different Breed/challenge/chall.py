import random
import os
from Crypto.Cipher import AES
from Crypto.Util.number import isPrime, inverse


Quotes1 = open('Quotes1.txt','r').read().split('\n')

Flag = open('flag.txt','rb').read()
assert(len(Flag) == 32)

Flag1 = Flag[:16]
Flag2 = Flag[16:]


class myAES:
    def __init__(self):
        self.BLOCK_SIZE = 128 // 8
        self.master_key = Flag1
        self.iv         = Flag2
    
    def message_adjust(self, message):
        x = -len(message)%self.BLOCK_SIZE
        message += x * b'\x00'
        return message
    
    def encrypt(self, plaintext):
        plaintext = bytes.fromhex(plaintext)
        plaintext = self.message_adjust(plaintext)
        cipher = AES.new(self.master_key, AES.MODE_CBC, iv=self.iv)
        return cipher.encrypt(plaintext)
    
    def decrypt(self, ciphertext):
        ciphertext = bytes.fromhex(ciphertext)
        
        if (len(ciphertext)%16 != 0):
            print('Bruuuhhhhhhhh...')
            exit()
        
        cipher = AES.new(self.master_key, AES.MODE_CBC, iv=self.iv)
        return cipher.decrypt(ciphertext)
    


class myRSA:
    def __init__(self):
        self.PRIME_BYTE_SIZE = 512 // 8
        
        self.p = int((Flag1*3 + os.urandom(self.PRIME_BYTE_SIZE - len(Flag1)*3)).hex(), 16)     # layn l5asara
        self.q = int((Flag2*3 + os.urandom(self.PRIME_BYTE_SIZE - len(Flag2)*3)).hex(), 16)

        self.p = self.generate_prime(self.p)
        self.q = self.generate_prime(self.q)

        self.public = [65537, self.p * self.q]
        self.private = [inverse(self.public[0], (self.p - 1) * (self.q - 1)), self.p * self.q]
    
    def generate_prime(self, p):
        while(True):
            if isPrime(p):
                return p
            p += 1
            

    def encrypt(self, plaintext):
        plaintext = int(plaintext, 16)
        ciphertext = pow(plaintext, self.public[0], self.public[1])
        return hex(ciphertext)
    
    def decrypt(self, ciphertext):
        ciphertext = int(ciphertext, 16)
        plaintext = pow(ciphertext, self.private[0], self.private[1])
        return hex(plaintext)



def main():

    print("""                 __      __
    _________          ___.                      ___________         __    
    \_   ___ \  ___.__.\_ |__     ____  _______  \__    ___/  ____  |  | __
    /    \  \/ <   |  | | __ \  _/ __ \ \_  __ \   |    |   _/ __ \ |  |/ /
    \     \____ \___  | | \_\ \ \  ___/  |  | \/   |    |   \  ___/ |    < 
     \______  / / ____| |___  /  \___  > |__|      |____|    \___  >|__|_ \\
            \/  \/          \/       \/                          \/      \/ \n""")
    while True:
        random.shuffle(Quotes1)
        print(Quotes1[0])
        print(" [+] To encrypt using RSA, please press 1")
        print(" [+] To encrypt using AES, please press 2")
        algo = input(" > ")
        print()

        
        if algo == '1':
            Cipher = myRSA()
            print(f'Public Key: {Cipher.public}')
        elif algo == '2':
            Cipher = myAES()
        else:
            print(' i see...')
            continue
        
        print(" [+] to encrypt, please press 1")
        print(" [+] to decrypt, please press 2")

        print(" [+] to get the flag.... try harder")
        operation = input(" > ")
        
        if operation == '1':
            msg = input(" message in hex > ")
            print(f'Ciphertext: {Cipher.encrypt(msg)}')
        
        elif operation == '2':
            msg = input(" ciphertext in hex > ")
            print(f'Plaintext: {Cipher.decrypt(msg)}')
        
        elif operation == '3':
            print(' i see...')
            continue
        


main()