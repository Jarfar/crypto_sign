from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5


key = RSA.generate(1024)

kf = open('publick.pem', 'wb')
kf.write(key.exportKey('PEM'))
kf.close()

with open('message.txt', 'r') as f:
    h = SHA.new(f)

