from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from hashlib import sha256

from secret import Flag, p, private_a, private_b

F = GF(p)
E = EllipticCurve(F, [47711, 39749])
G = E(56190703330641171196318160940804991527609142654842619859338273539667008627692 , 18467617306692418403904248124162118311641513792566391404833878807454794983866)

A = G * private_a  
print(A)
# A = (24167001443353793704143421300014841633485002778327055775497956317064253692242 : 10636782644097658169867621951692685548587392289640718010259647718954626529439 : 1)

B = G * private_b
print(B)
# B = (64717507767429265706953693719672201339074449737514438527963172288485256555695 : 58623770025789344280791314074865822698034703254587311829324744416870138486230 : 1)


C = private_a * B


hash = sha256()
hash.update(long_to_bytes(C[0]))
key = hash.digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(Flag, 16))

print(encrypted)
# encrypted = b'\xee\xf6\x7f\x9b\x146\x99\xdaNK6~\x95\xbd\xc5\xfe\xa9\x17\x17\xeb\x8e2%,\x9c\x9bt\xf2\xf4\x8bp\x88\x91\x81uym\xe5w\xe4n\xa4\xc9\x8c1\xdf\x08A\x0b\xe1\x8dZ\x83\x1a\xb0*\x11i\xed)\xf1$\xdb*'
